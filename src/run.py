import sys
from multiprocessing import Process
from discovery.broadcast import broadcast_service
from portlistener import start_bottle
from resources.global_resources.variables import *
from log.log import Log

_log = Log()


try:

    ################################
    # Receive sys arguments

    # Argument 1: Port application listens on
    try:
        self_port = sys.argv[1]
    except:
        raise Exception('self_port not available')

    # Argument 2: Port of self exposed on host
    try:
        host_port = sys.argv[2]
    except:
        raise Exception('host_port not available')

    _log.new_entry(logCategoryProcess, '-', 'Starting micro service', '-', 'starting')

    ################################
    # Receive sys arguments

    _log.new_entry(logCategoryProcess, '-', 'Service discovery broadcaster',
                   'port-{port}'.format(port=server_broadcastPort), 'starting')

    process_broadcast = Process(target=broadcast_service, args=(host_port,))
    process_broadcast.start()

    _log.new_entry(logCategoryProcess, '-', 'Service discovery broadcaster',
                   'port-{port}'.format(port=server_broadcastPort), 'started')


    ################################
    # Port_listener

    _log.new_entry(logCategoryProcess, '-', 'Port listener', 'port-{port}'.format(port=self_port), 'started')

    start_bottle(self_port)

    _log.new_entry(logCategoryProcess, '-', 'Port listener', '-'.format(port=self_port), 'stopped')

except Exception as e:
    _log.new_entry(logCategoryProcess, '-', 'Starting micro service', e, 'fail', level=logLevelError)
