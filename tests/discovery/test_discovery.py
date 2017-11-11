from multiprocessing import Process
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname, gethostname
from src.resources.global_resources.variables import server_broadcastPort, server_broadcastCode
from src.discovery.broadcast import broadcast_service
from tests.discovery.testlist import testlist


def discover_server():
    s = socket(AF_INET, SOCK_DGRAM) # create UDP socket
    s.bind(('', server_broadcastPort))

    while True:
        data, addr = s.recvfrom(1024) # wait for a packet
        data = data.decode("utf-8")
        if data.startswith(server_broadcastCode):
            return data[len(server_broadcastCode):]


def my_ip():
    return gethostbyname(gethostname())


def run_test():
    for t in testlist:
        result = test_discover(t['port'])
        expect = my_ip() + ':' + str(t['port'])
        result_compare(t['id'], expect, result)


def test_discover(port):
    process_test_broadcast = Process(target=broadcast_service, args=(port,))
    process_test_broadcast.start()
    result = discover_server()
    process_test_broadcast.terminate()
    return result


def result_compare(id, expect, result):
    #
    str_result = 'PASS' if result==expect else 'FAIL'
    #
    print('Test #{id}::{str_result}::expected={expect}-v-result={result}'.format(id=id,
                                                                                 str_result=str_result,
                                                                                 expect=expect,
                                                                                 result=result))
