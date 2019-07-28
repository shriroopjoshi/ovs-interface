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

def update_external_ids(name, key, value):
    bridge = BridgeOperations.get_bridge_by_name(name)
    if not bridge:
            print('No such bridge')
            return

    bridge.external_ids[key] = value
    rows = BridgeOperations.update_bridge_by_name(bridge.name, bridge)
    print('Rows updated = %s' % rows)

    bridge = BridgeOperations.get_bridge_by_name(name)
    bridge.external_ids.pop(key)
    BridgeOperations.update_bridge_by_uuid(bridge.uuid, bridge)
    print('Rows updated = %s' % rows)

    bridge = BridgeOperations.get_bridge_by_name(name)
    assert key not in bridge.external_ids
