# Copyright (c) 2023, worood and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime

class Emergency(Document):
	# Copyright (c) 2023, worood and contributors
# For license information, please see license.txt
	def before_save(self):
		self.emergency_data()


	# This function handles the proration logic for plans within a given document.
	def emergency_data(self):
		#current_time = datetime.datetime.now().time()
		current_datetime = frappe.utils.now_datetime()
		current_time = current_datetime.time()
		self.custom_time=current_time
		for row in self.get("procedure"):
			procedure = frappe.get_doc("Emergency Procedure Prices", row.procedure)
			row.price=procedure.price
		total=0
		for row in self.get("procedure"):
			total = total + row.price
		
		self.custom_total = total
		
		#self.append("custom_tests", {"price": "sister"})
		#invoice = frappe.new_doc("Invoice")
		"""invoice.patient = self.patient_name
		invoice.date = self.custom_date
		invoice.time = current_time"""
		"""for rowj in self.get("custom_tests"):
			invoice.append("custom_test", {"test": rowj.test,
                                      "price": rowj.price,})
		for rowi in self.get("custom_doctors"):
			invoice.append("custom_doctors", {"doctor": rowi.doctor,
                                      })"""
		"""invoice.discount = self.discount
		invoice.price = self.total_price
		invoice.net_total = self.net_total"""
		#invoice.doctor = self.doctor
		#invoice.insert()
		#invoice.save()
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




