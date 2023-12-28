
/***$(document).on("startup", function () {
    // custom logic
    email = frappe.session.user
    var currentUserRoles = frappe.user_roles; //get user roles
    console.log(currentUserRoles[0])  
    role = currentUserRoles[0]
    if (role === "Myopic" && role ==='Emergency' && role ==='Dentist' && role ==='System Manager' && role ==='Receptionist' && email !='Administrator'){
        console.log(currentUserRoles)  
        console.log(currentUserRoles[0])  
        frappe.set_route("dashboards");
    }
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

});***/


$(document).on("startup", function () {
    // custom logic
    email = frappe.session.user
    var currentUserRoles = frappe.user_roles; //get user roles 
    role = currentUserRoles[0]
    if (currentUserRoles.includes("System Manager")){
        console.log(currentUserRoles)  
        console.log(currentUserRoles[0])  
        frappe.set_route("dashboards");
    }
    else if (currentUserRoles.includes("Analyst") && !currentUserRoles.includes("System Manager")){
        console.log(currentUserRoles)  
        console.log(currentUserRoles[0])  
        frappe.set_route("laboratory");
    }
    else if (currentUserRoles.includes("Receptionist") && !currentUserRoles.includes("System Manager")){
        console.log(currentUserRoles)  
        console.log(currentUserRoles[0])  
        frappe.set_route("patients");
    }
    else if (currentUserRoles.includes("Dentist") && !currentUserRoles.includes("System Manager")){
        console.log(currentUserRoles)  
        console.log(currentUserRoles[0])  
        frappe.set_route("dental");
    }
    else if (rcurrentUserRoles.includes("Emergency") && !currentUserRoles.includes("System Manager")){
        console.log(currentUserRoles)  
        console.log(currentUserRoles[0])  
        frappe.set_route("emergency");
    }
    else if (currentUserRoles.includes("Myopic") && !currentUserRoles.includes("System Manager")){
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