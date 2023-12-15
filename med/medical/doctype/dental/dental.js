// Copyright (c) 2023, worood and contributors
// For license information, please see license.txt

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
            'price': frm.doc.custom_total,
			'net_total': frm.doc.custom_total,  
			'custom_dental_procedure':procedure,
			'custom_doctors':doctors 

            }).then(doc => {

            const name = doc.name;
            const host = window.location.host;
            const protocol = window.location.protocol;
            window.location.href =`${protocol}//${host}/app/invoice/${name}`; 
    });

}});
