# -*- coding: utf-8 -*-
{
    'name': "Multi Website Sale Stock",

    'summary': """
        Multi website customisations for sale stock.
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Bizitas",
    'website': "http://www.bizitas.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'stock',
        'bz_multi_website',
        'website_sale_stock'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/website_views.xml',
        'views/templates.xml',
    ],
}
