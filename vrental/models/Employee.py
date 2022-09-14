from odoo import api, fields, models


class Employee(models.Model):
    _name = 'vrental.employee'
    _description = 'New Description'

    name = fields.Char(string='Name')
    address = fields.Char(string='Address')
    phone_number = fields.Char(string='Phone Number')
    job = fields.Selection([
        ('admin', 'Admin'), 
        ('clerk', 'Clerk'), 
        ('cleaning', 'Cleaning')
    ], string='Job')





    

    

    
    
