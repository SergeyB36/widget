from widget import get_date

def filter_by_state(filter_list: list[dict], state='EXECUTED'):
    new_list_dict = []
    for i_dict in filter_list:
        if i_dict['state'] == state:
            new_list_dict.append(i_dict)
    return new_list_dict

def sort_by_date(sort_list, sort_key=False):
    sorted_list = sorted(sort_list, key=lambda sorted_key: sorted_key['date'][:10], reverse= sort_key)
    return sorted_list
