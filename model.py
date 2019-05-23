""" OVSDB Models """

DB_NAME = 'Open_vSwitch'

class Bridge(object):

    DPDK_DATAPATH_TYPE = 'netdev'

    def __init__(self, name):
        self.__auto_attach = set()
        self.__controller = set()
        self.__datapath_id = ''
        self.__datapath_type = ''
        self.__datapath_version = tuple()
        self.__external_ids = dict()
        self.__fail_mode = set()
        self.__flood_vlans = set()
        self.__ipfix = set()
        self.__mcast_snooping_enable = False
        self.__mirrors = set()
        self.__name = name
        self.__netflow = set()
        self.__other_config = dict()
        self.__ports = set()
        self.__protocols = set()
        self.__rstp_enabled = False
        self.__rstp_status = dict()
        self.__sflow = set()
        self.__status = dict()
        self.__stp_enable = True
