from __future__ import print_function

import json
import socket

import constants

class OVSConnection():

    HOST = '/usr/local/var/run/openvswitch/db.sock'
    BUFF_SIZE = 1024

    def __init__(self):
        self.connection_sock = socket.socket(family=socket.AF_UNIX, type=socket.SOCK_STREAM)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        self.disconnect()

    def connect(self):
        self.connection_sock.connect(OVSConnection.HOST)

    def send(self, payload):
        payload = payload.encode('ascii', 'replace')
        self.connection_sock.send(payload)

    def receive(self):
        response = b''
        while True:
            part_response = self.connection_sock.recv(OVSConnection.BUFF_SIZE)
            response += part_response
            if len(part_response) < OVSConnection.BUFF_SIZE:
                break
        return response

    def disconnect(self):
        self.connection_sock.close()

class TransactionID():

    __NUMBER_OF_CONCURRENT_TRANSACTIONS = 128
    __counter = 0

    @classmethod
    def id(cls):
        cls.__counter += 1
        return cls.__counter % cls.__NUMBER_OF_CONCURRENT_TRANSACTIONS

class TransactionHandle(object):

    def __init__(self):
        self.__transaction_id = TransactionID.id()
        self.__request_payload = {
            'id': self.transaction_id,
            'method': constants.Method.transact.value,
            'params': [constants.OVSDB_NAME]
        }
        self.__response = dict()

    @property
    def transaction_id(self):
        return self.__transaction_id

    @property
    def response(self):
        return self.__response

    def add_request(self, request):
        self.__request_payload['params'].append(request)

    def apply_transaction(self):
        with OVSConnection() as connection:
            connection.send(json.dumps(self.__request_payload))
            self.__response = json.loads(connection.receive())
            #TODO Make sure ID is same in request and response
        

def main():
    echo_msg = {
        'method': 'echo',
        'params': ['Test'],
        'id': 0
    }
    with OVSConnection() as conn:
        conn.send(json.dumps(echo_msg))
        print(conn.receive())
