from operations.interface_operations import InterfaceOperations
from operations.port_operations import PortOperations

def get_all_interfaces():
    interfaces = InterfaceOperations.get_interfaces()
    for interface in interfaces:
        print('%s: %s\n' % (interface.name, str(interface)))


def get_interface_by_name(name):
    interface = InterfaceOperations.get_interface_by_name(name)
    if interface:
        print('%s: %s' % (interface.name, str(interface)))
    else:
        print('No such interface')


def get_interfaces_by_uuid(port_name):
    port = PortOperations.get_port_by_name(port_name)
    if not port:
        print('No such port')
        return
    for interface_uuid in port.interfaces:
        interface = InterfaceOperations.get_interfaces_by_uuid(interface_uuid)
        print('%s: %s' % (interface.name, str(interface)))


def update_external_ids(name, key, value):
    interface = InterfaceOperations.get_interface_by_name(name)
    if not interface:
        print('No such interface')
        return

    interface.external_ids[key] = value
    print('Rows updated = %s' % \
        InterfaceOperations.update_interface_by_name(interface.name, interface))
    
    interface = InterfaceOperations.get_interface_by_name(name)
    interface.external_ids.pop(key)
    print('Rows updated = %s' % \
        InterfaceOperations.update_interface_by_uuid(interface.uuid, interface))

    interface = InterfaceOperations.get_interface_by_name(name)
    assert key not in interface.external_ids
