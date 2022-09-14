from odoo import api, fields, models
from odoo.exceptions import *
from datetime import *

class Transaction(models.Model):
    _name = 'vrental.transaction'
    _description = 'Transaction Model'

    name = fields.Char(string='Tx No.')
    customer_name = fields.Many2one(comodel_name="vrental.customer", string="Customer Name")
    id_member = fields.Char(compute='_compute_id_member', string='Member ID', required=False)
    start_date = fields.Date(string='Rent Date', default=fields.Datetime.now, required=True)
    end_date = fields.Date(string='End Date', default=fields.Datetime.now, required=True)
    rent_day = fields.Integer(compute='_compute_totalday', string='Rent Day')
    total_cost = fields.Integer(compute='_compute_totalcost', string='Total Cost', readonly=True)
    transactiondetail_ids = fields.One2many(comodel_name =
            "vrental.transactiondetail",
            inverse_name = 'transaction_id',
            string = 'Transaction Detail'
    ) 

    state = fields.Selection(
        string='Status',
        selection=[('draft', 'Draft'), 
                    ('confirm', 'Confirm'),
                    ('rented', 'Rented'),
                    ('returned', 'Returned'),
                    ('done', 'Done'),
                    ('cancelled', 'Cancelled')], 
        required=True, 
        readonly=True,
        default='draft'
    )
    
    @api.depends('customer_name')
    def _compute_id_member(self):
        for rec in self:
            rec.id_member = rec.customer_name.id_member

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_rented(self):
        self.write({'state': 'rented'})

    def action_returned(self):
        self.write({'state': 'returned'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})

    #RENT DAY FUNCTION
    @api.depends('start_date', 'end_date')
    def _compute_totalday(self):
        for rec in self:
            start_date = fields.Datetime.to_datetime(rec.start_date).date()
            end_date = fields.Datetime.to_datetime(rec.end_date).date()
            a = str(int((end_date - start_date).days))
            rec.rent_day = a

    @api.depends('transactiondetail_ids')
    def _compute_totalcost(self):
        for rec in self:
            a = sum(self.env['vrental.transactiondetail'].search([('transaction_id','=',rec.id)]).mapped('subtotal'))
            zzz = a * rec.rent_day
            rec.total_cost = zzz


    @api.ondelete(at_uninstall=False)
    def __ondelete_transaction(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise ValidationError("You can remove this just in DRAFT state")
        else:
            if self.transactiondetail_ids:
                a=[]
                for rec in self:
                    a = self.env['vrental.transactiondetail'].search([('transaction_id','=',rec.id)])
                    print(a)

                for ob in a:
                    print(ob.vr_id.name + ' ' + str(ob.qty))
                    ob.vr_id.stock += ob.qty

    def write(self,vals):
        for rec in self:
            a = self.env['vrental.transactiondetail'].search([('transaction_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.vr_id.name)+' '+str(data.qty)+' '+str(data.vr_id.stock))
                data.vr_id.stock += data.qty
        record = super(Transaction,self).write(vals)
        for rec in self:
            b = self.env['vrental.transactiondetail'].search([('transaction_id','=',rec.id)])
            print(b)
            for newdata in b:
                if newdata in a:
                    print(str(newdata.vr_id.name)+' '+str(newdata.qty)+' '+str(newdata.vr_id.stock))
                    newdata.vr_id.stock -= data.qty
                else:
                    pass
        return record


    _sql_constraints = [
        ('note_unique','unique (name)','Transaction Note Must be Unique!!!')
    ]

class TransactionDetail(models.Model):
    _name = 'vrental.transactiondetail'
    _description = 'Transaction Detail'
    

    name = fields.Char(string='Name')
    transaction_id = fields.Many2one(comodel_name='vrental.transaction', string='Transaction Detail')
    vr_id = fields.Many2one(comodel_name='vrental.vrlist', string='List VR')
    each_price = fields.Integer(string='Each Price')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal',string='Subtotal')

    @api.depends('each_price','qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.each_price
    
    @api.onchange('vr_id')
    def _onchange_vr_id(self):
        if (self.vr_id.price):
            self.each_price = self.vr_id.price
    
    @api.model
    def create(self,vals):
        record = super(TransactionDetail,self).create(vals)
        if record.qty:
            self.env['vrental.vrlist'].search([('id','=',record.vr_id.id)]).write({'stock': record.vr_id.stock - record.qty})
        return record

    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty <1:
                raise ValidationError("How many {} you want it?".format(rec.vr_id.name))
            elif (rec.vr_id.stock < rec.qty):
                raise ValidationError("Stock () not enough. There just {} left".format(rec.vr_id.name,rec.vr_id.stock))
                
    
    
    
    
    