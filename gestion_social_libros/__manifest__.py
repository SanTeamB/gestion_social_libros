# -*- coding: utf-8 -*-
{
    'name': "Gestion social libros",

    'summary': """
        Un módulo de odoo que se encarga de gestionar un sistema de comentarios y
        publicar opiniones online acerca de libros.
        """,

    'description': """
        Un módulo de odoo que se encarga de gestionar un sistema de comentarios y
        publicar opiniones online acerca de libros.
    """,

    'author': "Santiago López de Luzuriaga Olmos",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Gestion',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
