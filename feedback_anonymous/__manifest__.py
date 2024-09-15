{
    'name': 'Feedback Anónimo en Tiempo Real',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Permite a los empleados enviar feedback anónimo en tiempo real.',
    'description': """
        Este módulo permite a los empleados enviar feedback anónimo en tiempo real, 
        con análisis de sentimiento incluido.
    """,
    'author': 'N1000',
    'website': 'https://www.tusitio.com',
    'depends': ['base', 'mail'],
    'data': [
       'views/feedback_view.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'feedback_anonymous/static/src/css/custom_styles.css',
        ],
        },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}