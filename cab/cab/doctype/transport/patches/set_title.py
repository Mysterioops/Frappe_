import frappe

import frappe

def execute():
    transports = frappe.db.get_all("Transport", pluck="name")

    for t in transports:
        doc = frappe.get_doc("Transport", t)
        doc.save(ignore_permissions=True)

    frappe.db.commit()
