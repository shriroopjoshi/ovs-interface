import json

import constants
from model.open_vswitch import Open_vSwitch
from operations.ovs_operations import OVSOperations


class Open_vSwitchOperations(OVSOperations):

    @staticmethod
    def get():
        record = super(Open_vSwitchOperations, Open_vSwitchOperations).get(
            constants.OVSDBTables.open_vswitch.value
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
            other_config={key: value for key, value in record['other_config'][1]},
            ovs_version=record['ovs_version'],
            ssl=record['ssl'][1],
            statistics={key: value for key, value in record['statistics'][1]},
            system_type=record['system_type'],
            system_version=record['system_version'],
            uuid=record['_uuid'][1]
        )

    @staticmethod
    def update(open_vswitch):
        record = {
            'bridges': ['set', [['uuid', str(_)] for _ in open_vswitch.bridges]],
            'cur_cfg': open_vswitch.cur_cfg,
            'datapath_types': ['set', [_ for _ in open_vswitch.datapath_types]],
            'db_version': open_vswitch.db_version,
            'external_ids': ['map', [
                [_, open_vswitch.external_ids[_]] for _ in open_vswitch.external_ids
            ]],
            'iface_types': ['set', [_ for _ in open_vswitch.iface_types]],
            'manager_options': ['set', [_ for _ in open_vswitch.manager_options]],
            'next_cfg': open_vswitch.next_cfg,
            'other_config': ['map', [
                [_, open_vswitch.other_config[_]] for _ in open_vswitch.other_config
            ]],
            'ovs_version': open_vswitch.ovs_version,
            'ssl': ['set', [_ for _ in open_vswitch.ssl]],
            'statistics': ['map', [
                [_, open_vswitch.statistics[_]] for _ in open_vswitch.statistics
            ]],
            'system_type': open_vswitch.system_type,
            'system_version': open_vswitch.system_version
        }
        return super(Open_vSwitchOperations, Open_vSwitchOperations).update(
            constants.OVSDBTables.open_vswitch.value, record,
            ['_uuid', '==', ['uuid', str(open_vswitch.uuid)]]
        )
