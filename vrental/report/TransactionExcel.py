from odoo import models, fields


class PartnerXlsx(models.AbstractModel):
    _name = 'report.vrental.report_transaction_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    date_lap = fields.Date.today()
    
    def generate_xlsx_report(self, workbook, data, transaction):
        sheet = workbook.add_worksheet('Transaction Register')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.date_lap))
        sheet.write(1, 0, 'No. Note')
        sheet.write(1, 1, 'Name') 
        sheet.write(1, 2, 'Transaction Date')
        sheet.write(1, 3, 'Renting Day') 
        sheet.write(1, 4, 'Total Cost') 
        
        row = 2
        col = 0
        for obj in transaction:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.customer_name.name)
            sheet.write(row, col+2, str(obj.start_date))
            sheet.write(row, col+3, obj.rent_day)
            sheet.write(row, col+4, obj.total_cost)
            row += 1