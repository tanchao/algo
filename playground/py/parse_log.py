import math
import statistics
from typing import Dict, List


REQ_STAT_DICT = {}
RECORDS = []
CPM_STAT = {
    'all_resp_time': [],
    'dyno_mode': []
}
CPM_RECORD = []
GET_CPM = 'GET /api/users/{user_id}/count_pending_messages'
GET_GM = 'GET /api/users/{user_id}/get_messages'
GET_GFP = 'GET /api/users/{user_id}/get_friends_progress'
GET_GFS = 'GET /api/users/{user_id}/get_friends_score'
POST = 'POST /api/users/{user_id}'
#GET /api/users/{user_id}


def get_req_id(info):
    if len(info) != 12: # validation
        return "" # unexpected
    #print(info[3])
    if 'POST' in info[3]:
        return POST
    else:
        if 'count_pending_messages' in info[4]:
            return GET_CPM
        # todo: else
    #print(info[4])


def aggregate(logs):
    if req_id == GET_CPM:
        response_time = extract_time(logs['connect']) + extract_time(logs['service'])
        dyno_mode = logs['dyno']
        CPM_STAT['all_resp_time'].append(response_time)
        CPM_STAT['dyno_mode'].append(dyno_mode)
    

def extract_time(timeInStr):
    num = timeInStr.replace('ms', '')
    return float(num)


def stat(req_id):
    result = {}
    if req_id == GET_CPM:
        result['request_identifier'] = GET_CPM
        result['called'] = len(CPM_STAT['all_resp_time'])
        result['response_time_mean'] = calc_mean(CPM_STAT['all_resp_time'])
        result['response_time_median'] = calc_median(CPM_STAT['all_resp_time'])
        result['dyno_mode'] = CPM_STAT['dyno_mode'][-1]
    return result


def calc_mean(times):
    return statistics.mean(times)


def calc_median(times):
    return statistics.median(times)


with open('random.log', 'r') as log_file:
    # inputs = log_file.read()
    lines = log_file.readlines()
    #print(len(lines))
    for line in lines:
        # print(line)
        info = line.split(' ')
        # print(len(info))
        # print(get_req_id(info))
        req_id = get_req_id(info)
        log = {}
        log['req_id'] = req_id
        for pair in info:
            if '=' in pair: # isKeyValPair
                k, v = pair.split('=')
                log[k] = v
            elif 'router' in pair: # isRouter
                log['router'] = pair
            elif 'T' in pair: # isTimestamp
                log['timestamp'] = pair
        RECORDS.append(log)
        aggregate(log)
    print(RECORDS)
    print(stat(GET_CPM))

"""
1. parse
1. store and aggregate for each type
1. stat from aggregation
"""