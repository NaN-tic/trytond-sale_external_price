# This file is part sale_external_price module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.config import config as config_

__all__ = ['Sale']
__metaclass__ = PoolMeta

DIGITS = config_.getint('product', 'price_decimal', default=4)


class Sale:
    __name__ = 'sale.sale'
    external_untaxed_amount = fields.Numeric('External Untaxed', readonly=True,
        digits=(16, DIGITS))
    external_tax_amount = fields.Numeric('External Tax', readonly=True,
        digits=(16, DIGITS))
    external_total_amount = fields.Numeric('External Total', readonly=True,
        digits=(16, DIGITS))
    external_shipment_amount = fields.Numeric('External Total Shipment', readonly=True,
        digits=(16, DIGITS))
