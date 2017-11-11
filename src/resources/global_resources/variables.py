serviceName = 'Jarvis: Config Server'
deviceName = 'config_server'

logFileName = 'config_server'
logFileNameTimeformat = '%Y-%m-%d'

logLevelUnset = 'unset'
logLevelDebug = 'debug'
logLevelInfo = 'info'
logLevelWarning = 'warning'
logLevelError = 'error'
logLevelCritical = 'critical'

logCategoryClient = 'client request'
logCategoryProcess = 'process'

timeformat = '%Y/%m/%d %H.%M.%S.%f'

uri_configServices = 'config/services'
uri_configService = '/config/service/<id>'

httpStatusSuccess = 200
httpStatusBadrequest = 400
httpStatusForbidden = 404
httpStatusFailure = 420
httpStatusServererror = 500

# As micro service will be containerised, a hard-coded port (1600) will be
# used, and this will be mapped to as part of container build/deployment.
self_port = 1600

server_broadcastPort = 5000
server_broadcastCode = "jarvis_server"
