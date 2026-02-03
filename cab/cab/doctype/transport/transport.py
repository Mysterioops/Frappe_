# Copyright (c) 2026, adhi and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Transport(Document):
    def before_save(self):
        self.title = f"{self.make} {self.model}, {self.year}"
