# Copyright (c) 2022, Richard Kwa and contributors
# For license information, please see license.txt
import frappe
from frappe import _, msgprint
from frappe.utils import formatdate, nowdate
from frappe.model.document import Document
from frappe import new_doc

import erpnext

class patch_postdate_sales(Document):
	@frappe.whitelist()
	def before_save(self):
		get_name = frappe.db.sql(f"""SELECT parent from `tabSales Taxes and Charges` 
			WHERE parenttype = 'Sales Invoice' """, as_dict=True)
		if get_name:
			for d in get_name:
				frappe.msgprint("parent {0}".format(d.parent))
				get_postdate = frappe.db.sql(f"""SELECT name, customer, posting_date from `tabSales Invoice`
					WHERE name = %s""", (d.parent), as_dict=True)
				for p in get_postdate:
					fdate = formatdate(p.posting_date, "YYYY-MM-dd")
					frappe.db.sql("update `tabSales Taxes and Charges` set posting_date=%s, csname=%s where parent=%s AND parenttype='Sales Invoice' ", (fdate, p.customer, p.name))
					frappe.db.commit()
