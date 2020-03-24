""" Bridge Model """
import json
import uuid as _uuid


class Bridge(object):

    def __init__(
        self, name, auto_attach=list(), controller=list(), datapath_id='', datapath_type='',
        datapath_version='', external_ids=dict(), fail_mode=list(), flood_vlans=list(),
        ipfix=list(), mcast_snooping_enable=False, mirrors=list(), netflow=list(),
        other_config=dict(), ports=list(), protocols=list(), rstp_enable=False,
        rstp_status=dict(), sflow=list(), status=dict(), stp_enable=True, uuid=''
    ):
        self.auto_attach = set(auto_attach) if auto_attach else set()
        self.controller = set(controller) if controller else set()
        self.datapath_id = datapath_id
        self.datapath_type = datapath_type
        self.datapath_version = datapath_version
        self.external_ids = dict(external_ids) if external_ids else dict()
        self.fail_mode = set(fail_mode) if fail_mode else set()
        self.flood_vlans = set(flood_vlans) if flood_vlans else set()
        self.ipfix = set(ipfix) if ipfix else set()
        self.mcast_snooping_enable = mcast_snooping_enable
        self.mirrors = set(mirrors) if mirrors else set()
        self.name = name
        self.netflow = set(netflow) if netflow else set()
        self.other_config = dict(other_config) if other_config else dict()
        self.ports = set(ports) if ports else set()
        self.protocols = set(protocols) if protocols else set()
        self.rstp_enable = rstp_enable
        self.rstp_status = dict(rstp_status) if rstp_status else dict()
        self.sflow = set(sflow) if sflow else set()
        self.status = dict(status) if status else dict()
        self.stp_enable = stp_enable
        self.uuid = uuid if uuid else str(_uuid.uuid4())

    @property
    def auto_attach(self):
        return self.__auto_attach

    @auto_attach.setter
    def auto_attach(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('auto_attach can only be a list or a set')
        self.__auto_attach = set(value)

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('controller can only be a list or a set')
        self.__controller = set(value)

    @property
    def datapath_id(self):
        return self.__datapath_id

    @datapath_id.setter
    def datapath_id(self, value):
        if (not isinstance(value, str)):
            raise ValueError('datapath_id can only be a string')
        self.__datapath_id = value

    @property
    def datapath_type(self):
        return self.__datapath_type

    @datapath_type.setter
    def datapath_type(self, value):
        if (not isinstance(value, str)):
            raise ValueError('datapath_type can only be a string')
        self.__datapath_type = value

    @property
    def datapath_version(self):
        return self.__datapath_version

    @datapath_version.setter
    def datapath_version(self, value):
        if (not isinstance(value, str)):
            raise ValueError('datapath_verion can only be a string')
        self.__datapath_version = str(value)

    @property
    def external_ids(self):
        return self.__external_ids

    @external_ids.setter
    def external_ids(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('external_ids can only be a dict')
        self.__external_ids = dict(value)

    @property
    def fail_mode(self):
        return self.__fail_mode

    @fail_mode.setter
    def fail_mode(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('fail_mode can only be a list or a set')
        self.__fail_mode = value

    @property
    def flood_vlans(self):
        return self.__flood_vlans

    @flood_vlans.setter
    def flood_vlans(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('flood_vlans can only be a list or a set')
        self.__flood_vlans = set(value)

    @property
    def ipfix(self):
        return self.__ipfix

    @ipfix.setter
    def ipfix(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('ipfix can only be a list or a set')
        self.__ipfix = set(value)

    @property
    def mcast_snooping_enable(self):
        return self.__mcast_snooping_enable

    @mcast_snooping_enable.setter
    def mcast_snooping_enable(self, value):
        if (not isinstance(value, bool)):
            raise ValueError('mcast_snooping_error can only be a bool')
        self.__mcast_snooping_enable = value

    @property
    def mirrors(self):
        return self.__mirrors

    @mirrors.setter
    def mirrors(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('mirrors can only be a list or a set')
        self.__mirrors = set(value)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if (not isinstance(value, str)):
            raise ValueError('name can only be a string')
        self.__name = str(value)

    @property
    def netflow(self):
        return self.__netflow

    @netflow.setter
    def netflow(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('netflow can only be a list or a set')
        self.__netflow = set(value)

    @property
    def other_config(self):
        return self.__other_config

    @other_config.setter
    def other_config(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('other_config can only be a dict')
        self.__other_config = dict(value)

    @property
    def ports(self):
        return self.__ports

    @ports.setter
    def ports(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('ports can only be a list or a set')
        for val in value:
            if (not isinstance(val, (str, _uuid.UUID))):
                raise ValueError('port need to a instances of str')
        self.__ports = set([_uuid.UUID(str(val)) for val in value])

    @property
    def protocols(self):
        return self.__protocols

    @protocols.setter
    def protocols(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('protocols can only be a list or a set')
        self.__protocols = set(value)

    @property
    def rstp_enable(self):
        return self.__rstp_enabled

    @rstp_enable.setter
    def rstp_enable(self, value):
        if (not isinstance(value, bool)):
            raise ValueError('rstp_enable can only be a bool')
        self.__rstp_enabled = value

    @property
    def rstp_status(self):
        return self.__rstp_status

    @rstp_status.setter
    def rstp_status(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('rstp_status can only be a dict')
        self.__rstp_status = value

    @property
    def sflow(self):
        return self.__sflow

    @sflow.setter
    def sflow(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('sflow can only be a list or a dict')
        self.__sflow = set(value)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('status can only be a dict')
        self.__status = value

    @property
    def stp_enable(self):
        return self.__stp_enable

    @stp_enable.setter
    def stp_enable(self, value):
        if (not isinstance(value, bool)):
            raise ValueError('status can only be a boolean')
        self.__stp_enable = value

    @property
    def uuid(self):
        return self.__uuid

    @uuid.setter
    def uuid(self, value):
        if (not isinstance(value, str)):
            raise ValueError('uuid can only be str')
        self.__uuid = _uuid.UUID(value)

    def __str__(self):
        return json.dumps({
            'auto_attach': list(self.auto_attach),
            'controller': list(self.controller),
            'datapath_id': self.datapath_id,
            'datapath_type': self.datapath_type,
            'datapath_version': self.datapath_version,
            'external_ids': self.external_ids,
            'fail_mode': list(self.fail_mode),
            'flood_vlans': list(self.flood_vlans),
            'ipfix': list(self.ipfix),
            'mcast_snooping_enable': self.mcast_snooping_enable,
            'mirrors': list(self.mirrors),
            'name': self.name,
            'netflow': list(self.netflow),
            'other_config': self.other_config,
            'ports': [str(port) for port in self.ports],
            'protocols': list(self.protocols),
            'rstp_enable': self.rstp_enable,
            'sflow': list(self.sflow),
            'status': self.status,
            'stp_enable': self.stp_enable,
            'uuid': str(self.uuid)
        })
