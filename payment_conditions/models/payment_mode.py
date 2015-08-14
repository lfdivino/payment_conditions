__author__ = 'kmee'

from openerp import models, fields, api
from openerp.exceptions import Warning

class PaymentModel(models.Model):
    _inherit = 'payment.mode'

    verificarLimiteCredito = fields.Boolean(string='Verificar credito', default=True)


class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'

    payment_mode_id = fields.Many2many('payment.mode', 'payment_mode_rel',
                                       'payment_term_id', 'payment_mode_id', string='Modo de pagamento')

    valorMinimo = fields.Float(string='Valor minimo de compra', default=0)

    valorMaximo = fields.Float(string='Valor maximo de compra', default=0)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    payment_term = fields.Many2one('account.payment.term', 'Payment Term',
                                   domain="[('payment_mode_id','=',payment_mode_id)]")

    @api.model
    def test_paid(self):
        if not self.payment_mode_id.verificarLimiteCredito:
            if(self.amount_total < self.payment_term.valorMinimo):
                raise Warning('Valor de compra menor do que o valor minimo para essa operacao!')
                return False

            if(self.amount_total > self.payment_term.valorMaximo) or self.payment_term.valorMaximo == 0:
                raise Warning('Valor de compra maior do que o valor maximo para essa operacao!')
                return False
            return True
        else:
            if (self.amount_total <= (self.partner_id.credit_limit - self.partner_id.credit)):
                if(self.amount_total < self.payment_term.valorMinimo):
                    raise Warning('Valor de compra menor do que o valor minimo para essa operacao!')
                    return False

                if(self.amount_total > self.payment_term.valorMaximo) or self.payment_term.valorMaximo == 0:
                    raise Warning('Valor de compra maior do que o valor maximo para essa operacao!')
                    return False
                return True
            raise Warning('Caloteeeeeeee! Credito disponivel: {}'.format((self.partner_id.credit_limit - self.partner_id.credit)))
            return False