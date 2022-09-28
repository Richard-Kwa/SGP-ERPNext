# Copyright (c) 2022, Richard Kwa and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	return get_columns(), get_data(filters)

def get_data(filters):
	conditions = ""

	# if filters.get('item_code'):
	#	conditions += " item_code LIKE '{filters.get('item_code')}'"
	# if filters.get('item_name'):
	#	conditions += " item_name LIKE '{filters.get('item_name')}'"
	#	return conditions
	get_data = frappe.db.sql(f"""Select item_code, item_name, item_group, brand from tabItem 
		WHERE item_code LIKE '{filters.get('item_code')}' OR item_group ='{filters.get('item_group')}' 
		OR brand='{filters.get('brand')}'""",as_dict=1)
	# get_data = frappe.db.sql(f"""Select item_code, item_name, item_group, brand from tabItem;""",filters,as_dict=True)
	return get_data

def get_columns():
	return [
		{"label":_("Item"),"fieldname":"item_code","fieldtype":"Data","width":150},
		{"label":_("Item Name"),"fieldname":"item_name","fieldtype":"Data","width":400},
		{"label":_("Item Group"),"fieldname":"item_group","fieldtype":"Data","width":150},
		{"label":_("Brand"),"fieldname":"brand","fieldtype":"Data","width":120}
	]