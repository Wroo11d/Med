
$(document).on("startup", function () {
    // custom logic
    email = frappe.session.user
    var currentUserRoles = frappe.user_roles; //get user roles
    console.log(currentUserRoles[0])  
    role = currentUserRoles[0]
    if (role === 'Analyst' && email !='Administrator'){
        console.log(currentUserRoles)  
        console.log(currentUserRoles[0])  
        frappe.set_route("laboratory");
    }
    else if (role === "Receptionist" && email !='Administrator'){
        console.log(currentUserRoles)  
        console.log(currentUserRoles[0])  
        frappe.set_route("patients");
    }
    else if (role === "System Manager" && email !='Administrator'){
        console.log(currentUserRoles)  
        console.log(currentUserRoles[0])  
        frappe.set_route("dashboards");
    }
    else if (role === "Dentist" && email !='Administrator'){
        console.log(currentUserRoles)  
        console.log(currentUserRoles[0])  
        frappe.set_route("dental");
    }
    else if (role === "Emergency" && email !='Administrator'){
        console.log(currentUserRoles)  
        console.log(currentUserRoles[0])  
        frappe.set_route("emergency");
    }
    else if (role === "Myopic" && email !='Administrator'){
        console.log(currentUserRoles)  
        console.log(currentUserRoles[0])  
        frappe.set_route("oct");
    }

    else if (email === 'Administrator'){
        frappe.set_route("dashboards");
    }
    else{
        'User Not Found'
    }

});