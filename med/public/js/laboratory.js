$(document).on("startup", function () {
    // custom logic
    role = frappe.session.user
    console.log(role)
    if (role === 'Analyst'){
    frappe.set_route("laboratory");}
    if (role === 'Administrator'){
        frappe.set_route("patient");
    }
});
