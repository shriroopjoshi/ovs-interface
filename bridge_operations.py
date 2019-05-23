import model
import json
import ovs_connection
import constants

class BridgeOperations(object):

    table_name = 'Bridge'

    @staticmethod
    def get_bridge(bridge_name):
        request = {
            'method': constants.Method.transact.value,
            'params': [
                model.DB_NAME,
                {
                    'op': constants.Operations.select.value,
                    'table': BridgeOperations.table_name,
                    'where': [
                        ['name', '==', str(bridge_name)]
                    ]
                }
            ],
            'id': 0
        }
        response = None
        conn = ovs_connection.OVSConnection()
        conn.connect()
        request = json.dumps(request)
        print request
        conn.send(request)
        response = conn.receive()
        conn.disconnect()
        print response
