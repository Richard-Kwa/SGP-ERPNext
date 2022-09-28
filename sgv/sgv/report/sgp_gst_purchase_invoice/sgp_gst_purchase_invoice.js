// Copyright (c) 2022, Richard Kwa and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["SGP GST Purchase Invoice"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
			"width": "80"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today()
		},
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("Company")
		},
		{
			"fieldname":"taxes_and_charges",
			"label": __("Purchase Tax Code"),
			"fieldtype": "Link",
			"options": "Purchase Taxes and Charges Template"
		},
		{
			"fieldname": "no_tax_code",
			"label": __("No Tax Entries"),
			"fieldtype": "Check"
		},
	],
	"formatter": function (value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);

		if (column.fieldname == "included_in_print_rate" && data && data.included_in_print_rate == 0) 
		{
			value = "<span style='color:red'>" + value + "</span>"
		}
		return value;
		}
};