// Copyright (c) 2022, Richard Kwa and contributors
// For license information, please see license.txt

frappe.ui.form.on('SGP Item', {
	
	search_item: function(frm){
		frappe.msgprint("dialog")
		var d = new frappe.ui.dialog({
			size: "large",
			title: "Search details",
			fields: [
				{
					label: 'Item Code',
					fieldname: 'item_code',
					fieldtype: 'Data',
					reqd: 1,
				},
				{
					label: 'Item Code',
					fieldname: 'item_group',
					fieldtype: 'Data',
				},
				{
					label: 'Brand',
					fieldname: 'brand',
					fieldtype: 'Data',
					Option: 'Lenovo'
				},
			]
		});	

		dialog.set_primary_action(__("Submit"), function() {
				var data = d.get_values();
				show_alert(d.et_values());
				d.hide();
			});
		d.show();
	}
});
