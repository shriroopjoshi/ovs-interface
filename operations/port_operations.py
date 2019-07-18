import json

import constants
import model.port
import ovs_connection
import ovs_exceptions.ovs_exceptions

class PortOperations(object):

    @staticmethod
    def get_ports(*conditions):
        request = {
            'method': constants.Method.transact.value,
            'params': [
                constants.OVSDB_NAME,
                {
                    'op': constants.Operations.select.value,
                    'table': constants.OVSDBTables.port.value,
                    'where': [condition for condition in conditions]
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
        response_rows = response['result'][0]['rows']
        ports = list()
        for response_row in response_rows:
            ports.append(model.port.Port(
                response_row['name'],
                bond_active_slave=response_row['bond_active_slave'][1],
                bond_downdelay=response_row['bond_downdelay'],
                bond_fake_iface=response_row['bond_fake_iface'],
                bond_mode=response_row['bond_mode'][1],
                bond_updelay=response_row['bond_updelay'],
                cvlans=response_row['cvlans'][1],
                external_ids={key: value for key, value in response_row['external_ids'][1]},
                fake_bridge=response_row['fake_bridge'],
                interfaces=[intf for _, intf in response_row['interfaces'][1]] if(
                    response_row['interfaces'][0] == 'set') else [response_row['interfaces'][1]],
                lacp=response_row['lacp'][1],
                mac=response_row['mac'][1],
                other_config={key: value for key, value in response_row['other_config'][1]},
                protected=response_row['protected'],
                qos=response_row['qos'][1],
                rstp_statistics={key: value for key, value in response_row['rstp_statistics'][1]},
                rstp_status={key: value for key, value in response_row['rstp_status'][1]},
                statistics={key: value for key, value in response_row['statistics'][1]},
                status={key: value for key, value in response_row['status'][1]},
                tag=response_row['tag'][1],
                trunks=response_row['trunks'][1],
                vlan_mode=response_row['vlan_mode'][1],
                uuid=response_row['_uuid'][1]
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