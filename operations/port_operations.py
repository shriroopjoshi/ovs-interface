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