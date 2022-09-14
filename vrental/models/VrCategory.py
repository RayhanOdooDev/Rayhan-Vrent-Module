from odoo import api, fields, models


class VRCategory(models.Model):
    _name = 'vrental.vrcategory'
    _description = 'New Description'

    name = fields.Selection([
        ('standalone', 'Standalone'), 
        ('tethered', 'Tethered'), 
        ('psvr', 'Psvr'),
        ('acc', 'Acc')
    ], string='VR Category')
    
    code_category = fields.Char(string='Code Category')

    @api.onchange('name')
    def _compute_code_category(self):
        if (self.name == 'standalone'):
            self.code_category = 'vr01'
        elif (self.name == 'tethered'):
            self.code_category = 'vr02'
        elif (self.name == 'psvr'):
            self.code_category = 'vr03'
        elif (self.name == 'acc'):
            self.code_category = 'acc'
    
    shelf = fields.Char(string='Shelf')
    vr_ids = fields.One2many(comodel_name='vrental.vrlist', 
                                inverse_name='vrcategory_id', 
                                string='VR List')
    
    total_item = fields.Char(compute='_compute_total_item', string='Total Item')
    
    @api.depends('vr_ids')
    def _compute_total_item(self):
         for rec in self:
            a = self.env['vrental.vrlist'].search([('vrcategory_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.total_item = b

            
        