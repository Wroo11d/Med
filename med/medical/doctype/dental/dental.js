// Copyright (c) 2023, worood and contributors
// For license information, please see license.txt

frappe.ui.form.on('Dental', {
    discount: function (frm) {
        console.log("Clicked");
        var isChecked = frm.doc.discount;
        console.log(`clicked ${isChecked}`);
        frm.set_df_property('discount_amount', 'hidden', !isChecked);
    }
});

frappe.ui.form.on('Dental', {
    refresh: function(frm) {
        // Check if discount_amount has a value
        if (frm.doc.discount_amount) {
            // If it does, set it to read-only
            frm.set_df_property('discount_amount', 'read_only', 1);
        }
    }
});

frappe.ui.form.on('Dental', {
    after_save: function(frm) {
        let procedure = frm.doc.procedure.map(row => ({
            'procedure': row.procedure,
            'price': row.price
        }));
		let doctors = frm.doc.custom_doctors.map(row => ({
            'doctor': row.doctor,
        }));
		

		let currentDate = frappe.datetime.get_today(); 
		let currentTime = frappe.datetime.now_time();
        frappe.db.insert({
            'doctype': 'Invoice',
            //'type':'Emergency',
            'patient': frm.doc.patient,   
            'date': currentDate,      
            'time': currentTime,
            'discount': frm.doc.discount,  
            'price': frm.doc.custom_total,
			'net_total': frm.doc.net_total,
			'custom_dental_procedure':procedure,
			'custom_doctors':doctors

            }).then(doc => {

            const name = doc.name;
            const host = window.location.host;
            const protocol = window.location.protocol;
            window.location.href =`${protocol}//${host}/app/invoice/${name}`; 
    });

}});
