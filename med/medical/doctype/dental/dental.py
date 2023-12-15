# Copyright (c) 2023, worood and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Dental(Document):
	def before_save(self):
		self.dental_data()


	# This function handles the proration logic for plans within a given document.
	def dental_data(self):
		#current_time = datetime.datetime.now().time()
		current_datetime = frappe.utils.now_datetime()
		current_time = current_datetime.time()
		for row in self.get("procedure"):
			procedure = frappe.get_doc("Dental Procedure Prices", row.procedure)
			row.price=procedure.price
		total=0
		for row in self.get("procedure"):
			total = total + row.price
		
		self.custom_total = total
