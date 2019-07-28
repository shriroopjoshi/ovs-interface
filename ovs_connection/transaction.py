import json
import socket
import threading
from contextlib import contextmanager

import constants
from ovs_connection.connection import OVSConnection
from ovs_exceptions.ovs_exceptions import OVSTransactionException
from util import Singleton

class TransactionLock(metaclass=Singleton):

    def __init__(self):
        self.__lock = threading.Lock()
        self.__counter = 0

    @contextmanager
    def lock(self):
        _lock = self.__lock.acquire(blocking=True, timeout=constants.TRANSACTION_TIMEOUT)
        yield _lock
        if _lock:
            self.__lock.release()

    @property
    def counter(self):
        self.__counter += 1
        return self.__counter % constants.ALLOWED_CONCURRENT_TRANSACTIONS

class Transaction(object):

    def __init__(self):
        self.__lock = TransactionLock()
        self.__request = {
            'method': constants.Method.transact.value,
            'params': [constants.OVSDB_NAME]
        }
        self.__response = dict()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.apply()

    @property
    def response(self):
        return self.__response.get('result')

    def _apply_trans(self, tid, conn):
        self.__request['id'] = tid
        try:
            conn.send(json.dumps(self.__request))
            self.__response = json.loads(conn.receive())
            while (self.__response.get('id') != tid):
                self.__response = json.loads(conn.receive())
        except socket.timeout:
            self.__response = {'error': 'connection timeout'}

    def add_request_payload(self, payload):
        self.__request['params'].append(payload)

    def apply(self):
        if self.__response:
            # Block applying same transaction after getting response
            return
        conn = OVSConnection()
        try:
            with TransactionLock().lock():
                self._apply_trans(TransactionLock().counter, conn)
        except (IOError, OSError):
            self.__response = {'error': 'IO error'}
        if self.__response['error']:
            raise OVSTransactionException(self.__response['error'].strip())
