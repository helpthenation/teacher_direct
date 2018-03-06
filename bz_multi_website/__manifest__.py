# -*- coding: utf-8 -*-
{
    'name': "Multi Website",

    'summary': """
        Allows you to create multiple websites.
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
        'website',
        'auth_signup',
        'website_theme_install'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/website_views.xml',
        'views/res_users_views.xml',
        'views/ir_attachment_views.xml',
        'views/ir_module_views.xml',
        'views/templates.xml',
        'data/data.xml'
    ],
}