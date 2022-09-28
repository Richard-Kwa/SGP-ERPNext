import frappe

from frappe import _
from frappe.utils import cint, flt, getdate
from erpnext import get_company_currency, get_default_company

def execute(filters=None):
	return get_columns(), get_data(filters)

def get_data(filters):
	get_data = frappe.db.sql(f"""SELECT creation, posting_date, parent, parenttype, charge_type, account_head,
		base_total, base_tax_amount, included_in_print_rate FROM `tabSales Taxes and Charges`
		WHERE (posting_date >= '{filters.get('from_date')}' AND posting_date <= '{filters.get('to_date')}')
		AND docstatus = 1 AND parenttype = 'Sales Invoice' AND account_head = '{filters.get('account')}'
		order by parent, creation""",as_dict=1)
	for data in get_data:
		tot = data.base_total - data.base_tax_amount
		data.update({
		"total" : tot
		})
	return get_data

def get_columns():
	company = get_default_company()
	currency = get_company_currency(company)
	return [
		{
			"label":_("Date"),
			"fieldname":"creation",
			"fieldtype":"Date",
			"width":110
		},
		{
			"label":_("Posting Date"),
			"fieldname":"posting_date",
			"fieldtype":"Date",
			"width":110
		},
		{
			"label":_("Document"),
			"fieldname":"parent",
			"fieldtype":"Link",
			'options': 'Sales Invoice',
			"width":150
		},
		{
			"label":_("Parent Type"),
			"fieldname":"parenttype",
			"fieldtype":"Data",
			"width":150
		},
		{
			"label": _("Amount ({0})").format(currency),
			"fieldname": "total",
			"fieldtype": "Float",
			"width": 130
		},
		{
			"label": _("GST Amount ({0})").format(currency),
			"fieldname": "base_tax_amount",
			"fieldtype": "Float",
			"width": 130
		},
				{
			"label": _("Total Amount ({0})").format(currency),
			"fieldname": "base_total",
			"fieldtype": "Float",
			"width": 130
		},
		{
			"label":_("Charge Type"),
			"fieldname":"charge_type",
			"fieldtype":"Data",
			"width":180
		},
		{
			"label":_("Account"),
			"fieldname":"account_head",
			"fieldtype":"Data",
			"width":180
		},
					{
			"label":_("Remarks"),
			"fieldname":"included_in_print_rate",
			"fieldtype":"Data",
			"width":80
		}
	]
