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
