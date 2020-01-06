from operations.open_vswitch_operations import Open_vSwitchOperations


def get():
    ovs = Open_vSwitchOperations.get()
    print(str(ovs))


def update():
    ovs = Open_vSwitchOperations.get()
    ovs.external_ids['mykey'] = 'myvalue'
    print('Rows updated = %s' % Open_vSwitchOperations.update(ovs))
    ovs = Open_vSwitchOperations.get()
    ovs.external_ids.pop('mykey')
    print('Rows updated = %s' % Open_vSwitchOperations.update(ovs))
