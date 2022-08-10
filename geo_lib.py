import math
import time

def angle_trans(angle1, angle2):
    arr = [angle1, angle2]
    for i, angle in enumerate(arr):
        angle = angle.replace('°', ' ').replace('\\', ' ').replace('\'', ' ').replace('\"', '')
        if angle[0] == 'S' or angle[0] == 'W':
            zn = -1
            angle = angle.replace('S', '').replace('W', '')
        else:
            zn = 1
            angle = angle.replace('N', '').replace('E', '')     
        d, m, s = map(float, angle.split())
        a_d = round(((d + m/60 + s/3600) * zn), 6)
        arr[i] = a_d
    return arr

def distance(arr1, arr2):
    r = 6371.009 #3963
    
    lat1, lng1 = math.radians(arr1[0]), math.radians(arr1[1])
    lat2, lng2 = math.radians(arr2[0]), math.radians(arr2[1])

    sin_lat1, cos_lat1 = math.sin(lat1), math.cos(lat1)
    sin_lat2, cos_lat2 = math.sin(lat2), math.cos(lat2)

    delta_lng = lng2 - lng1
    cos_delta_lng, sin_delta_lng = math.cos(delta_lng), math.sin(delta_lng)

    d = math.atan2(math.sqrt((cos_lat2 * sin_delta_lng) ** 2 + (cos_lat1 * sin_lat2 - sin_lat1 * cos_lat2 * cos_delta_lng) ** 2), sin_lat1 * sin_lat2 + cos_lat1 * cos_lat2 * cos_delta_lng)

    return d*r
    

def azimuth(arr1, arr2):

    lat1, lng1 = math.radians(arr1[0]), math.radians(arr1[1])
    lat2, lng2 = math.radians(arr2[0]), math.radians(arr2[1])
    
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1)*math.cos(lat2)*math.cos(lng2-lng1)
    y = math.sin(lng2-lng1)*math.cos(lat2)
    z = math.degrees(math.atan(-y/x))
    if x<0:
        z = z + 180

    z2 = (z+180)%360-180
    z2 = -math.radians(z2)

    anglerad2 = z2 -((2*math.pi)*math.floor((z2/(2*math.pi))))
    anglerad = anglerad2 * 180 / math.pi

    return anglerad

def trans(dist, azim, bear):
    angle = bear - azim
    x = round(-dist * math.sin(math.radians(angle)), 1)
    y = round( dist * math.cos(math.radians(angle)), 1)
    line = str(x) + ' ' + str(y)
    return line

