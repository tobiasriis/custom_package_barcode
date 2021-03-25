{
    'name': "custom_package_barcode",
    'description': "Customizes the package_barcode report for Parafusos Express",
    'author': "Tobias Riis @ IT Brasil",
    'category': 'Uncategorized',
    'application': False,
    'version': '0.1',
    'website': 'http://itbrasil.com.br/',
    'data': [
        'reports/package_barcode.xml',
        'reports/package_barcode_template_parafusos.xml'
    ],
    'depends': ['base', 'stock'], #modulos requeridos para essa funciona
}