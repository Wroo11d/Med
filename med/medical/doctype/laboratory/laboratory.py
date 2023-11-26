# Copyright (c) 2023, worood and contributors
# For license information, please see license.txt

import frappe
#from frappe.model.document import Document
from frappe import model


class Laboratory(model.document.Document):

	def before_save(self):
		self.patient_data()


	# This function handles the proration logic for plans within a given document.
	def patient_data(self):
		patient = frappe.get_doc("Patient", self.patient_name)
		test = frappe.get_doc("Tests", self.test)
		#frappe.msgprint(f"patient{patient} and test is {test}")
		self.age = patient.age
		self.phone_number = patient.phone_number
		self.address = patient.address
		self.total_price = test.price
		self.net_total = test.price
		if self.discount == 1:
			self.net_total = test.price - self.discount_amount
"""			self.set_discount_amount_read_only(1)  # Make discount_amount field read-only
		else:
			self.set_discount_amount_read_only(0) """

"""	def set_discount_amount_read_only(self, read_only_value):
		frappe.db.set_value(
            self.doctype,
            self.name,
            'discount_amount',
            read_only_value,
            update_modified=False
        )"""



