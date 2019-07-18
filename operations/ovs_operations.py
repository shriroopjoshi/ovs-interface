import json

import constants
import ovs_connection
from ovs_exceptions.ovs_exceptions import OVSException

class OVSOperations(object):

    @staticmethod
    def get(operation, table, *conditions):
        request = {
            'method': constants.Method.transact.value,
            'params': [
                constants.OVSDB_NAME,
                {
                    'op': operation,
                    'table': table,
                    'where': [condition for condition in conditions]
                }
            ],
            'id': ovs_connection.TransactionID.id()
        }
        response = None
        # print('REQUEST: %s' % request)
        with ovs_connection.OVSConnection() as connection:
            connection.send(json.dumps(request))
            response = json.loads(connection.receive())
        # print('RESPONSE: %s' % response)
        if response['error']:
            raise OVSException(response['error'].strip())
        return response['result'][0]['rows']
