# Copyright (c) 2022, Richard Kwa and contributors
# For license information, please see license.txt

import frappe

from frappe import _
from frappe.utils import cint, flt, getdate
from erpnext import get_company_currency, get_default_company

def execute(filters=None):
	return get_columns(), get_data(filters)

def get_data(filters):
	get_data = frappe.db.sql(f"""SELECT posting_date, name, party, party_type, account, 
		voucher_type, debit, credit FROM `tabGL Entry`
		WHERE posting_date >= '{filters.get('from_date')}'AND posting_date <= '{filters.get('to_date')}' 
		AND docstatus=1 AND is_opening = "No" AND account = '{filters.get('account')}'
		AND voucher_type IN ('Journal Entry', 'Cash Entry', 'Bank Entry')
		order by posting_date""",as_dict=1)
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
			"fieldtype":"Data",
			"width":200
		},
		{
			"label":_("Account"),
			"fieldname":"account",
			"fieldtype":"Data",
			"width":180
		},
		{
			"label":_("Party"),
			"fieldname":"party",
			"fieldtype":"Data",
			"width":200
		},
		{
			"label":_("Party Type"),
			"fieldname":"party_type",
			"fieldtype":"Data",
			"width":200
		},
		{
			"label": _("Debit Amount ({0})").format(currency),
			"fieldname": "debit",
			"fieldtype": "Float",
			"width": 130
		},
		{
			"label": _("Credit Amount ({0})").format(currency),
			"fieldname": "Credit",
			"fieldtype": "Float",
			"width": 130
		},
		{
			"label":_("Voucher Type"),
			"fieldname":"_comments",
			"fieldtype":"Data",
			"width":180
		}
	]
