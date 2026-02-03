# Copyright (c) 2026, adhi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Booking(Document):
    def validate(self):
        if self.rate is None:
            frappe.throw("Please provide a rate")

        total_distance = 0
        for item in self.items:
            total_distance += item.distance or 0

        self.total_amount = total_distance * self.rate
