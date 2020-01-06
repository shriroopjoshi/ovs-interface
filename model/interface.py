import json
import uuid as _uuid


class Interface(object):

    def __init__(
        self, name, admin_state='', bfd=None, bfd_status=None, cfm_fault=None,
        cfm_fault_status=None, cfm_flap_count=None, cfm_health=None, cfm_mpid=None,
        cfm_remote_mpids=None, cfm_remote_opstate=None, duplex=None, error=None, external_ids=None,
        ifindex=-1, ingress_policing_burst=0, ingress_policing_rate=0, lacp_current=None,
        link_resets=-1, link_speed=None, link_state='', lldp=None, mac=None, mac_in_use='', mtu=0,
        mtu_request=None, ofport=0, ofport_request=None, options=None, other_config=None,
        statistics=None, status=None, type='', uuid=''
    ):
        self.admin_state = admin_state
        self.bfd = dict(bfd) if bfd else dict()
        self.bfd_status = dict(bfd_status) if bfd_status else dict()
        self.cfm_fault = set(cfm_fault) if cfm_fault else set()
        self.cfm_fault_status = set(cfm_fault_status) if cfm_fault_status else set()
        self.cfm_flap_count = set(cfm_flap_count) if cfm_flap_count else set()
        self.cfm_health = set(cfm_health) if cfm_health else set()
        self.cfm_mpid = set(cfm_mpid) if cfm_mpid else set()
        self.cfm_remote_mpids = set(cfm_remote_mpids) if cfm_remote_mpids else set()
        self.cfm_remote_opstate = set(cfm_remote_opstate) if cfm_remote_opstate else set()
        self.duplex = set(duplex) if duplex else set()
        self.error = set(error) if error else set()
        self.external_ids = dict(external_ids) if external_ids else dict()
        self.ifindex = ifindex
        self.ingress_policing_burst = ingress_policing_burst
        self.ingress_policing_rate = ingress_policing_rate
        self.lacp_current = set(lacp_current) if lacp_current else set()
        self.link_resets = link_resets
        self.link_speed = set(link_speed) if link_speed else set()
        self.link_state = link_state
        self.lldp = dict(lldp) if lldp else dict()
        self.mac = set(mac) if mac else set()
        self.mac_in_use = mac_in_use
        self.mtu = mtu
        self.mtu_request = set(mtu_request) if mtu_request else set()
        self.name = name
        self.ofport = ofport
        self.ofport_request = set(ofport_request) if ofport_request else set()
        self.options = dict(options) if options else dict()
        self.other_config = dict(other_config) if other_config else dict()
        self.statistics = dict(statistics) if statistics else dict()
        self.status = dict(status) if status else dict()
        self.type = type
        self.uuid = uuid if uuid else str(_uuid.uuid4())

    @property
    def admin_state(self):
        return self.__admin_state

    @admin_state.setter
    def admin_state(self, value):
        if (not isinstance(value, str)):
            raise ValueError('admin_state can only be a str')
        self.__admin_state = value

    @property
    def bfd(self):
        return self.__bfd

    @bfd.setter
    def bfd(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('bfd can only be a dict')
        self.__bfd = dict(value)

    @property
    def bfd_status(self):
        return self.__bfd_status

    @bfd_status.setter
    def bfd_status(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('bfd_status can only be a dict')
        self.__bfd_status = dict(value)

    @property
    def cfm_fault(self):
        return self.__cfm_fault

    @cfm_fault.setter
    def cfm_fault(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('cfm_fault can only be a list or a set')
        self.__cfm_fault = set(value)

    @property
    def cfm_fault_status(self):
        return self.__cfm_fault_status

    @cfm_fault_status.setter
    def cfm_fault_status(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('cfm_fault_status can only be a list or a set')
        self.__cfm_fault_status = set(value)

    @property
    def cfm_flap_count(self):
        return self.__cfm_flap_count

    @cfm_flap_count.setter
    def cfm_flap_count(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('cfm_flap_count can only be a list or a set')
        self.__cfm_flap_count = set(value)

    @property
    def cfm_health(self):
        return self.__cfm_health

    @cfm_health.setter
    def cfm_health(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('cfm_health can only be a list or a set')
        self.__cfm_health = set(value)

    @property
    def cfm_mpid(self):
        return self.__cfm_mpid

    @cfm_mpid.setter
    def cfm_mpid(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('cfm_mpid can only be a list or a set')
        self.__cfm_mpid = set(value)

    @property
    def cfm_remote_mpids(self):
        return self.__cfm_remote_mpids

    @cfm_remote_mpids.setter
    def cfm_remote_mpids(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('cfm_remote_mpids can only be a list or a set')
        self.__cfm_remote_mpids = set(value)

    @property
    def cfm_remote_opstate(self):
        return self.__cfm_remote_opstate

    @cfm_remote_opstate.setter
    def cfm_remote_opstate(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('cfm_remote_opstate can only be a list or a set')
        self.__cfm_remote_opstate = set(value)

    @property
    def duplex(self):
        return self.__duplex

    @duplex.setter
    def duplex(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('duplex can only be a list or a set')
        self.__duplex = set(value)

    @property
    def error(self):
        return self.__error

    @error.setter
    def error(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('error can only be a list or a set')
        self.__error = set(value)

    @property
    def external_ids(self):
        return self.__external_ids

    @external_ids.setter
    def external_ids(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('external_ids can only be a dict')
        self.__external_ids = dict(value)

    @property
    def ifindex(self):
        return self.__ifindex

    @ifindex.setter
    def ifindex(self, value):
        if (not isinstance(value, int)):
            raise ValueError('ifindex can only be int')
        self.__ifindex = value

    @property
    def ingress_policing_burst(self):
        return self.__ingress_policing_burst

    @ingress_policing_burst.setter
    def ingress_policing_burst(self, value):
        if (not isinstance(value, int)):
            raise ValueError('ingress_policing_burst can only be int')
        self.__ingress_policing_burst = value

    @property
    def ingress_policing_rate(self):
        return self.__ingress_policing_rate

    @ingress_policing_rate.setter
    def ingress_policing_rate(self, value):
        if (not isinstance(value, (float, int))):
            raise ValueError('ingress_policing_rate can only be float')
        self.__ingress_policing_rate = value * 1.0

    @property
    def lacp_current(self):
        return self.__lacp_current

    @lacp_current.setter
    def lacp_current(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('lacp_current can only be a list or a set')
        self.__lacp_current = set(value)

    @property
    def link_resets(self):
        return self.__link_resets

    @link_resets.setter
    def link_resets(self, value):
        if (not isinstance(value, int)):
            raise ValueError('link_resets can only be int')
        self.__link_resets = value

    @property
    def link_speed(self):
        return self.__link_speed

    @link_speed.setter
    def link_speed(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('link_speed can only be a list or a set')
        self.__link_speed = set(value)

    @property
    def link_state(self):
        return self.__link_state

    @link_state.setter
    def link_state(self, value):
        if (not isinstance(value, str)):
            raise ValueError('link_state can only be a str')
        self.__link_state = value

    @property
    def lldp(self):
        return self.__lldp

    @lldp.setter
    def lldp(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('lldp can only be a dict')
        self.__lldp = dict(value)

    @property
    def mac(self):
        return self.__mac

    @mac.setter
    def mac(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('mac can only be a list or a set')
        self.__mac = set(value)

    @property
    def mac_in_use(self):
        return self.__mac_in_use

    @mac_in_use.setter
    def mac_in_use(self, value):
        if (not isinstance(value, str)):
            raise ValueError('mac_in_use can only be a str')
        self.__mac_in_use = value

    @property
    def mtu(self):
        return self.__mtu

    @mtu.setter
    def mtu(self, value):
        if (not isinstance(value, int)):
            raise ValueError('mtu can only be a int')
        self.__mtu = value

    @property
    def mtu_request(self):
        return self.__mtu_request

    @mtu_request.setter
    def mtu_request(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('mtu_request can only be a list or a set')
        self.__mtu_request = set(value)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if (not isinstance(value, str)):
            raise ValueError('name can only be a str')
        self.__name = value

    @property
    def ofport(self):
        return self.__ofport

    @ofport.setter
    def ofport(self, value):
        if (not isinstance(value, int)):
            raise ValueError('ofport can only be an int')
        self.__ofport = value

    @property
    def ofport_request(self):
        return self.__ofport_request

    @ofport_request.setter
    def ofport_request(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('ofport_request can only be a list or a set')
        self.__ofport_request = set(value)

    @property
    def options(self):
        return self.__options

    @options.setter
    def options(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('options can only be a dict')
        self.__options = dict(value)

    @property
    def other_config(self):
        return self.__other_config

    @other_config.setter
    def other_config(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('other_config can only be a dict')
        self.__other_config = dict(value)

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
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if (not isinstance(value, str)):
            raise ValueError('type can only be a str')
        self.__type = value

    @property
    def uuid(self):
        return self.__uuid

    @uuid.setter
    def uuid(self, value):
        if (not isinstance(value, str)):
            raise ValueError('uuid can only be str')
        self.__uuid = uuid.UUID(value)

    def __str__(self):
        return json.dumps({
            'admin_state': self.admin_state,
            'bfd': self.bfd,
            'bfd_status': self.bfd_status,
            'cfm_fault': list(self.cfm_fault),
            'cfm_fault_status': list(self.cfm_fault_status),
            'cfm_flap_count': list(self.cfm_flap_count),
            'cfm_health': list(self.cfm_health),
            'cfm_mpids': list(self.cfm_mpid),
            'cfm_remote_mpids': list(self.cfm_remote_mpids),
            'cfm_remote_opstate': list(self.cfm_remote_opstate),
            'duplex': list(self.duplex),
            'error': list(self.error),
            'external_ids': self.external_ids,
            'ifindex': self.ifindex,
            'ingress_policing_burst': self.ingress_policing_burst,
            'ingress_policing_rate': self.ingress_policing_rate,
            'lacp_current': list(self.lacp_current),
            'link_resets': self.link_resets,
            'link_speed': list(self.link_speed),
            'link_state': self.link_state,
            'lldp': self.lldp,
            'mac': list(self.mac),
            'mac_in_use': self.mac_in_use,
            'mtu': self.mtu,
            'mtu_request': list(self.mtu_request),
            'name': self.name,
            'ofport': self.ofport,
            'ofport_request': list(self.ofport_request),
            'options': self.options,
            'other_config': self.other_config,
            'statistics': self.statistics,
            'status': self.status,
            'type': self.type,
            'uuid': str(self.uuid)
        })
