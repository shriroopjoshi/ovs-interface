import json
import uuid

class Open_vSwitch(object):

    def __init__(
            self, bridges=list(), cur_cfg=0, datapath_types=list(), db_version='',
            dpdk_initialized=False, dpdk_version='', external_ids=dict(), iface_types=list(),
            manager_options=list(), next_cfg=0, other_configs=dict(), ovs_version='', ssl=list(),
            statistics=dict(), system_type='', system_version='', uuid=''
        ):
        self.bridges = list(bridges)
        self.cur_cfg = cur_cfg
        self.datapath_types = list(datapath_types)
        self.db_version = db_version
        self.dpdk_initialized = dpdk_initialized
        self.dpdk_version = dpdk_version
        self.external_ids = dict(external_ids)
        self.iface_types = list(iface_types)
        self.manager_options = list(manager_options)
        self.next_cfg = next_cfg
        self.other_configs = dict(other_configs)
        self.ovs_version = ovs_version
        self.ssl = list(ssl)
        self.statistics = dict(statistics)
        self.system_type = system_type
        self.system_version = system_version
        self.uuid = uuid

    @property
    def bridges(self):
        return self.__bridges

    @bridges.setter
    def bridges(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('bridges can only be a list or set')
        for val in value:
            if (not isinstance(val, (str, uuid.UUID))):
                raise ValueError('bridge can only be UUID')
        self.__bridges = set([uuid.UUID(str(val)) for val in value])

    @property
    def cur_cfg(self):
        return self.__cur_cfg

    @cur_cfg.setter
    def cur_cfg(self, value):
        if (not isinstance(value, int)):
            raise ValueError('cur_cfg can only be int')
        self.__cur_cfg = int(value)

    @property
    def datapath_types(self):
        return self.__datapath_types

    @datapath_types.setter
    def datapath_types(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('datapath_types can only be a list or set')
        for val in value:
            if (not isinstance(val, str)):
                raise ValueError('datapath_type can only be str')
        self.__datapath_types = [str(val) for val in value]

    @property
    def db_version(self):
        return self.__db_version

    @db_version.setter
    def db_version(self, value):
        if (not isinstance(value, str)):
            raise ValueError('db_version can only be str')
        self.__db_version = str(value)

    @property
    def dpdk_initialized(self):
        return self.__dpdk_initialized

    @dpdk_initialized.setter
    def dpdk_initialized(self, value):
        if (not isinstance(value, bool)):
            raise ValueError('dpdk_initialized can only be bool')
        self.__dpdk_initialized = bool(value)

    @property
    def dpdk_version(self):
        return self.__dpdk_version

    @dpdk_version.setter
    def dpdk_version(self, value):
        if (not isinstance(value, str)):
            raise ValueError('dpdk_version can only be str')
        self.__dpdk_version = str(value)

    @property
    def external_ids(self):
        return self.__external_ids

    @external_ids.setter
    def external_ids(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('external_ids can only be dict')
        self.__external_ids = dict(value)

    @property
    def iface_types(self):
        return self.__iface_types

    @iface_types.setter
    def iface_types(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('iface_types can only be a list or set')
        self.__iface_types = set(value)

    @property
    def manager_options(self):
        return self.__manager_options

    @manager_options.setter
    def manager_options(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('manager_optiosn can only be a list or set')
        self.__manager_options = set(value)

    @property
    def next_cfg(self):
        return self.__next_cfg

    @next_cfg.setter
    def next_cfg(self, value):
        if (not isinstance(value, int)):
            raise ValueError('next_cfg can only be int')
        self.__next_cfg = int(value)

    @property
    def other_configs(self):
        return self.__other_configs

    @other_configs.setter
    def other_configs(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('other_configs can only be dict')
        self.__other_configs = dict(value)

    @property
    def ovs_version(self):
        return self.__ovs_version

    @ovs_version.setter
    def ovs_version(self, value):
        if (not isinstance(value, str)):
            raise ValueError('ovs_version can only be str')
        self.__ovs_version = str(value)

    @property
    def ssl(self):
        return self.__ssl

    @ssl.setter
    def ssl(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('ssl can only be a list or set')
        self.__ssl = set(value)

    @property
    def statistics(self):
        return self.__statistics

    @statistics.setter
    def statistics(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('statistics can only be dict')
        self.__statistics = dict(value)

    @property
    def system_type(self):
        return self.__system_type

    @system_type.setter
    def system_type(self, value):
        if (not isinstance(value, str)):
            raise ValueError('system_type can only be str')
        self.__system_type = str(value)

    @property
    def system_version(self):
        return self.__system_version

    @system_version.setter
    def system_version(self, value):
        if (not isinstance(value, str)):
            raise ValueError('system_version can only be str')
        self.__system_version = str(value)

    @property
    def uuid(self):
        return self.__uuid

    @uuid.setter
    def uuid(self, value):
        if (not isinstance(value, (uuid.UUID, str))):
            raise ValueError('uuid can only be str or uuid.UUID')
        self.__uuid = uuid.UUID(value)

    def __str__(self):
        return json.dumps({
            'bridges': [str(bridge) for bridge in self.bridges],
            'cur_cfg': self.cur_cfg,
            'datapath_types': list(self.datapath_types),
            'db_version': self.db_version,
            'dpdk_initialized': self.dpdk_initialized,
            'dpdk_version': self.dpdk_version,
            'external_ids': self.external_ids,
            'iface_types': list(self.iface_types),
            'manager_options': list(self.manager_options),
            'next_cfg': self.next_cfg,
            'other_configs': self.other_configs,
            'ovs_version': self.ovs_version,
            'ssl': list(self.ssl),
            'statistics': self.statistics,
            'system_type': self.system_type,
            'system_version': self.system_version,
            'uuid': str(self.uuid)
        })
