from odoo import api, fields, models


class VirtualR(models.Model):
    _name = 'vrental.vrlist'
    _description = 'New Description'

    name = fields.Char(string='VR Name')
    price = fields.Integer(string='Rent Price',required=True)
    vrcategory_id = fields.Many2one(comodel_name='vrental.vrcategory', 
                                        string='VR Cateogry',
                                        ondelete='cascade')
    stock = fields.Integer(string='Stock')
    image = fields.Image(string="image")
    
    
