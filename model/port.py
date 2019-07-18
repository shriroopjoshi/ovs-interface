import json
import uuid

class Port(object):

    def __init__(
            self, name, bond_active_slave=list(), bond_downdelay=0, bond_fake_iface=False,
            bond_mode=list(), bond_updelay=0, cvlans=list(), external_ids=dict(),
            fake_bridge=False, interfaces=list(), lacp=list(), mac=list(), other_config=dict(),
            protected=False, qos=list(), rstp_statistics=dict(), rstp_status=dict(),
            statistics=dict(), status=dict(), tag=list(), trunks=list(), vlan_mode=list(), uuid=''
        ):
        self.name = name
        self.bond_active_slave = set(bond_active_slave)
        self.bond_downdelay = bond_downdelay
        self.bond_fake_iface = bond_fake_iface
        self.bond_mode = set(bond_mode)
        self.bond_updelay = bond_updelay
        self.cvlans = set(cvlans)
        self.external_ids = dict(external_ids)
        self.fake_bridge = fake_bridge
        self.interfaces = set(interfaces)
        self.lacp = set(lacp)
        self.mac = set(mac)
        self.other_config = dict(other_config)
        self.protected = protected
        self.qos = set(qos)
        self.rstp_statistics = dict(rstp_statistics)
        self.rstp_status = dict(rstp_status)
        self.statistics = dict(statistics)
        self.status = dict(status)
        self.tag = set(tag)
        self.trunks = set(trunks)
        self.vlan_mode = set(vlan_mode)
        self.uuid = uuid

    @property
    def bond_active_slave(self):
        return self.__bond_active_slave

    @bond_active_slave.setter
    def bond_active_slave(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('bond_active_state can only be list or set')
        self.__bond_active_slave = set(value)

    @property
    def bond_downdelay(self):
        return self.__bond_downdelay

    @bond_downdelay.setter
    def bond_downdelay(self, value):
        if (not isinstance(value, int)):
            raise ValueError('bond_downdelay can only be int')
        self.__bond_downdelay = value

    @property
    def bond_fake_iface(self):
        return self.__bond_fake_iface

    @bond_fake_iface.setter
    def bond_fake_iface(self, value):
        if (not isinstance(value, bool)):
            raise ValueError('bond_fake_iface can only be bool')
        self.__bond_fake_iface = value

    @property
    def bond_mode(self):
        return self.__bond_mode

    @bond_mode.setter
    def bond_mode(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('bond_mode can only be a list or a set')
        self.__bond_mode = set(value)

    @property
    def bond_updelay(self):
        return self.__bond_updelay

    @bond_updelay.setter
    def bond_updelay(self, value):
        if (not isinstance(value, int)):
            raise ValueError('bond_updelay can only be int')
        self.__bond_updelay = value

    @property
    def cvlans(self):
        return self.__cvlans

    @cvlans.setter
    def cvlans(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('cvlans can only be a list or a set')
        self.__cvlans = set(value)

    @property
    def external_ids(self):
        return self.__external_ids

    @external_ids.setter
    def external_ids(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('external_ids can only be a dict')
        self.__external_ids = dict(value)

    @property
    def fake_bridge(self):
        return self.__fake_bridge

    @fake_bridge.setter
    def fake_bridge(self, value):
        if (not isinstance(value, bool)):
            raise ValueError('fake_bridge can only be a bool')
        self.__fake_bridge = value

    @property
    def interfaces(self):
        return self.__interfaces

    @interfaces.setter
    def interfaces(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('interfaces can only be a list or a set')
        for val in value:
            if (not isinstance(val, (str, uuid.UUID))):
                raise ValueError('interface can only be UUID')
        self.__interfaces = set(value)

    @property
    def lacp(self):
        return self.__lacp

    @lacp.setter
    def lacp(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('lacp can only be a list or a set')
        self.__lacp = set(value)

    @property
    def mac(self):
        return self.__mac

    @mac.setter
    def mac(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('mac can only be a list or a set')
        self.__mac = set(value)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if (not isinstance(value, str)):
            raise ValueError('name can only be a str')
        self.__name = value

    @property
    def other_config(self):
        return self.__other_config

    @other_config.setter
    def other_config(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('other_config can only be a dict')
        self.__other_config = dict(value)

    @property
    def protected(self):
        return self.__protected

    @protected.setter
    def protected(self, value):
        if (not isinstance(value, (bool))):
            raise ValueError('protected can only be bool')
        self.__protected = value

    @property
    def qos(self):
        return self.__qos

    @qos.setter
    def qos(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('qos can only be a list or a set')
        self.__qos = set(value)

    @property
    def rstp_statistics(self):
        return self.__rstp_statistics

    @rstp_statistics.setter
    def rstp_statistics(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('rstp_statistics can only be a dict')
        self.__rstp_statistics = dict(value)

    @property
    def rstp_status(self):
        return self.__rstp_status

    @rstp_status.setter
    def rstp_status(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('rstp_status can only be a dict')
        self.__rstp_status = dict(value)

    @property
    def statistics(self):
        return self.__statistics

    @statistics.setter
    def statistics(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('statistics can only be a dict')
        self.__statistics = dict(value)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('status can only be a dict')
        self.__status = dict(value)

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('tag can only be a list or a set')
        self.__tag = set(value)

    @property
    def trunks(self):
        return self.__trunks

    @trunks.setter
    def trunks(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('trunks can only be a list or a set')
        self.__trunks = set(value)

    @property
    def vlan_mode(self):
        return self.__vlan_mode

    @vlan_mode.setter
    def vlan_mode(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('vlan_mode can only be a list or a set')
        self.__vlan_mode = set(value)

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
            'name': self.name,
            'bond_active_slave': list(self.bond_active_slave),
            'bond_downdelay': self.bond_downdelay,
            'bond_fake_iface': self.bond_fake_iface,
            'bond_mode': list(self.bond_mode),
            'bond_updelay': self.bond_updelay,
            'cvlans': list(self.cvlans),
            'external_ids': self.external_ids,
            'fake_bridge': self.fake_bridge,
            'interfaces': list(self.interfaces),
            'lacp': list(self.lacp),
            'mac': list(self.mac),
            'other_config': list(self.other_config),
            'protected': self.protected,
            'qos': list(self.qos),
            'rstp_statistics': self.rstp_statistics,
            'rstp_status': self.rstp_status,
            'statistics': self.statistics,
            'status': self.status,
            'tag': list(self.tag),
            'trunks': list(self.trunks),
            'vlan_mode': list(self.vlan_mode),
            'uuid': str(self.uuid)
        })