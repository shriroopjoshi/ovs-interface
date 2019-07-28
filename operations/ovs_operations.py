import json

import constants
from ovs_connection.transaction import Transaction
from ovs_exceptions.ovs_exceptions import OVSException

class OVSOperations(object):

    @staticmethod
    def get(table, *conditions):
        request = {
            'op': constants.Operations.select.value,
            'table': table,
            'where': [condition for condition in conditions]
        }
        response = None
        # print('REQUEST: %s' % request)
        with Transaction() as handle:
            handle.add_request_payload(request)
            handle.apply()
            response = handle.response[0]
        # print('RESPONSE: %s' % response)
        if not response:
            raise OVSException('No response')
        if 'error' in response:
            raise OVSException('%s: %s' % (response['error'].strip(), response['details'].strip()))
        return response['rows']

    @staticmethod
    def update(table, record, *conditions):
        request = {
            'op': constants.Operations.update.value,
            'table': table,
            'where': [condition for condition in conditions],
            'row': record
        }
        response = None
        # print('REQUEST: %s' % request)
        with Transaction() as handle:
            handle.add_request_payload(request)
            handle.apply()
            response = handle.response[0]
        # print('RESPONSE: %s' % response)
        if not response:
            raise OVSException('No response')
        if 'error' in response:
            raise OVSException('%s: %s' % (response['error'].strip(), response['details'].strip()))
        return response['count']
