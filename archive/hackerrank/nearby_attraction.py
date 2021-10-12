#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tanchao'

import sys
import math

PI = 3.14159265359
EARTH_RADIUS = 6371  # in km
TRANSPORTS = {
    'metro': 20,
    'bike': 15,
    'foot': 5
}

'''
{'15': (52.357895, 4.892835), '14': (52.368832, 4.892744), '35': (52.342497, 4.855094),
'1': (52.378281, 4.90007), '3': (52.375737, 4.896547), '2': (52.373634, 4.890289),
'5': (52.376237, 4.90286), '4': (52.372995, 4.893096), '7': (52.366537, 4.911348),
'6': (52.367066, 4.893381)}
'''

def nearby_attraction(addresses, reqs):
    for req in reqs:
        req_point = req['location']
        req_trans = req['transport']
        req_time = req['time']
        req_addresses = {}
        for addr in addresses:
            req_addresses[addr['id']] = addr['location']
        res = ''
        while True:
            nearest = 10000000  # INT MAX
            near_id = ''
            for addr_id in req_addresses:
                addr_point = req_addresses[addr_id]
                distance = round(distance_between(req_point, addr_point), 2)  # round to 0.2f
                if nearest > distance or (nearest == distance and int(near_id) > int(addr_id)):
                    nearest = distance
                    near_id = addr_id
            time = float(nearest / TRANSPORTS[req_trans] * 60)
            req_time -= time
            req_point = req_addresses.pop(near_id)  # remove point travelled
            print req_addresses, '----->', near_id, req_point, nearest, req_time, time
            if req_time >= 0:
                res += str(near_id) + ' '
            else:
                break
            if not req_addresses:
                break
        print res.strip()


def nearby_attractions(addrs, reqs):
    for req in reqs:
        distances = []
        for addr in addrs:
            addr['distance'] = round(distance_between(req['location'], addr['location']), 2)  # round to 0.2f
            distances.append(addr)  # addrs with distances
        distances.append({'id': 0, 'location': req['location'], 'distance': 0.00})
        distances.sort(key=lambda distance: (distance['distance'], distance['id']))  # sort by id
        # print distances
        total_time, res = req['time'], ''
        # for d in distances:
        #     time = d['distance'] / TRANSPORTS[req['transport']] * 60  # minutes
        #     total_time -= time
        #     if total_time >= 0:
        #         res += str(d['id']) + ' '
        #     else:
        #         break
        for i in xrange(len(distances) - 1):
            j = i + 1
            d = round(distance_between(distances[j]['location'], distances[i]['location']), 2)
            time = d / TRANSPORTS[req['transport']] * 60  # minutes
            total_time -= time
            print distances[i], distances[j], d, time, total_time
            if total_time >= 0:
                res += str(distances[j]['id']) + ' '
            else:
                break
        print res.strip()


def distance_between(point1, point2):
    point1_lat_in_radians = degree2radians(point1[0])
    point1_long_in_radians = degree2radians(point1[1])
    point2_lat_in_radians = degree2radians(point2[0])
    point2_long_in_radians = degree2radians(point2[1])
    return float(math.acos(math.sin(point1_lat_in_radians) * math.sin(point2_lat_in_radians) +
                     math.cos(point1_lat_in_radians) * math.cos(point2_lat_in_radians) *
                     math.cos(point2_long_in_radians - point1_long_in_radians)) * EARTH_RADIUS)


def degree2radians(degree):
    return float(degree * 2 * PI / 360)


if __name__ == '__main__':
    arg = sys.argv[-1]  # get input file name
    addresses, reqs = [], []
    with open(arg, 'r') as input_file:
        n = int(input_file.readline())
        for i in xrange(n):
            line = input_file.readline()
            lines = line.split()
            address = {'id': int(lines[0]), 'location': (float(lines[1]), float(lines[2]))}
            addresses.append(address)
        m = int(input_file.readline())
        for i in xrange(m):
            line = input_file.readline()
            lines = line.split()
            req = {'location': (float(lines[0]), float(lines[1])), 'transport': lines[2], 'time': int(lines[3])}
            reqs.append(req)
    nearby_attraction(addresses, reqs)