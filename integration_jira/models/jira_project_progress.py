from odoo import models, fields, api
from odoo.exceptions import UserError
import requests
from requests.auth import HTTPBasicAuth
import logging

class JiraProjectProgress(models.Model):
    _name = 'jira.project.progress'
    _description = 'Jira Project Progress'

    _logger = logging.getLogger(__name__)  # Logger para depuración

    jira_url = fields.Char('Jira URL', required=True)
    jira_username = fields.Char('Jira Username', required=True)
    jira_api_token = fields.Char('Jira API Token', required=True)
    
    # Campos adicionales para la vista de árbol
    project_key = fields.Char('Project Key')
    summary = fields.Char('Summary')

    @api.model
    def create(self, vals):
        record = super(JiraProjectProgress, self).create(vals)
        try:
            record._call_jira_api()
        except Exception as e:
            raise UserError(f'Error while calling Jira API: {e}')
        return record

    def _call_jira_api(self):
        """Fetch project data from Jira and update the record in Odoo."""
        for record in self:
            # Construir la URL para obtener los proyectos desde Jira
            api_url = f"{record.jira_url}/rest/api/2/project/search"
            auth = HTTPBasicAuth(record.jira_username, record.jira_api_token)

            try:
                # Realiza la solicitud a Jira para obtener los detalles
                response = requests.get(api_url, auth=auth)
                response.raise_for_status()  # Lanza un error si la respuesta HTTP tiene un código de error
                data = response.json()

                # Imprimir el JSON completo en la terminal
                print(data)  # Imprime en la terminal
                self._logger.info(f"Jira API Response: {data}")  # También lo registra en el logger

                # Verificar si la respuesta tiene proyectos
                if data.get('values'):
                    # Iterar sobre los proyectos y extraer información
                    for project in data['values']:
                        project_key = project.get('key')
                        summary = project.get('name')
                        
                        # Actualizar los campos en Odoo con la información obtenida de Jira
                        record.write({
                            'project_key': project_key,
                            'summary': summary,
                        })
                else:
                    raise UserError('No projects found in Jira response.')

            except requests.RequestException as e:
                # Manejo de errores si la solicitud a Jira falla
                raise UserError(f'Failed to fetch data from Jira: {e}')
