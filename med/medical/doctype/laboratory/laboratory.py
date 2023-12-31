# Copyright (c) 2023, worood and contributors
# For license information, please see license.txt

import frappe
#from frappe.model.document import Document
from frappe import model
import datetime

class Laboratory(model.document.Document):

	def before_save(self):
		self.patient_data()

	"""def before_validate(self):
		self.test_price()
		
	
	def test_price(self):
		for row in self.get("custom_tests"):
			test = frappe.get_doc("Tests", row.test)
			row.price=test.price"""

	# This function handles the proration logic for plans within a given document.
	def patient_data(self):
		#current_time = datetime.datetime.now().time()
		current_datetime = frappe.utils.now_datetime()
		current_time = current_datetime.time()
		patient = frappe.get_doc("Patients", self.patient_name)
		#test = frappe.get_doc("Tests", self.test)
		#frappe.msgprint(f"patient{patient} and test is {test}")
		self.age = patient.age
		self.phone_number = patient.phone_number
		self.address = patient.address
		self.custom_date = frappe.utils.today()
		#self.total_price = test.price
		for row in self.get("custom_tests"):
			test = frappe.get_doc("Tests", row.test)
			row.price=test.price
		total=0
		for row in self.get("custom_tests"):
			total = total + row.price
		
		self.total_price = total
		self.net_total= total
		#self.net_total = test.price
		if self.discount == 1:
			self.net_total = self.total_price - self.discount_amount
		
		#self.append("custom_tests", {"price": "sister"})
		invoice = frappe.new_doc("Invoice")
		"""invoice.patient = self.patient_name
		invoice.date = self.custom_date
		invoice.time = current_time"""
		for rowj in self.get("custom_tests"):
			invoice.append("custom_test", {"test": rowj.test,
                                      "price": rowj.price,})
		for rowi in self.get("custom_doctors"):
			invoice.append("custom_doctors", {"doctor": rowi.doctor,
                                      })
		"""invoice.discount = self.discount
		invoice.custom_totalprice = self.total_price
		invoice.net_total = self.net_total"""
		#invoice.doctor = self.doctor
		invoice.insert()
		invoice.save()
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



