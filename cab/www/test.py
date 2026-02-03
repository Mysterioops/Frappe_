import frappe

def get_context(context):
    context.my_secret_text = 'This is secret'
    
    return context