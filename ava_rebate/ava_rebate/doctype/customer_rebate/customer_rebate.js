// Copyright (c) 2020, GreyCube Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer Rebate', {
	onload: function (frm) {
		frm.get_field("customer_rebate_detail").grid.cannot_add_rows = true;
		frm.set_value("from_date", frappe.datetime.month_start());
		let to_date=frappe.datetime.get_today();
		frm.set_value("to_date", to_date);
		// frm.set_query('customer', () => {
		// 	return {
		// 		filters: {
		// 			"is_parent_customer_cf":0
		// 		}
		// 	}
		// })
		frm.set_value("total_amount","");
		frm.set_value("customer","");
		frm.set_value("customer_group", 'All Customer Groups');
		frm.set_value("total_discount","");
		frm.doc.customer_rebate_detail=[];
		frm.refresh_field("customer_rebate_detail");

	},
	get_sales_invoices: function (frm) {
		return frappe.call({
			doc: frm.doc,
			method: 'fill_customer_rebate_details',
			callback: function(r) {
				if(r.message===true){
					frm.refresh();
				}
				else{
					frm.set_value("total_amount", 0);
					frm.set_value("total_discount", 0);
					frm.set_value("customer_rebate_detail", "");
					frappe.msgprint(__('No customers found for the mentioned criteria'))
				}

			}
		})
	},
	create_journal_entry: function (frm) {
		if (frm.doc.customer_rebate_detail.length == 0) {
			frappe.throw(__('Customer rebate details cann\'t be empty' ))
		}		
		if (frm.doc.default_receivable_account==undefined) {
			frappe.throw(__('Default Receivable Account cann\'t be empty' ))
		}		
		if (frm.doc.expense_account==undefined) {
			frappe.throw(__('Expense Account cann\'t be empty' ))
		}	
		return frappe.call({
			doc: frm.doc,
			method: 'process_sales_invoice_and_create_journal_entry',
			callback: function(r) {
				setTimeout(function() { 
					let si='';
					frappe.msgprint(__('Journal Entry {0} is submitted.',['<a href="#Form/Journal%20Entry/'+r.message[0]+'">' + r.message[0]+ '</a>']));
					// frappe.msgprint(__('{0} invoices are updated as paid.',[r.message[1]]));
				}, 100);
				console.log(r)
			}
		})
	},	
	customer_group: function (frm) {
		frm.set_query('customer', () => {
			return {
				filters: {
					"customer_group": frm.doc.customer_group,
					// "is_parent_customer_cf":0
				}
			}
		})
		frm.refresh_field("customer")
	}
});
frappe.ui.form.on('Customer Rebate Detail CT', {
	before_customer_rebate_detail_remove: function(frm, cdt, cdn) {
		let row = frappe.get_doc(cdt, cdn);
		let total_amount=frm.doc.total_amount-row.sales_amount
		let total_discount=frm.doc.total_discount-row.rebate_amount
		frm.set_value('total_amount', total_amount)
		frm.set_value('total_discount', total_discount)
	}
})
