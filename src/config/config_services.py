from config.config import get_config_json, write_config


def get_cfg_services():
    #
    return get_config_json('service')['services']


def get_cfg_service(id):
    #
    data = get_cfg_services()
    #
    for service in data:
        if service['id'] == id:
            return service
    #
    return False


def set_cfg_service_microservice(id, ip, port):
    #
    data = get_cfg_services()
    #
    for service in data:
        if service['id'] == id:
            service['microservice']['ip'] = ip
            service['microservice']['port'] = port
            return write_config(data, 'service')
    #
    raise Exception('Requested service id not found in config file')


def set_cfg_service_details(id, **kwargs):
    #
    data = get_cfg_services()
    #
    for service in data:
        if service['id'] == id:
            for k, v in kwargs:
                service['details'][k] = v
            return write_config(data, 'service')
    #
    raise Exception('Requested service id not found in config file')
