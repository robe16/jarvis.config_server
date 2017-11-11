from portlistener import start_bottle
from resources.global_resources.variables import *
from log.log import Log

_log = Log()


try:

    _log.new_entry(logCategoryProcess, '-', 'Starting micro service', '-', 'starting')

    ################################
    # As micro service will be containerised, a hard-coded port (1600) will be
    # used, and this will be mapped to as part of container build/deployment.
    self_port = 1600

    ################################
    # Port_listener

    _log.new_entry(logCategoryProcess, '-', 'Port listener', 'port-{port}'.format(port=self_port), 'started')

    start_bottle(self_port)

    _log.new_entry(logCategoryProcess, '-', 'Port listener', '-'.format(port=self_port), 'stopped')

except Exception as e:
    _log.new_entry(logCategoryProcess, '-', 'Starting micro service', e, 'fail', level=logLevelError)
