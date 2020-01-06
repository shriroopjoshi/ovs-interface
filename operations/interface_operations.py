import json

import constants
from model.interface import Interface
from operations.ovs_operations import OVSOperations


class InterfaceOperations(OVSOperations):

    @staticmethod
    def get_interfaces(*conditions):
        interfaces = list()
        response = super(InterfaceOperations, InterfaceOperations).get(
            constants.OVSDBTables.interface.value, *conditions
        )
        for record in response:
            interfaces.append(Interface(
                record['name'],
                admin_state=record['admin_state'],
                bfd={key: value for key, value in record['bfd'][1]},
                bfd_status={key: value for key, value in record['bfd_status'][1]},
                cfm_fault=record['cfm_fault'][1],
                cfm_fault_status=record['cfm_fault_status'][1],
                cfm_flap_count=record['cfm_flap_count'][1],
                cfm_health=record['cfm_health'][1],
                cfm_mpid=record['cfm_mpid'][1],
                cfm_remote_mpids=record['cfm_remote_mpids'][1],
                cfm_remote_opstate=record['cfm_remote_opstate'][1],
                duplex=record['duplex'][1],
                error=record['error'][1],
                external_ids={key: value for key, value in record['external_ids'][1]},
                ifindex=record['ifindex'],
                ingress_policing_burst=record['ingress_policing_burst'],
                ingress_policing_rate=record['ingress_policing_rate'],
                lacp_current=record['lacp_current'][1],
                link_resets=record['link_resets'],
                link_speed=record['link_speed'][1],
                link_state=record['link_state'],
                lldp={key: value for key, value in record['lldp'][1]},
                mac=record['mac'][1],
                mac_in_use=record['mac_in_use'],
                mtu=record['mtu'],
                mtu_request=record['mtu_request'][1],
                ofport=record['ofport'],
                ofport_request=record['ofport_request'][1],
                options={key: value for key, value in record['options'][1]},
                other_config={key: value for key, value in record['other_config'][1]},
                statistics={key: value for key, value in record['statistics'][1]},
                status={key: value for key, value in record['status'][1]},
                type=record['type'],
                uuid=record['_uuid'][1]
            ))
        return interfaces

    @staticmethod
    def get_interface_by_name(name):
        interfaces = InterfaceOperations.get_interfaces(['name', '==', str(name)])
        return interfaces[0] if interfaces else None

    @staticmethod
    def get_interfaces_by_uuid(uuid):
        interfaces = InterfaceOperations.get_interfaces(['_uuid', '==', ['uuid', str(uuid)]])
        return interfaces[0] if interfaces else None

    @staticmethod
    def update_interface(interface, *conditions):
        record = {
            'admin_state': interface.admin_state,
            'bfd': ['map', [[_, interface.bfd[_]] for _ in interface.bfd]],
            'bfd_status': ['map', [[_, interface.bfd_status[_]] for _ in interface.bfd_status]],
            'cfm_fault': ['set', [_ for _ in interface.cfm_fault]],
            'cfm_fault_status': ['set', [_ for _ in interface.cfm_fault_status]],
            'cfm_flap_count': ['set', [_ for _ in interface.cfm_flap_count]],
            'cfm_health': ['set', [_ for _ in interface.cfm_health]],
            'cfm_mpid': ['set', [_ for _ in interface.cfm_mpid]],
            'cfm_remote_mpids': ['set', [_ for _ in interface.cfm_remote_mpids]],
            'cfm_remote_opstate': ['set', [_ for _ in interface.cfm_remote_opstate]],
            'duplex': ['set', [_ for _ in interface.duplex]],
            'error': ['set', [_ for _ in interface.error]],
            'external_ids': ['map', [
                [_, interface.external_ids[_]] for _ in interface.external_ids
            ]],
            'ifindex': interface.ifindex,
            'ingress_policing_burst': interface.ingress_policing_burst,
            'ingress_policing_rate': interface.ingress_policing_rate,
            'lacp_current': ['set', [_ for _ in interface.lacp_current]],
            'link_resets': interface.link_resets,
            'link_speed': ['set', [_ for _ in interface.link_speed]],
            'link_state': interface.link_state,
            'lldp': ['map', [[_, interface.lldp[_]] for _ in interface.lldp]],
            'mac': ['set', [_ for _ in interface.mac]],
            'mac_in_use': interface.mac_in_use,
            'mtu': interface.mtu,
            'mtu_request': ['set', [_ for _ in interface.mtu_request]],
            'ofport': interface.ofport,
            'ofport_request': ['set', [_ for _ in interface.ofport_request]],
            'options': ['map', [[_, interface.options[_]] for _ in interface.options]],
            'other_config': ['map', [
                [_, interface.other_config[_]] for _ in interface.other_config
            ]],
            'statistics': ['map', [[_, interface.statistics[_]] for _ in interface.statistics]],
            'status': ['map', [[_, interface.status[_]] for _ in interface.status]],
            'type': interface.type
        }
        return super(InterfaceOperations, InterfaceOperations).update(
            constants.OVSDBTables.interface.value, record, *conditions
        )

    @staticmethod
    def update_interface_by_name(name, interface):
        return InterfaceOperations.update_interface(interface, ['name', '==', str(name)])

    @staticmethod
    def update_interface_by_uuid(uuid, interface):
        return InterfaceOperations.update_interface(interface, ['_uuid', '==', ['uuid', str(uuid)]])
