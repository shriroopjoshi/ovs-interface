# ovs-interface
A lightweight python client to interact with Open vSwitch. It enables your python application to programmatically communicate with OpenvSwitch instead of relying on weird hacks involving `subprocess` and `ovs-vsctl`.

# Get Started
Clone the repository and check the value of `OVSDB_SOCKET` in `constants.py`. It has to match the path of the ovs-db socket on your system. By default, the socket is located under `/var/run/openvswitch`. If you are using a different path, change the value of `OVSDB_SOCKET` accordingly.

Once that is set, you can check out the examples directory to get started!
