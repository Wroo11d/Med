# Copyright (c) 2023, worood and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Patients(Document):
    def before_validate(self):
        self.validate_patients()

    def validate_patients(self):
        existing_doc = frappe.get_all(
        'Patients',
        filters={'full_name': self.full_name},
        fields=['name']
    )
        if existing_doc and existing_doc[0].name != self.name:
            patient = frappe.get_doc('Patients', existing_doc[0].name)
            self.age = patient.age
            self.custom_patient=self.name
            self.phone_number = patient.phone_number
            self.gender = patient.gender
            self.address = patient.address
            self.doctor = patient.doctor
            for row in patient.get("chronic_diseases"):
                self.append("chronic_diseases", {"disease": row.disease})
            #frappe.throw(f"Another record with full name '{self.full_name}' already exists.")
            
		

"""full_name=self.full_name
        #patient_name = self.custom_patient
        existing_patient = frappe.db.exists('Patient', {'full_name': self.full_name})

        if not existing_patient:
            for patient in existing_patient:
                # Access each existing patient and its details
                frappe.msgprint(f"Patient found with name: {full_name}")
                frappe.msgprint(f"Age: {patient.age}, Phone Number: {patient.phone_number}, Gender: {patient.gender}, Address: {patient.address}, Doctor: {patient.doctor}")
                """
"""else:
            # Populate the 'Patients' document with existing patient details
            patient = frappe.get_doc('Patient', patient_name)
            self.age = patient.age
            self.phone_number = patient.phone_number
            self.gender = patient.gender
            self.address = patient.address
            self.doctor = patient.doctor


"""