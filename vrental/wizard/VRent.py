from odoo import api, fields, models


class VRent(models.Model):
    _name = 'vrental.vrent'

    transaction_id = fields.Many2one(
        comodel_name="vrental.transaction", string="Transaction ID")


    

    
