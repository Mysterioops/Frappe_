# Copyright (c) 2026, adhi and contributors
# For license information, please see license.txt

import frappe
from frappe import _


import frappe
from frappe import _


def execute(filters=None):
	columns = [
		{"fieldname": "make", "label": "Make", "fieldtype": "Data"},
		{"fieldname": "total_revenue", "label": "Total Revenue", "fieldtype": "Currency", "options": "INR"},
		{"fieldname": "num_of_trips", "label": "# of Trips", "fieldtype": "Int"},
	]

	data = frappe.db.sql(
		"""
		SELECT
			t.make AS make,
			SUM(b.total_amount) AS total_revenue,
			COUNT(*) AS num_of_trips
		FROM `tabBooking` b
		JOIN `tabTransport` t ON t.name = b.transport
		WHERE b.docstatus = 1
		GROUP BY t.make
		""",
		as_dict=True
	)
	chart = {
		"data": {
			"labels": [x.make for x in data],
			"datasets": [
				{
					"name": "Revenues",
					"values": [x.total_revenue for x in data]
				}
			]
		},
		"type": "pie",
		"height": 300
	}	

	return columns, data,None, chart, None


'''

'''