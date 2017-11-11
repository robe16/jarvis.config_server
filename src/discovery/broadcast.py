from time import sleep
from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST, gethostbyname, gethostname
from paramters import broadcast_frequency
from resources.global_resources.variables import server_broadcastPort, server_broadcastCode


def broadcast_service(host_port):
    s = socket(AF_INET, SOCK_DGRAM)  # create UDP socket
    s.bind(('', 0))
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)  # this is a broadcast socket
    my_ip = gethostbyname(gethostname())

    while True:
        data = server_broadcastCode + my_ip + ':' + str(host_port)
        data = bytes(data, "utf-8")
        s.sendto(data, ('<broadcast>', server_broadcastPort))
        sleep(broadcast_frequency)
