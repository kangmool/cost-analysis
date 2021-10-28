import logging

from spaceone.core.manager import BaseManager
from spaceone.core.connector.space_connector import SpaceConnector
from spaceone.billing.error import *

_LOGGER = logging.getLogger(__name__)


class SecretManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.secret_connector: SpaceConnector = self.locator.get_connector('SpaceConnector', service='secret')

    def list_secrets(self, query, domain_id):
        return self.secret_connector.dispatch('Secret.list', {'query': query, 'domain_id': domain_id})

    def get_secret(self, secret_id, domain_id):
        return self.secret_connector.dispatch('Secret.get', {'secret_id': secret_id, 'domain_id': domain_id})

    def get_secret_data(self, secret_id, domain_id):
        response = self.secret_connector.dispatch('Secret.get_data', {'secret_id': secret_id, 'domain_id': domain_id})
        return response['data']
