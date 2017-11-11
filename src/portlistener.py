from bottle import HTTPError
from bottle import get, post
from bottle import request, run, static_file, HTTPResponse

from resources.global_resources.variables import *
from validation.validation import validate_service_details
from log.log import Log
from config.config_services import get_cfg_services, get_cfg_service, set_cfg_service_microservice

def start_bottle(self_port):

    _log = Log()

    ################################################################################################
    # Enable cross domain scripting
    ################################################################################################

    def enable_cors(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET'
        return response

    ################################################################################################
    # Get all service information
    ################################################################################################

    @get(uri_configServices)
    def get_services():
        try:
            #
            d = get_cfg_services()
            #
            if not bool(d):
                status = httpStatusFailure
            else:
                status = httpStatusSuccess
            #
            _log.new_entry(logCategoryClient, request['REMOTE_ADDR'], request.url, 'GET', status, level=logLevelInfo)
            #
            if isinstance(d, bool):
                return HTTPResponse(status=status)
            else:
                return HTTPResponse(body=str(d), status=status)
            #
        except Exception as e:
            status = httpStatusServererror
            _log.new_entry(logCategoryClient, request['REMOTE_ADDR'], request.url, 'GET', status, level=logLevelError)
            raise HTTPError(status)

    ################################################################################################
    # Get single service information (from id)
    ################################################################################################

    @get(uri_configService)
    def get_service(id):
        try:
            #
            d = get_cfg_service(id)
            #
            if not bool(d):
                status = httpStatusFailure
            else:
                status = httpStatusSuccess
            #
            _log.new_entry(logCategoryClient, request['REMOTE_ADDR'], request.url, 'GET', status, level=logLevelInfo)
            #
            if isinstance(d, bool):
                return HTTPResponse(status=status)
            else:
                return HTTPResponse(body=str(d), status=status)
            #
        except Exception as e:
            status = httpStatusServererror
            _log.new_entry(logCategoryClient, request['REMOTE_ADDR'], request.url, 'GET', status, level=logLevelError)
            raise HTTPError(status)

    ################################################################################################
    # Update config for service (from id)
    ################################################################################################

    @post(uri_configService)
    def post_service_details(service_id):
        try:
            #
            data_dict = request.json
            #
            if validate_service_details(data_dict):
                #
                r = set_cfg_service_microservice(service_id,
                                                 data_dict['ipaddress'],
                                                 data_dict['port'])
                #
                if r:
                    status = httpStatusFailure
                else:
                    status = httpStatusSuccess
            else:
                status = httpStatusBadrequest
            #
            _log.new_entry(logCategoryClient, request['REMOTE_ADDR'], request.url, 'POST', status, level=logLevelInfo)
            #
            return HTTPResponse(status=status)
            #
        except Exception as e:
            status = httpStatusServererror
            _log.new_entry(logCategoryClient, request['REMOTE_ADDR'], request.url, 'POST', status, level=logLevelError)
            raise HTTPError(status)

    ################################################################################################

    host='0.0.0.0'
    _log.new_entry(logCategoryProcess, '-', 'Port listener', '{host}:{port}'.format(host=host, port=self_port), 'started')
    run(host=host, port=self_port, debug=True)
