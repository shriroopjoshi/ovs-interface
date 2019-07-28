import json

import constants
from model.bridge import Bridge
from operations.ovs_operations import OVSOperations

class BridgeOperations(OVSOperations):

    @staticmethod
    def get_bridges(*conditions):
        bridges = list()
        response = super(BridgeOperations, BridgeOperations).get(
            constants.OVSDBTables.bridge.value, *conditions
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
                rstp_enable=record['rstp_enable'],
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

    @staticmethod
    def update_bridge(bridge, *conditions):
        record = {
            'auto_attach': ['set', [_ for _ in bridge.auto_attach]],
            'controller': ['set', [_ for _ in bridge.controller]],
            'datapath_id': bridge.datapath_id,
            'datapath_type': bridge.datapath_type,
            'datapath_version': bridge.datapath_version,
            'external_ids': ['map', [
                [_, bridge.external_ids[_]] for _ in bridge.external_ids
            ]],
            'fail_mode': ['set', [_ for _ in bridge.fail_mode]],
            'flood_vlans': ['set', [_ for _ in bridge.flood_vlans]],
            'mcast_snooping_enable': bridge.mcast_snooping_enable,
            'mirrors': ['set', [_ for _ in bridge.mirrors]],
            'netflow': ['set', [_ for _ in bridge.netflow]],
            'other_config': ['map', [
                [_, bridge.other_config[_]] for _ in bridge.other_config
            ]],
            'ports': ['set', [['uuid', str(_)] for _ in bridge.ports]],
            'protocols': ['set', [_ for _ in bridge.protocols]],
            'rstp_enable': bridge.rstp_enable,
            'rstp_status': ['map', [
                [_, bridge.rstp_status[_]] for _ in bridge.rstp_status
            ]],
            'sflow': ['set', [_ for _ in bridge.sflow]],
            'status': ['map', [
                [_ , bridge.status[_]] for _ in bridge.status
            ]],
            'stp_enable': bridge.stp_enable
        }
        return super(BridgeOperations, BridgeOperations).update(
            constants.OVSDBTables.bridge.value, record, *conditions
        )

    def update_bridge_by_name(name, bridge):
        return BridgeOperations.update_bridge(bridge, ['name', '==', str(name)])

    def update_bridge_by_uuid(uuid, bridge):
        return BridgeOperations.update_bridge(bridge, ['_uuid', '==', ['uuid', str(uuid)]])
