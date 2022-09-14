from odoo import api, fields, models


class ResPartners(models.Model):
    _name = 'res.partners'
    _description = 'Partners'
    _rec_name = 'display_name'


    display_name = fields.Char(string='Name', required=True)
    email = fields.Char('Email', required=True)
    mobile = fields.Char('Mobile', required=True)