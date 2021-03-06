# -*- coding: utf-8 -*-
##################
#
#   Uniceramica.it
#
##################

{
    'name': 'Uniceramica',
    'version': '0.0.1.0.0',
    'summary': """Modulo per la gestione di Uniceramica.""",
    'description': "Questo modulo serve per gestire le funzionalit√† aggiuntive necesssarie per una migliore gestione.",
    'category': "Inventory",
    'author': 'Uniceramica',
    'company': 'Uniceramica',
    'website': "https://uniceramica.it",
    'depends': ['base', 'stock', 'web','website_sale','sale','sale_management'],
    'data': [
        'templates/ddt.xml',
        'templates/layout.xml',
        'templates/preventivo_ordine.xml',
        'templates/website_product.xml',
        'templates/website_partner.xml',
        'views/brand_views.xml',
        'views/series_views.xml',
        'views/preventivo_ordine.xml',
        'views/product_category.xml',
        'views/product_template.xml',
        'views/volume_view.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
}
