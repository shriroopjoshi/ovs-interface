from operations.bridge_operations import BridgeOperations
from operations.port_operations import PortOperations

def get_all_ports():
    ports = PortOperations.get_ports()
    for port in ports:
        print('%s: %s' % (port.name, str(port)))

def get_port_by_name(name):
    port = PortOperations.get_port_by_name(name)
    if port:
        print('%s: %s' % (port.name, str(port)))
    else:
        print('No such port')

def get_ports_by_uuid(bridge_name):
    bridge = BridgeOperations.get_bridge_by_name(bridge_name)
    if not bridge:
        print('No such bridge')
        return
    for port_uuid in bridge.ports:
        port = PortOperations.get_port_by_uuid(port_uuid)
        print('%s: %s' % (port.name, str(port)))