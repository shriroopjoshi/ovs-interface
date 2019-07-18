from operations.bridge_operations import BridgeOperations
from operations.open_vswitch_operations import Open_vSwitchOperations

def get_all_bridges():
    bridges = BridgeOperations.get_bridges()
    for bridge in bridges:
        print('%s: %s' % (bridge.name, str(bridge)))

def get_bridge_by_name(name):
    bridge = BridgeOperations.get_bridge_by_name(name)
    if bridge:
        print('%s: %s' % (bridge.name, str(bridge)))
    else:
        print('No such bridge')

def get_bridges_by_uuid():
    ovs = Open_vSwitchOperations.get()
    for bridge_uuid in ovs.bridges:
        bridge = BridgeOperations.get_bridge_by_uuid(bridge_uuid)
        print('%s: %s' % (bridge.name, str(bridge)))
