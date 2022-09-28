// Copyright (c) 2022, Richard Kwa and contributors
// For license information, please see license.txt

frappe.ui.form.on('SGP GST Report', {
	"to_date": function(frm) {
		if (frm.doc.from_date >= frm.doc.to_date)
			{
				frappe.msgprint("To Date must be later than From Date");
				frappe.validate = false;
			}
		}
});

frappe.ui.form.on('SGP GST Report',	{
	generate_detail: function(frm) {
		frm.call({
			method:'list_all_gst_details',
			doc: frm.doc,
			args: {
				doctype:"SGP GST Detail"
			},
			callback: function(r) {
				frappe.msgprint("Successfully Updated")
				frm.refresh_field('sgp_gst_detail')
			}
		})
	}
});


