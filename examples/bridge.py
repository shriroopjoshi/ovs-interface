from operations.bridge_operations import BridgeOperations

def get_bridges():
    bridges = BridgeOperations.get_bridges()
    for bridge in bridges:
        print('%s: %s' % (bridge.name, str(bridge)))

def get_bridge_by_name(name):
    bridge = BridgeOperations.get_bridge_by_name(name)
    print('%s: %s' % (bridge.name, str(bridge)))
