
$(document).on("startup", function () {
    // custom logic
    role = frappe.session.user
    var currentUserRoles = frappe.user_roles;
    console.log(currentUserRoles[0])
    analy = currentUserRoles[0]
    if (analy === 'Analyst'){
        log("Match")
    }
    else{
        'No Match'
    }
   /* if (role === 'Analyst'){
    frappe.set_route("laboratory");}
    if (role === 'Administrator'){
        frappe.set_route("patient");
    }*/
});


