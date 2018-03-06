# -*- coding: utf-8 -*-
{
    'name': "Multi Website Sale",

    'summary': """
        Add multi website to ecommerce.
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
        'bz_multi_website',
        'website_sale'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/website_views.xml',
        'views/templates.xml',
        'data/data.xml'
    ],
}
