import json

import constants
from model.port import Port
from operations.ovs_operations import OVSOperations


class PortOperations(OVSOperations):

    @staticmethod
    def get_ports(*conditions):
        ports = list()
        response = super(PortOperations, PortOperations).get(
            constants.OVSDBTables.port.value, *conditions
        )
        for record in response:
            ports.append(Port(
                record['name'],
                bond_active_slave=record['bond_active_slave'][1],
                bond_downdelay=record['bond_downdelay'],
                bond_fake_iface=record['bond_fake_iface'],
                bond_mode=record['bond_mode'][1],
                bond_updelay=record['bond_updelay'],
                cvlans=record['cvlans'][1],
                external_ids={key: value for key, value in record['external_ids'][1]},
                fake_bridge=record['fake_bridge'],
                interfaces=[intf for _, intf in record['interfaces'][1]] if(
                    record['interfaces'][0] == 'set') else [record['interfaces'][1]],
                lacp=record['lacp'][1],
                mac=record['mac'][1],
                other_config={key: value for key, value in record['other_config'][1]},
                protected=record['protected'],
                qos=record['qos'][1],
                rstp_statistics={key: value for key, value in record['rstp_statistics'][1]},
                rstp_status={key: value for key, value in record['rstp_status'][1]},
                statistics={key: value for key, value in record['statistics'][1]},
                status={key: value for key, value in record['status'][1]},
                tag=record['tag'][1],
                trunks=record['trunks'][1],
                vlan_mode=record['vlan_mode'][1],
                uuid=record['_uuid'][1]
            ))
        return ports

    @staticmethod
    def get_port_by_name(name):
        ports = PortOperations.get_ports(['name', '==', str(name)])
        return ports[0] if ports else None

    @staticmethod
    def get_port_by_uuid(uuid):
        ports = PortOperations.get_ports(['_uuid', '==', ['uuid', str(uuid)]])
        return ports[0] if ports else None

    @staticmethod
    def update_port(port, *conditions):
        record = {
            'bond_active_slave': ['set', [_ for _ in port.bond_active_slave]],
            'bond_downdelay': port.bond_downdelay,
            'bond_fake_iface': port.bond_fake_iface,
            'bond_mode': ['set', [_ for _ in port.bond_mode]],
            'cvlans': ['set', [_ for _ in port.cvlans]],
            'external_ids': ['map', [[_, port.external_ids[_]] for _ in port.external_ids]],
            'fake_bridge': port.fake_bridge,
            'interfaces': ['set', [['uuid', str(_)] for _ in port.interfaces]],
            'lacp': ['set', [_ for _ in port.lacp]],
            'mac': ['set', [_ for _ in port.mac]],
            'other_config': ['map', [[_, port.other_config[_]] for _ in port.other_config]],
            'protected': port.protected,
            'qos': ['set', [_ for _ in port.qos]],
            'rstp_statistics': ['map', [
                [_, port.rstp_statistics[_]] for _ in port.rstp_statistics
            ]],
            'statistics': ['map', [[_, port.statistics[_]] for _ in port.statistics]],
            'status': ['map', [[_, port.status[_]] for _ in port.status]],
            'tag': ['set', [_ for _ in port.tag]],
            'trunks': ['set', [_ for _ in port.trunks]],
            'vlan_mode': ['set', [_ for _ in port.vlan_mode]]
        }
        return super(PortOperations, PortOperations).update(
            constants.OVSDBTables.port.value, record, *conditions
        )

    @staticmethod
    def update_port_by_name(name, port):
        return PortOperations.update_port(port, ['name', '==', str(name)])

    @staticmethod
    def update_port_by_uuid(uuid, port):
        return PortOperations.update_port(port, ['_uuid', '==', ['uuid', str(uuid)]])
