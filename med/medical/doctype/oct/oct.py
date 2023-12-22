# Copyright (c) 2023, worood and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class OCT(Document):
	def before_save(self):
		self.oct_data()

		
	def oct_data(self):
		patient = frappe.get_doc("Patients", self.patient)
		self.age = patient.age
		#total = self.total
		total = 0
		#selected_tests = doc.get("oct_tests")  
		for test_entry in self.get("test"):
			test_type = test_entry.get("test")
			eye_condition = test_entry.get("eye")
			patient_type = self.private # Fetch patient type from main OCT document


        # Define prices based on conditions for each test
			if patient_type == 1:
				if test_type == "Macular":
					if eye_condition == "العين اليمنى" or eye_condition == "العين اليسرى":
						test_entry.price = 20000  # Sample price
						#total = total+1000
					elif eye_condition == "كلتاهما":
						test_entry.price = 35000  # Sample price
					else:
						test_entry.price = 0  # Sample price
				# Add more conditions and prices for different scenarios for Macular test
				elif test_type == "Optic Disk":
					if eye_condition == "العين اليمنى" or eye_condition == "العين اليسرى":
						test_entry.price = 20000  # Sample price
						#total = total+1000
					elif eye_condition == "كلتاهما":
						test_entry.price = 35000  # Sample price
					else:
						test_entry.price = 0  # Sample price
			
				elif test_type == "Pachymetry":
					if eye_condition == "العين اليمنى" or eye_condition == "العين اليسرى":
						test_entry.price = 10000  # Sample price
					elif eye_condition == "كلتاهما":
						test_entry.price = 10000  # Sample price
					else:
						test_entry.price = 0  # Sample price

				elif test_type == "AC Angel":
					if eye_condition == "العين اليمنى" or eye_condition == "العين اليسرى":
						test_entry.price = 15000  # Sample price
						#total = total+1000
					elif eye_condition == "كلتاهما":
						test_entry.price = 20000  # Sample price
					else:
						test_entry.price = 0  # Sample price
				# Add more conditions and prices for different scenarios for Macular test
				elif test_type == "Fundus Camera":
					if eye_condition == "العين اليمنى" or eye_condition == "العين اليسرى":
						test_entry.price = 10000 # Sample price
						#total = total+1000
					elif eye_condition == "كلتاهما":
						test_entry.price = 15000  # Sample price
					else:
						test_entry.price = 0  # Sample price
				elif test_type == "IOP":
					if eye_condition == "العين اليمنى" or eye_condition == "العين اليسرى":
						test_entry.price = 10000 # Sample price
						#total = total+1000
					elif eye_condition == "كلتاهما":
						test_entry.price = 10000  # Sample price
					else:
						test_entry.price = 0  # Sample price
				else:
					pass
			else:
				if test_type == "Macular":
					if eye_condition == "العين اليمنى" or eye_condition == "العين اليسرى":
						test_entry.price = 10000 # Sample price
						#total = total+1000
					elif eye_condition == "كلتاهما":
						test_entry.price = 15000  # Sample price
					else:
						test_entry.price = 0  # Sample price
				# Add more conditions and prices for different scenarios for Macular test
				elif test_type == "Optic Disk":
					if eye_condition == "العين اليمنى" or eye_condition == "العين اليسرى":
						test_entry.price = 10000  # Sample price
						#total = total+1000
					elif eye_condition == "كلتاهما":
						test_entry.price = 15000  # Sample price
					else:
						test_entry.price = 0  # Sample price
			
				elif test_type == "Pachymetry":
					if eye_condition == "العين اليمنى" or eye_condition == "العين اليسرى":
						test_entry.price = 5000  # Sample price
					elif eye_condition == "كلتاهما":
						test_entry.price = 5000  # Sample price
					else:
						test_entry.price = 0  # Sample price

				elif test_type == "AC Angel":
					if eye_condition == "العين اليمنى" or eye_condition == "العين اليسرى":
						test_entry.price = 10000  # Sample price
						#total = total+1000
					elif eye_condition == "كلتاهما":
						test_entry.price = 15000  # Sample price
					else:
						test_entry.price = 0  # Sample price
				# Add more conditions and prices for different scenarios for Macular test
				elif test_type == "Fundus Camera":
					if eye_condition == "العين اليمنى" or eye_condition == "العين اليسرى":
						test_entry.price = 5000  # Sample price
						#total = total+1000
					elif eye_condition == "كلتاهما":
						test_entry.price = 5000  # Sample price
					else:
						test_entry.price = 0  # Sample price
				elif test_type == "IOP":
					if eye_condition == "العين اليمنى" or eye_condition == "العين اليسرى":
						test_entry.price = 5000 # Sample price
						#total = total+1000
					elif eye_condition == "كلتاهما":
						test_entry.price = 5000  # Sample price
					else:
						test_entry.price = 0  # Sample price
				else:
					pass

		for row in self.get("test"):
			self.total = self.total+row.price
		#frappe.msgprint(total)

			

        	# Add more conditions for other test types

    	# Save the calculated prices to the child tablee
		#self.save()
