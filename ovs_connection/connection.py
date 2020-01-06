import json
import os
import socket

import constants
from util import Singleton


class OVSConnection(metaclass=Singleton):

    def __init__(self):
        if not os.path.exists(constants.OVSDB_SOCKET):
            raise RuntimeError('socket %s not found' % constants.OVSDB_SOCKET)
        self.connection_sock = socket.socket(family=socket.AF_UNIX, type=socket.SOCK_STREAM)
        self.connection_sock.connect(constants.OVSDB_SOCKET)
        self.connection_sock.settimeout(constants.OVSDB_CONNECTION_TIMEOUT)

    def __del__(self):
        try:
            self.connection_sock.close()
        except Exception:
            pass

    def send(self, payload):
        payload = payload.encode('ascii', 'replace')
        self.connection_sock.send(payload)

    def receive(self):
        response = b''
        while True:
            part_response = self.connection_sock.recv(constants.OVSDB_CONNECTION_BUFFER_SIZE)
            response += part_response
            if len(part_response) < constants.OVSDB_CONNECTION_BUFFER_SIZE:
                break
        return response

    def disconnect(self):
        self.connection_sock.close()


def test():
    """
        This def is intended for testing connection to OVSDB
        It should not be used for anything other than testing
    """
    echo_msg = {
        'method': 'echo',
        'params': ['test'],
        'id': 0
    }
    conn = OVSConnection()
    conn.send(json.dumps(echo_msg))
    resp = json.loads(conn.receive())
    if resp['error']:
        print('Failure')
    if (resp['id'] == 0 and resp['result'] == ['test']):
        print('Success')
    else:
        print('Failure')
