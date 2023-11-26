import frappe
from frappe import utils

def redirect_analyst(user=None, *args, **kwargs):
    # Check if the user has the Analyst role
    if utils.has_role(frappe.session.user, 'Analyst'):
        frappe.msgprint(frappe.session.user)
        frappe.local.response["type"] = "redirect"
        frappe.local.response["location"] = "/app/laboratory"