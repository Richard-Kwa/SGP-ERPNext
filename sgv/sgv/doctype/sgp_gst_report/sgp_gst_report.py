# Copyright (c) 2022, Richard Kwa and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint
from frappe.utils import cint, cstr, flt, fmt_money, formatdate, nowdate
from frappe.model.document import Document

class SGPGSTReport(Document):
	def validate(self):
		if self.from_date >= self.to_date:
			frappe.throw("To Date must be later than From Date")

	@frappe.whitelist()
	def list_all_gst_details(self,doctype):

		box1_acct = frappe.db.sql(f"""SELECT name from `tabAccount` where gst_box = 'Box1' and
			disabled=0 and account_type = 'Tax'""", as_dict=1)

		data = frappe.db.sql(f"""SELECT posting_date, parent, parenttype, charge_type, description, rate, base_total, base_tax_amount, csname 
			FROM `tabSales Taxes and Charges`
			WHERE (posting_date >= %(from)s AND posting_date <= %(to)s)
			AND docstatus = 1 AND parenttype = 'Sales Invoice' AND account_head = %(b1acct)s order by parent""",
			{"from": self.from_date, "to": self.to_date, "b1acct": box1_acct[0].name},as_dict=1)
		
		self.append("sgp_gst_details",
			{
				"box":"Title",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Standard-Rated Supplies",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt":"",
				"gst_amt":""
			})

		box1tot = 0
		box1gst = 0
		for d in data:
			fdate = formatdate(d.posting_date, "YYYY-MM-dd")
			tot = d.base_total - d.base_tax_amount
			box1tot = box1tot + tot
			box1gst = box1gst + d.base_tax_amount
			self.append("sgp_gst_details",
			{
				"box":"Box1",
				"posting_date":fdate,
				"transaction_type":d.parenttype,
				"document_no":d.parent,
				"cs_name":d.csname,
				"gst_code":d.description,
				"gst_rate":d.rate,
				"taxable_amt":tot,
				"gst_amt":d.base_tax_amount
			})

		self.append("sgp_gst_details",
			{
				"box":"Total",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Total Standard-Rated Supplies",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt":box1tot,
				"gst_amt":box1gst
			})

		#Box2
		box2_acct = frappe.db.sql(f"""SELECT name from `tabAccount` where gst_box = 'Box2' and
			disabled=0 and account_type = 'Tax'""", as_dict=1)

		data = frappe.db.sql(f"""SELECT posting_date, parent, parenttype, charge_type, description, rate, base_total, base_tax_amount, csname
			FROM `tabSales Taxes and Charges`
			WHERE (posting_date >= %(from)s AND posting_date <= %(to)s)
			AND docstatus = 1 AND parenttype = 'Sales Invoice' AND account_head = %(b2acct)s order by parent""",
			{"from": self.from_date, "to": self.to_date, "b2acct": box2_acct[0].name},as_dict=1)
		
		self.append("sgp_gst_details",
			{
				"box":"Title",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Zero Rated Supplies",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt":"",
				"gst_amt":""
			})

		box2tot = 0
		box2gst = 0
		for d in data:
			fdate = formatdate(d.posting_date, "YYYY-MM-dd")
			tot = d.base_total - d.base_tax_amount
			box2tot = box2tot + tot
			box2gst = box2gst + d.base_tax_amount
			self.append("sgp_gst_details",
			{
				"box":"Box2",
				"posting_date":fdate,
				"transaction_type":d.parenttype,
				"document_no":d.parent,
				"cs_name":d.csname,
				"gst_code":d.description,
				"gst_rate":d.rate,
				"taxable_amt":tot,
				"gst_amt":d.base_tax_amount
			})

		self.append("sgp_gst_details",
			{
				"box":"Total",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Total Zero Rated Supplies",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt":box2tot,
				"gst_amt":box2gst
			})

		#Box3
		box3_acct = frappe.db.sql(f"""SELECT name from `tabAccount` where gst_box = 'Box3' and
			disabled=0 and account_type = 'Tax'""", as_dict=1)

		data = frappe.db.sql(f"""SELECT posting_date, parent, parenttype, charge_type, description, rate, base_total, base_tax_amount, csname
			FROM `tabSales Taxes and Charges`
			WHERE (posting_date >= %(from)s AND posting_date <= %(to)s)
			AND docstatus = 1 AND parenttype = 'Sales Invoice' AND account_head = %(b3acct)s order by parent""",
			{"from": self.from_date, "to": self.to_date, "b3acct": box3_acct[0].name},as_dict=1)
		
		self.append("sgp_gst_details",
			{
				"box":"Title",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Exempted Supplies",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt":"",
				"gst_amt":""
			})

		box3tot = 0
		box3gst = 0
		for d in data:
			fdate = formatdate(d.posting_date, "YYYY-MM-dd")
			tot = d.base_total - d.base_tax_amount
			box3tot = box3tot + tot
			box3gst = box3gst + d.base_tax_amount
			self.append("sgp_gst_details",
			{
				"box":"Box3",
				"posting_date":fdate,
				"transaction_type":d.parenttype,
				"document_no":d.parent,
				"cs_name":d.csname,
				"gst_code":d.description,
				"gst_rate":d.rate,
				"taxable_amt":tot,
				"gst_amt":d.base_tax_amount
			})

		self.append("sgp_gst_details",
			{
				"box":"Total",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Total Exempted Supplies",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt":box3tot,
				"gst_amt":box3gst
			})

		#box 5
		box5_acct = frappe.db.sql(f"""SELECT name from `tabAccount` where gst_box = 'Box5' and
			disabled=0 and account_type = 'Tax'""", as_dict=1)

		data = frappe.db.sql(f"""SELECT posting_date, parent, parenttype, charge_type, description, rate, base_total, base_tax_amount, csname 
			FROM `tabPurchase Taxes and Charges`
			WHERE (posting_date >= %(from)s AND posting_date <= %(to)s)
			AND docstatus = 1 AND parenttype = 'Purchase Invoice' AND account_head = %(b5acct)s order by parent""",
			{"from": self.from_date, "to": self.to_date, "b5acct": box5_acct[0].name},as_dict=1)

		self.append("sgp_gst_details",
			{
				"box":"Title",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Taxable Purchases",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt":"",
				"gst_amt":""
			})

		box5tot = 0
		box5gst = 0
		for d in data:
			fdate = formatdate(d.posting_date, "YYYY-MM-dd")
			tot = d.base_total - d.base_tax_amount
			box5tot = box5tot + tot
			box5gst = box5gst + d.base_tax_amount

			self.append("sgp_gst_details",
			{
				"box":"Box5",
				"posting_date":fdate,
				"transaction_type":d.parenttype,
				"document_no":d.parent,
				"cs_name":d.csname,
				"gst_code":d.description,
				"gst_rate":d.rate,
				"taxable_amt":tot,
				"gst_amt":d.base_tax_amount
			})

		self.append("sgp_gst_details",
			{
				"box":"Total",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Total Taxable Purchases",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt":box5tot,
				"gst_amt":box5gst
			})

	#Form 5 - Box1
		self.append("sgp_gst_details",
			{
				"box":"F5",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Box1: Total value of Standard-Rated Supplies",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt":box1tot,
				"gst_amt":0
			})

	#Form 5 - Box2
		self.append("sgp_gst_details",
			{
				"box":"F5",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Box2: Total value of Zero-Rated Supplies",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt":box2tot,
				"gst_amt":0
			})
	
	#Form 5 - Box3
		self.append("sgp_gst_details",
			{
				"box":"F5",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Box3: Total value of Exempt Supplies",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt":box3tot,
				"gst_amt":0
			})

	#Form 5 - Box4 - Box1 + Box2 + Box3
		box4tot = 0
		box4tot = box1tot + box2tot + box3tot
		self.append("sgp_gst_details",
			{
				"box":"F5",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Box4: Total value of (1) + (2) + (3)",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt":box4tot,
				"gst_amt":0
			})

	#Form 5 - Box5
		self.append("sgp_gst_details",
			{
				"box":"F5",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Box5: Total value of Taxable Purchases",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt":box5tot,
				"gst_amt":0
			})

		#Form 5 - Box6
		self.append("sgp_gst_details",
			{
				"box":"F5",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Box6: Output Tax Due",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt":box1gst,
				"gst_amt":0
			})

		#Form 5 - Box7
		self.append("sgp_gst_details",
			{
				"box":"F5",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Box7: Input Tax and refunds claims",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt":box5gst,
				"gst_amt":0
			})

		#Form 5 - Box8 - Box6 - Box7
		box8tot = 0
		box8tot = box1gst - box5gst
		self.append("sgp_gst_details",
			{
				"box":"F5",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Box 8: Net GST to be paid to IRAS = (6) - (7)",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt":box8tot,
				"gst_amt":0
			})
		
		#revenue 
		dr_amt = 0
		cr_amt = 0
		tot_dr_amt = 0
		tot_cr_amt = 0
		adata = frappe.db.sql(f"""SELECT name from `tabAccount` where is_group = 0 
		    and disabled = 0 and account_type = 'Income Account'""", as_dict=1)

		for d in adata:
			jtitle = d.name
			jdata = frappe.db.sql("""SELECT debit, credit FROM `tabGL Entry` WHERE (posting_date >= %(from)s AND posting_date <= %(to)s)
				AND docstatus = 1 AND account = %(acct)s""",	{"from": self.from_date, "to": self.to_date, "acct": jtitle},as_dict=1)
			for j in jdata:
				dr_amt = j.debit
				cr_amt = j.credit
				tot_dr_amt = tot_dr_amt + dr_amt
				tot_cr_amt = tot_cr_amt + cr_amt

		rev_amt = tot_cr_amt - tot_dr_amt
		self.append("sgp_gst_details",
			{
				"box":"F5",
				"posting_date": "",
				"transaction_type": "",
				"document_no": "Box 13:Revenue",
				"cs_name":"",
				"gst_code":"",
				"gst_rate":"",
				"taxable_amt": rev_amt,
				"gst_amt":0
			})

