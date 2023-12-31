import frappe

def execute():
	roles = ['Receptionist', 'Analyst','Emergency', 'Dentist','Myopic']
	for role in roles:
		if not frappe.db.exists('Role', role):
			role_doc = frappe.new_doc('Role')
			role_doc.role_name = role
			role_doc.flags.ignore_permissions = True
			role_doc.save()