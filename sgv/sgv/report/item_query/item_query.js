// Copyright (c) 2022, Richard Kwa and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Item Query"] = {
	"filters": get_filters(),
	"formatter":function(value,row,column,data,default_formatter)
		{ if(data && column.fieldname=="item_code")
			value = data.item_code
			column.link_onclick = "test"
			return value;
		}
	
}
function(frm){
	$("input[data-fieldname=item_code]").mouseover(function(){
	console.log(“Hello”);

function get_filters() {
	let filters = [
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype":"Link",
			"options": "Company",
			"default":frappe.defaults.get_user_default("Company"),
			"reqd":1
		},
		{
			"fieldname":"item_code",
			"label": __("Item Code"),
			"fieldtype":"Data",
			"on_change":function(query_reports){
				var item_code=query_reports.get_values().item_code;
				frappe.msgprint("onchange")
			}
		},
		{
			"fieldname":"item_group",
			"label": __("Item Group"),
			"fieldtype":"Link",
			"options": "Item Group",
		},
		{
			"fieldname":"brand",
			"label": __("Brand"),
			"fieldtype":"Link",
			"options": "Brand",
			"default": "CRUCIAL"
		}
	]
	return filters;
}