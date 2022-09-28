# Copyright (c) 2022, Richard Kwa and contributors
# For license information, please see license.txt

import frappe

from frappe import _, _dict
from frappe.utils import cint, flt, getdate
from erpnext import get_company_currency, get_default_company

def execute(filters=None):
	columns, data = [], []
	return get_columns(), get_data(filters)

def get_data(filters):
	data = []
	box1_text = "Box 1: Total value of standard-rated supplies exclude GST Amount"
	data.append(box1_text)

	get_name = frappe.db.sql("""SELECT name from `tabSales Taxes and Charges Template` 
		WHERE `_user_tags` = ',Box1' """,as_dict=1)
	for gname in get_name:
		box1 = (gname.name)
		print(box1)

	get_data = frappe.db.sql(f"""SELECT posting_date, name, customer, base_net_total, 
		base_total_taxes_and_charges, taxes_and_charges, is_return, is_debit_note, _comments FROM `tabSales Invoice`
		WHERE posting_date >= '{filters.get('from_date')}'AND posting_date <= '{filters.get('to_date')}' 
		AND docstatus =1 AND is_opening = "No" and taxes_and_charges = '{box1}'
		order by taxes_and_charges, posting_date""",as_dict=1)
	for data in get_data:
		if cint(data.is_return) == 1:
			vch = "Sales Return"
		elif cint(data.is_debit_note) == 1:
			vch = "Debit Note"
		else:
			vch = "Sales Invoice"
		data.update({
			"_comments" : vch
			})
	return get_data

def get_columns():
	company = get_default_company()
	currency = get_company_currency(company)
	return [
		{
			"label":_("Posting Date"),
			"fieldname":"posting_date",
			"fieldtype":"Date",
			"width":120
		},
		{
			"label":_("Document"),
			"fieldname":"name",
			"fieldtype":"Link",
			'options': 'Sales Invoice',
			"width":200
		},
		{
			"label": _("Amount ({0})").format(currency),
			"fieldname": "base_net_total",
			"fieldtype": "Float",
			"width": 130
		},
		{
			"label":_("Tax Code"),
			"fieldname":"taxes_and_charges",
			"fieldtype":"Data",
			"width":180
		},
		{
			"label":_("Voucher Type"),
			"fieldname":"_comments",
			"fieldtype":"Data",
			"width":180
		}
	]