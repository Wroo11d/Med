// Copyright (c) 2023, worood and contributors
// For license information, please see license.txt


frappe.ui.form.on('OCT', {
    after_save: function(frm) {
        let tests = frm.doc.test.map(row => ({
            'test': row.test,
            'eye': row.eye,
			'price':row.price
        }));
		

		let currentDate = frappe.datetime.get_today(); 
		let currentTime = frappe.datetime.now_time();
        frappe.db.insert({
            'doctype': 'Invoice',
            //'type':'Emergency',
            'patient': frm.doc.patient,   
            'date': currentDate,      
            'time': currentTime,
            'price': frm.doc.total,
			'net_total': frm.doc.total,  
			'custom_oct_tests':tests,
			//'custom_doctors':doctors,
			'doctor':frm.doc.doctor

            }).then(doc => {

            const name = doc.name;
            const host = window.location.host;
            const protocol = window.location.protocol;
            window.location.href =`${protocol}//${host}/app/invoice/${name}`; 
    });

}});