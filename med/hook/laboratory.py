"""import frappe

def before_save(doc, method):
	patient_data(doc)


# This function handles the proration logic for plans within a given document.
def patient_data(doc):
	patient = frappe.get_doc("Patient", doc.patient_name)
	test = frappe.get_doc("Tests", doc.test)
	#frappe.msgprint(f"patient{patient} and test is {test}")
	doc.age = patient.age
	doc.phone_number = patient.phone_number
	doc.address = patient.address
	doc.total_price = test.price
	doc.net_total = test.price
	if doc.discount==1:
		doc.net_total = test.price - doc.discount_amount

#doc.save()"""
