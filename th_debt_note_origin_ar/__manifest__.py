# -*- coding: utf-8 -*-
{
    'name': "Mostrar campo documento de origen para ND Argentina",

    'summary': """
        Muestra el campo Docuemnto de origen al crear una ND Argentina
    """,

    'description': """
        Muestra el campo Documento de origen al crear una ND Argentina
        Debe llenarse de la forma XXXX-XXXXXXXX donde los 4 primeros
        digitos son el PV y los 8 ultimos digitos es el numero de comprobante
    """,

    'author': "TRIX.Hosting",
    'website': "https://trix.hosting",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'account',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
        # 'demo/demo.xml',
    # ],
}