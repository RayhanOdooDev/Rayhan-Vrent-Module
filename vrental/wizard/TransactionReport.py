from odoo import api, fields, models


class TransactionReport(models.Model):
    _name = 'vrental.transactionreport'
    _description = 'New Description'

    customer_id = fields.Many2one(comodel_name='vrental.customer', 
                                string='Customer',
                                required=False)
    from_date = fields.Date(string='From Date', 
                                required=False)
    to_date = fields.Date(string='To Date', 
                                required=False)
    
    
    def action_transaction_report(self):
        filter = []
        customer_id = self.customer_id
        from_date = self.from_date
        to_date = self.to_date
        if customer_id:
            filter += [('customer_name', '=', customer_id.id)]
        if from_date:
            filter += [('start_date', '>=', from_date)]
        if to_date:
            filter += [('start_date', '<=', to_date)]
        print(filter)
        transaction = self.env['vrental.transaction'].search_read(filter)
        print(transaction)
        data = {
            'form': self.read()[0],
            'transaction': transaction
        }
        return self.env.ref('vrental.wizard_transactionreport_pdf').report_action(self, data=data)
        

    
