// Copyright (c) 2026, adhi and contributors
// For license information, please see license.txt

frappe.ui.form.on("Booking", {
	refresh(frm) {
        console.log('hello');   
	},

    rate(frm) {
        frm.trigger('setTotalAmount');
    },

    setTotalAmount(frm) {
        let totalDistance = 0;
        for(let item of frm.doc.items) {
            totalDistance += item.distance;
        }

        const amount = frm.doc.rate * totalDistance;
        frm.set_value('total_amount', amount);
        
    }
});

frappe.ui.form.on('Ride Booking Item', {
	refresh(frm) {
	},

    distance(frm, cdt, cdn) { 
        frm.trigger('setTotalAmount');
    },

    items_add(frm, cdt, cdn) {
        const lastItem = frm.doc.items[frm.doc.items.length - 2];
        let origin = lastItem ? lastItem.destination : null;
        frappe.model.set_value(cdt, cdn, 'source', origin);
    },

    items_remove(frm, cdt, cdn) {
        frm.trigger("setTotalAmount");
    }
});