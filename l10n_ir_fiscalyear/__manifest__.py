# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "jalali Support - fiscal year",
    "version": "0.1",
    'author': "Fadoo",
    'maintainer': ["saeed-raeisi"],
    'website': "http://www.fadoo.ir",
    'support': "fadoo.iran@gmail.com",
    "summary": "Iran Localization of Events Organization",
    "category": "Localization/Iran",
    "depends": ["account", "account_accountant"],
    'images': ['static/description/banner.gif'],
    'Live_test_url':'demo.fadoo.ir',
    "data": [
     "views/res_config_settings_views.xml",
    ],
    "external_dependencies": {
        "python": ["jdatetime"],
    },
    'installable': True,
    'price': 0.0,
    'currency': 'USD',
    'application': False,
    'auto_install': False,
    'license': 'OPL-1'
}
