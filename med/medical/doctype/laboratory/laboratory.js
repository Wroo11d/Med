// Copyright (c) 2023, worood and contributors
// For license information, please see license.txt

frappe.ui.form.on('Laboratory', {
    discount: function (frm) {
        console.log("Clicked");
        var isChecked = frm.doc.discount;
        console.log(`clicked ${isChecked}`);
        frm.set_df_property('discount_amount', 'hidden', !isChecked);
    }
});

frappe.ui.form.on('Laboratory', {
    refresh: function(frm) {
        // Check if discount_amount has a value
        if (frm.doc.discount_amount) {
            // If it does, set it to read-only
            frm.set_df_property('discount_amount', 'read_only', 1);
        }
    }
});
frappe.ui.form.on('Laboratory', {
    after_save: function(frm) {
        let custom_tests = frm.doc.custom_tests.map(row => ({
            'test': row.test,
            'price': row.price
        }));

        let custom_doctors = frm.doc.custom_doctors.map(row => ({
            'doctor': row.doctor,
        }));

        frappe.db.insert({
            'doctype': 'Invoice',
            //'type':'Laboratory',
            'doctor': frm.doc.doctor,
            'patient': frm.doc.patient_name,   
            'date': frm.doc.custom_date,      
            'time': frm.doc.current_time,  
            'discount': frm.doc.discount,   // Assuming this is the link to the original document
            'price': frm.doc.total_price,      // Replace 'party' with the fieldname that holds the customer
            'net_total': frm.doc.net_total,
            'custom_test':custom_tests,
            'custom_doctors':custom_doctors
            }).then(doc => {

                const name = doc.name;
            const host = window.location.host;
            const protocol = window.location.protocol;
            window.location.href =`${protocol}//${host}/app/invoice/${name}`; 
    });

}});
    /*for (let row of frm.doc.custom_tests){
        frm.add_child('custom_test',{
            test:row.test,
            price: row.price})};*/
/*frappe.ui.form.on('Laboratory', {
    after_save: function(frm) {
    frappe.route_options = {
        'patient': frm.doc.patient_name,   
        'date': frm.doc.custom_date,      
        'time': frm.doc.current_time,  
        'discount': frm.doc.discount,   // Assuming this is the link to the original document
        'price': frm.doc.total_price,      // Replace 'party' with the fieldname that holds the customer
        //'net_total': frm.doc.net_total, 
    }
        
        then(doc => {
                
                const host = window.location.host;
                const protocol = window.location.protocol;
                window.location.href =`${protocol}//${host}/app/invoice/${doc.name}`;
            });
        }});*/

/*for (let row of frm.doc.custom_tests){
        doc.add_child('custom_test',{
            test:row.test,
            price: row.price}) */