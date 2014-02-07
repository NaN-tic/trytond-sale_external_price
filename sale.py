#This file is part sale_external_price module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    'Sale'
    __name__ = 'sale.sale'
    external_untaxed_amount = fields.Numeric('Untaxed', readonly=True,
        digits=(16, Eval('currency_digits', 2)), depends=['currency_digits'])
    external_tax_amount = fields.Numeric('Tax', readonly=True,
        digits=(16, Eval('currency_digits', 2)), depends=['currency_digits'])
    external_total_amount = fields.Numeric('Total', readonly=True,
        digits=(16, Eval('currency_digits', 2)), depends=['currency_digits'])
