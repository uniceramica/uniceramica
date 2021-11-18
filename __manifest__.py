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
    'description': "Questo modulo serve per gestire le funzionalità aggiuntive necesssarie per una migliore gestione.",
    'category': "Inventory",
    'author': 'Uniceramica',
    'company': 'Uniceramica',
    'website': "https://uniceramica.it",
    'depends': ['base', 'stock', 'l10n_it_stock_ddt','web','website_sale','sale','sale_management'],
    'data': [
        'templates/ddt.xml',
        'templates/report.xml',
        'templates/preventivo_ordine.xml',
        'views/volume_view.xml'
    ],
    'demo': [],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
}
