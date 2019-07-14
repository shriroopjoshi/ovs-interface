import json

import constants
import model.open_vswitch
import ovs_connection
import ovs_exceptions.ovs_exceptions

class Open_vSwitchOperations(object):

    @staticmethod
    def get():
        request = {
            'method': constants.Method.transact.value,
            'params': [
                constants.OVSDB_NAME,
                {
                    'op': constants.Operations.select.value,
                    'table': constants.OVSDBTables.open_vswitch.value,
                    'where': []
                }
            ],
            'id': ovs_connection.TransactionID.id()
        }
        response = None
        with ovs_connection.OVSConnection() as conn:
            conn.send(json.dumps(request))
            response = json.loads(conn.receive())
        if response['error']:
            raise ovs_exceptions.ovs_exceptions.OVSException(response['error'].strip())
        response_row = response['result'][0]['rows'][0]
        return model.open_vswitch.Open_vSwitch(
            bridges=[bridge for _, bridge in response_row['bridges'][1]],
            cur_cfg=response_row['cur_cfg'],
            datapath_types=response_row['datapath_types'][1],
            db_version=response_row['db_version'],
            dpdk_initialized=response_row['dpdk_initialized'],
            dpdk_version=response_row['dpdk_version'],
            external_ids={key: value for key, value in response_row['external_ids'][1]},
            iface_types=response_row['iface_types'][1],
            manager_options=response_row['manager_options'][1],
            next_cfg=response_row['next_cfg'],
            other_configs={key: value for key, value in response_row['other_config'][1]},
            ovs_version=response_row['ovs_version'],
            ssl=response_row['ssl'][1],
            statistics={key: value for key, value in response_row['statistics'][1]},
            system_type=response_row['system_type'],
            system_version=response_row['system_version'],
            uuid=response_row['_uuid'][1]
        )
        