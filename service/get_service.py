from data.services_dicts import *


def get_service_by_callback(action):  # Получение категории и услуги
    if action.startswith('wd'):
        service = f"Веб-дизайн | {service_dict['wd_dict'][f'ss_{action}']}"
    elif action.startswith('p'):
        service = f"Полиграфия | {service_dict['p_dict'][f'ss_{action}']}"
    elif action.startswith('gp'):
        service = f"Графический дизайн | {service_dict['gp_dict'][f'ss_{action}']}"
    else:
        return None
    return service


def get_cost_by_callback(action):
    return cost_dict[action]


def get_speed_by_callback(action):
    return speed_dict[action]
