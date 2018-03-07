# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'TD Theme',
    'description': 'TD website theme to showcase customization possibilities.',
    'category': 'Theme',
    'author': 'SSI - Chad',
    'sequence': 1000,
    'version': '1.0',
    'depends': ['website', 'sale'],
    'data': [
        'data/theme_td_data.xml',
        'views/theme_td_templates.xml',
        'views/layout.xml',
        'views/assets.xml',
        'views/snippets.xml',
    ],
    
    'images': [
        'static/description/ssi.png',
        'static/description/theme_default_screenshot.jpg',
    ],
    'application': False,

}
