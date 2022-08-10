from bs4 import BeautifulSoup as bs
import requests
import time
import random
import threading
import operator
import os
from geo_lib import *


icao = ['uuww', 'ulli', 'urwa', 'uwkd', 'urml', 'uhww', 'urka', 'uiii', 'urss', 'usrr', 'umkk', 'uhmm', 'ulpb', 'uhpp']

def get_page(air1, air2):
    url = 'http://rfinder.asalink.net/free/autoroute_rtx.php'
    params_ = {'id1': air1, 'ic1': '', 'id2': air2, 'ic2': '', 'minalt': 'FL330', 'maxalt': 'FL330', 'lvl': 'B', 'dbid': '2207', 'usesid': 'Y', 'usestar': 'Y', 'easet': 'Y', 'rnav': 'Y', 'nats': 'R', 'k': '2033919939'}
    response = requests.post(url, data = params_).text
    return response


def get_arr_wpt(r):
    soup = bs(r, 'html.parser')
    p = soup.find('pre').text
    p = p.split('\n')
    p.pop(0)
    p.pop(len(p)-1)
    for i, val in enumerate(p):
        val = val.split()
        line = ''
        j = len(val) - 1
        while True:
            line = val[j] + ' ' + line
            val.pop(j)
            j -= 1
            if val[j].isalpha() == False and val[j] != '/' and val[j].find('/') == -1:
                val.append(line)
                break
        if len(val) != 7:
            val.insert(1, '---')
        p[i] = val
    return p

def twag(arr, dct):
    wpt_arr = []
    arr1 = angle_trans(arr[0][4], arr[0][5])
    wpt_arr.append('0.0 0.0')
    for i in range(0, len(arr)-1):
        arr2 = angle_trans(arr[i+1][4], arr[i+1][5])
        wpt_arr.append(trans(distance(arr1, arr2), azimuth(arr1, arr2), dct))
    return wpt_arr
        
def twac(arr):
    wpt_arr = []
    wpt_arr.append('0.0 0.0')
    for i in range(0, len(arr)-1):
        arr1 = angle_trans(arr[i][6], arr[i][7])
        arr2 = angle_trans(arr[i+1][6], arr[i+1][7])
        d = round(distance(arr1, arr2), 1)
        a = round(azimuth(arr1, arr2), 1)
        line = str(a) + ' ' + str(d)
        wpt_arr.append(line)
    return wpt_arr

def arr_of_wpt(air1, air2, hdg):   
    arr = get_arr_wpt(get_page(air1, air2))
    arr1 = twag(arr, hdg)
    for i, val in enumerate(arr):
        val.insert(4, arr1[i].split()[0])
        val.insert(5, arr1[i].split()[1])      
    arr1 = twac(arr)
    for i, val in enumerate(arr):
        val[2] = arr1[i].split()[0]
        val[3] = arr1[i].split()[1]
    return arr
