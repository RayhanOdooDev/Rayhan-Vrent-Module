from odoo import api, fields, models


class Customer(models.Model):
    _name = 'vrental.customer'
    _description = 'New Description'

    name = fields.Char(string='Name')
    
    is_konsumen = fields.Boolean(string="Is Konsumen")
    id_member = fields.Char(
        string='Id',
        required=False)
    address = fields.Char(string='Address')
    phone_number = fields.Char(string='Phone Number')
    avatar = fields.Image(max_width=189, max_height=284)
g