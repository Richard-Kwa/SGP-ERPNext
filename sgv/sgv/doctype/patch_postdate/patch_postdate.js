// Copyright (c) 2022, Richard Kwa and contributors
// For license information, please see license.txt

frappe.ui.form.on('patch_postdate', 
{
	refresh: function(frm){
		if(frm.is_new()) {
			frm.add_custom_button("Sales"), function()
			{
				frappe.call({
					method: 'sgv.sgv.doctype.patch_postdate.patch.postdate.update_sales_date',
					callback: function() {
						frm.refresh()
					}
				})
			}, "Button Group"}
			frm.add_custom_button("Purchase"), function()
			{
				frappe.call({
					method: 'gv.sgv.doctype.patch_postdate.patch.postdate.update.purchase_date',
					callback: function() {
						frm.refresh()
					}
				})
			}, "Button Group"}
});

frappe.ui.form.on('patch_postdate', 
{
	"to_date": function(frm) {
	if (frm.doc.from_date >= frm.doc.to_date)
		{
			frappe.msgprint("To Date must be later than From Date - JS");
			frappe.valiate = false;
		}
	}
});