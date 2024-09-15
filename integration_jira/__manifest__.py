{
    'name': 'Odoo Jira Project Progress',
    'version': '1.1',
    'category': 'Project',
    'summary': 'View Jira project progress in Odoo',
    'description': """
        This module fetches and displays Jira project progress in a table format within Odoo.
    """,
    'author': 'Nicolás López',
    'depends': ['base', 'project'],
    'data': [
        'views/jira_project_progress_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'integration_jira/static/src/css/form_styles.css',
        ],
        },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}