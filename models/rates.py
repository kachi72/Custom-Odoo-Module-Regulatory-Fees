from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime


class RegulatoryPayments(models.Model):
    _name = "regulatory.payments"
    _description = "keeps account of payment of regulatory fees"

#   fields
    fee_name = fields.Selection([
        ('industrial training fund', 'Industrial Training Fund ITF'),
        ('national social insurance trust fund', 'National Social Insurance Trust Fund NSITF'),
        ('tax clearance certificate', 'Tax Clearance Certificate'),
        ('pencom', 'Pencom'),
        ('department of petroleum resources', 'Department of Petroleum Resources DPR'),
        ('lagos state signage and advertisement agency', 'Lagos State Signage And Advertisement Agency LASAA'),
        ('lagos state environmental protection agency', 'Lagos State Environmental Protection Agency LASEPA'),
        ('national information technology development agency', 'National Information Technology Development Agency NITDA'),
        ('bureau of public procurement', 'Bureau of Public Procurement BPP'),
        ('fumigation certificate', 'Fumigation Certificate'),
        ('fire service certificate', 'Fire Service Certificate'),
        ('local govt and radio', 'Local Government & Radio'),
        ('land use charge', 'Land Use Charge'),
        ('health management organization', 'Health Management Organization HMO'),
        ('group life', 'Group Life'),], string="Agency", required=True, index=True)
    price = fields.Integer(string='Price(Naira)', required=True)
    date_of_payment = fields.Date(string='Date of Payment')
    time = fields.Selection([
        ('annually', 'Annually'),
        ('quarterly', 'Quarterly'),
        ('biannually', 'Biannually'),
        ('monthly', 'Monthly')], string='Frequency', required=True)
    next_payment = fields.Date(string='Next Due', required=True)

    @api.constrains('next_payment')
    def _check_date_not_earlier_than_current_date(self):
        for record in self:
            if record.next_payment and record.next_payment < datetime.now().date():
                raise ValidationError("Date cannot be earlier than the current date!")

