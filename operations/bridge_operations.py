import json

import constants
import model.bridge
import ovs_connection
import ovs_exceptions.ovs_exceptions

class BridgeOperations(object):

    table_name = 'Bridge'

    @staticmethod
    def get_bridge(bridge_name):
        request = {
            'method': constants.Method.transact.value,
            'params': [
                constants.OVSDB_NAME,
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
        request = json.dumps(request)
        with ovs_connection.OVSConnection() as conn:
            conn.send(request)
            response = conn.receive()
        response = json.loads(response)
        if response['error']:
            raise ovs_exceptions.ovs_exceptions.OVSException(response['error'].strip('\n '))
        response_rows = response['result'][0]['rows']
        bridges = list()
        for response_row in response_rows:
            bridge = model.bridge.Bridge(
                response_row['name'],
                auto_attach=response_row['auto_attach'][1],
                controller=response_row['controller'][1],
                datapath_id=response_row['datapath_id'],
                datapath_type=response_row['datapath_type'],
                datapath_version=response_row['datapath_version'],
                external_ids={key: value for key, value in response_row['external_ids'][1]},
                fail_mode=response_row['fail_mode'][1],
                flood_vlans=response_row['flood_vlans'][1],
                ipfix=response_row['ipfix'][1],
                mcast_snooping_enable=response_row['mcast_snooping_enable'],
                mirrors=response_row['mirrors'][1],
                netflow=response_row['netflow'][1],
                other_config={key: value for key, value in response_row['other_config'][1]},
                ports=[value for key, value in response_row['ports'][1]],
                protocols=response_row['protocols'][1],
                rstp_enabled=response_row['rstp_enable'],
                rstp_status={key: value for key, value in response_row['rstp_status'][1]},
                sflow=response_row['sflow'][1],
                status={key: value for key, value in response_row['status'][1]},
                stp_enable=response_row['stp_enable']
            )
            bridges.append(bridge)
        if (len(bridges) == 1):
            return bridges[0]
        else:
            return bridges
