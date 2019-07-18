import json

import constants
from model.bridge import Bridge
from operations.ovs_operations import OVSOperations

class BridgeOperations(OVSOperations):

    @staticmethod
    def get_bridges(*conditions):
        bridges = list()
        response = super(BridgeOperations, BridgeOperations).get(
            constants.Operations.select.value, constants.OVSDBTables.bridge.value, *conditions
        )
        for record in response:
            bridges.append(Bridge(
                record['name'],
                auto_attach=record['auto_attach'][1],
                controller=record['controller'][1],
                datapath_id=record['datapath_id'],
                datapath_type=record['datapath_type'],
                datapath_version=record['datapath_version'],
                external_ids={key: value for key, value in record['external_ids'][1]},
                fail_mode=record['fail_mode'][1],
                flood_vlans=record['flood_vlans'][1],
                ipfix=record['ipfix'][1],
                mcast_snooping_enable=record['mcast_snooping_enable'],
                mirrors=record['mirrors'][1],
                netflow=record['netflow'][1],
                other_config={key: value for key, value in record['other_config'][1]},
                ports=[port for _, port in record['ports'][1]] if (
                    record['ports'][0] == 'set') else [record['ports'][1]],
                protocols=record['protocols'][1],
                rstp_enabled=record['rstp_enable'],
                rstp_status={key: value for key, value in record['rstp_status'][1]},
                sflow=record['sflow'][1],
                status={key: value for key, value in record['status'][1]},
                stp_enable=record['stp_enable'],
                uuid=record['_uuid'][1]
            ))
        return bridges

    @staticmethod
    def get_bridge_by_name(name):
        bridges = BridgeOperations.get_bridges(['name', '==', str(name)])
        return bridges[0] if bridges else None

    @staticmethod
    def get_bridge_by_uuid(uuid):
        bridges = BridgeOperations.get_bridges(['_uuid', '==', ['uuid', str(uuid)]])
        return bridges[0] if bridges else None
