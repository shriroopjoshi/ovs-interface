import json

import constants
import ovs_connection
from ovs_exceptions.ovs_exceptions import OVSException
from ovs_exceptions.ovs_exceptions import OVSTransactionException

class OVSOperations(object):

    @staticmethod
    def get(table, *conditions):
        request = {
            'id': ovs_connection.TransactionID.id(),
            'method': constants.Method.transact.value,
            'params': [
                constants.OVSDB_NAME,
                {
                    'op': constants.Operations.select.value,
                    'table': table,
                    'where': [condition for condition in conditions]
                }
            ]
        }
        response = None
        # print('REQUEST: %s' % request)
        with ovs_connection.OVSConnection() as connection:
            connection.send(json.dumps(request))
            response = json.loads(connection.receive())
        # print('RESPONSE: %s' % response)
        if response['error']:
            raise OVSTransactionException(response['error'].strip())
        if 'error' in response['result'][0]:
            raise OVSException(response['result'][0]['error'], response['result'][0]['details'])
        return response['result'][0]['rows']

    @staticmethod
    def update(table, record, *conditions):
        request = {
            'id': ovs_connection.TransactionID.id(),
            'method': constants.Method.transact.value,
            'params': [
                constants.OVSDB_NAME,
                {
                    'op': constants.Operations.update.value,
                    'table': table,
                    'where': [condition for condition in conditions],
                    'row': record
                }
            ]
        }
        response = None
        # print('REQUEST: %s' % request)
        with ovs_connection.OVSConnection() as connection:
            connection.send(json.dumps(request))
            response = json.loads(connection.receive())
        # print('RESPONSE: %s' % response)
        if response['error']:
            raise OVSTransactionException(response['error'].strip())
        if 'error' in response['result'][0]:
            raise OVSException(response['result'][0]['error'], response['result'][0]['details'])
        return response['result'][0]['count']
