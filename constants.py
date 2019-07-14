import enum

OVSDB_NAME = 'Open_vSwitch'

class OVSDBTables(enum.Enum):
    open_vswitch = 'Open_vSwitch'
    bridge = 'Bridge'
    port = 'Port'
    interface = 'Interface'

class Method(enum.Enum):
    transact = 'transact'

class Operations(enum.Enum):
    insert = 'insert'
    select = 'select'
    update = 'update'
    delete = 'delete'
