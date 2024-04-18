{
    'name': "Regulatory Payments",
    'version': '1.0',
    'depends': ['base'],
    'sequence': -100,
    'summary': "Management of fees payed by the company to regulatory agencies",
    'description': '''Management of Regulatory Fees''',
    'author': "Systemtech Services Limited",
    'category': 'Inventory',
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/rates_view.xml'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'

}

