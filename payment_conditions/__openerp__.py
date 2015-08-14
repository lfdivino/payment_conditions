{
    'name' : 'Payment Conditions',
    'version' : '1.0',
    'author' : 'OpenERP SA',
    'category': 'Accounting & Finance',
    'sequence': 10,
    'summary': 'Financial and Analytic Accounting',
    'description': """
Accounting Access Rights
========================
It gives the Administrator user access to all accounting features such as journal items and the chart of accounts.

It assigns manager and user access rights to the Administrator and only user rights to the Demo user.
""",
    'website': 'https://www.odoo.com/page/accounting',
    'depends' : ['account_payment_sale'],
    'data': [
  #      'views/payment_conditions.xml'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}