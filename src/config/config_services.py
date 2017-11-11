from config.config import get_config_json, write_config


def get_cfg_services():
    #
    return get_config_json('service')


def get_cfg_service(service_id):
    #
    data = get_cfg_services()
    #
    for service in data['services']:
        if service['id'] == service_id:
            return service
    #
    return False


def set_cfg_service_microservice(service_id, ip, port):
    #
    data = get_cfg_services()
    #
    for service in data['services']:
        if service['id'] == service_id:
            service['microservice']['ip'] = ip
            service['microservice']['port'] = port
            return write_config(data, 'service')
    #
    return False


def set_cfg_service_details(service_id, **kwargs):
    #
    data = get_cfg_services()
    #
    for service in data['services']:
        if service['id'] == service_id:
            for k, v in kwargs:
                service['details'][k] = v
            return write_config(data, 'service')
    #
    return False
