# Copyright (c) 2022, Richard Kwa and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint
from frappe.utils import formatdate, nowdate
from frappe.model.document import Document
from frappe import new_doc

import erpnext

class patch_postdate(Document):
	def validate(self):
		if self.from_date >= self.to_date:
			frappe.throw("To Date must be later than From Date - PY")

	@frappe.whitelist()
	def before_save(self):
		get_name = frappe.db.sql(f"""SELECT parent from `tabSales Taxes and Charges` 
			WHERE parenttype = 'Sales Invoice' """, as_dict=True)
		if get_name:
			for d in get_name:
				frappe.msgprint("parent {0}".format(d.parent))
				get_postdate = frappe.db.sql(f"""SELECT name, posting_date from `tabSales Invoice`
					WHERE name = %s""", (d.parent), as_dict=True)
				for p in get_postdate:
					frappe.msgprint("update {0}".format(p.posting_date))
					frappe.msgprint(formatdate(p.posting_date))
					frappe.msgprint(formatdate(p.posting_date, "YYYY-MM-dd"))
					fdate = formatdate(p.posting_date, "YYYY-MM-dd")
					frappe.msgprint("update {0}".format(fdate))

				#	frappe.db.sql("""update `tabSales Taxes and Charges` set posting_date=%s where parent=%s AND parenttype='Sales Invoice' """, (formatdate(p.postdate,"dd-MM-YYYY"), p.name))
					frappe.db.sql("update `tabSales Taxes and Charges` set posting_date=%s where parent=%s AND parenttype='Sales Invoice' ", (fdate, p.name))
				#   working
				#	frappe.db.sql("update `tabSales Taxes and Charges` set posting_date=%s where parent=%s AND parenttype='Sales Invoice' ", ("2022-03-31", p.name))
					frappe.db.commit()