import enum

OVSDB_NAME = 'Open_vSwitch'

class Method(enum.Enum):
    transact = 'transact'

class Operations(enum.Enum):
    insert = 'insert'
    select = 'select'
    update = 'update'
    delete = 'delete'
