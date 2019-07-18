import json

import constants
from model.open_vswitch import Open_vSwitch
from operations.ovs_operations import OVSOperations

class Open_vSwitchOperations(OVSOperations):

    @staticmethod
    def get():
        record = super(Open_vSwitchOperations, Open_vSwitchOperations).get(
            constants.Operations.select.value, constants.OVSDBTables.open_vswitch.value, *([])
        )[0]
        return Open_vSwitch(
            bridges=[bridge for _, bridge in record['bridges'][1]],
            cur_cfg=record['cur_cfg'],
            datapath_types=record['datapath_types'][1],
            db_version=record['db_version'],
            dpdk_initialized=record['dpdk_initialized'],
            dpdk_version=record['dpdk_version'],
            external_ids={key: value for key, value in record['external_ids'][1]},
            iface_types=record['iface_types'][1],
            manager_options=record['manager_options'][1],
            next_cfg=record['next_cfg'],
            other_configs={key: value for key, value in record['other_config'][1]},
            ovs_version=record['ovs_version'],
            ssl=record['ssl'][1],
            statistics={key: value for key, value in record['statistics'][1]},
            system_type=record['system_type'],
            system_version=record['system_version'],
            uuid=record['_uuid'][1]
        )
