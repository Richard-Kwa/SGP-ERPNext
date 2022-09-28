# Copyright (c) 2022, Richard Kwa and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint
from frappe.utils import formatdate, nowdate
from frappe.model.document import Document
from frappe import new_doc

class patch_posttdate_purchase(Document):

	@frappe.whitelist()
	def before_save(self):
		get_name = frappe.db.sql(f"""SELECT parent from `tabPurchase Taxes and Charges` 
			WHERE parenttype = 'Purchase Invoice' """, as_dict=True)
		if get_name:
			for d in get_name:
				frappe.msgprint("parent {0}".format(d.parent))
				get_postdate = frappe.db.sql(f"""SELECT name, supplier, posting_date from `tabPurchase Invoice`
					WHERE name = %s""", (d.parent), as_dict=True)
				for p in get_postdate:
					fdate = formatdate(p.posting_date, "YYYY-MM-dd")
					frappe.db.sql("update `tabPurchase Taxes and Charges` set posting_date=%s, csname=%s where parent=%s AND parenttype='Purchase Invoice' ", (fdate, p.supplier, p.name))
					frappe.db.commit()