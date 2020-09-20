# -*- coding: utf-8 -*-
{
    'name': "Tiempo de Entrega en Presupuesto",

    'summary': """
        Agrega el campo Tiempo Inicial de Entrega al presupuesto""",

    'description': """
        Agrega la columna Tiempo Inicial de Entrega en el presupuesto
    """,

    'author': "TRIX.Hosting",
    'website': "https://trix.hosting",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','sale_management','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/entrega_view.xml',
        # 'report/entrega_report_templates.xml',
    ],
    'installable' : True,
}