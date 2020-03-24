import enum

OVSDB_NAME = 'Open_vSwitch'

# connection constants
OVSDB_SOCKET = '/usr/local/var/run/openvswitch/db.sock'
OVSDB_CONNECTION_BUFFER_SIZE = 4096
OVSDB_CONNECTION_TIMEOUT = 2  # secs

# transaction constants
ALLOWED_CONCURRENT_TRANSACTIONS = 1024
# transaction timeout must always be greater than connection timeout
TRANSACTION_TIMEOUT = OVSDB_CONNECTION_TIMEOUT + 0.5  # sec


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
    mutate = 'mutate'
