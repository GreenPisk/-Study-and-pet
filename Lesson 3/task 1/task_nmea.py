from math import radians, cos, sin, asin, sqrt

def input_data():
    konserv = open('nmea.log', 'r')
    return konserv


def haversine(lon2,lat2):
    lon1 = 30.300509
    lat1 = 60.051584
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def file_len():
    with open('nmea.log') as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def time_dolg_shir():
    konserv = input_data()
    data = konserv.readlines()
    dict_info_poss= {}
    for i in range(int(file_len())):
        if len(data[i]) == 80:
            time = data[i][7:16]
            lat = data[i][17:29]
            lat = dolg_shir_in_gradus(lat)
            lon = data[i][33:45]
            lon = dolg_shir_in_gradus(lon)
            dict_info_poss[i] = [time,lat, lon]
    return dict_info_poss


def dolg_shir_in_gradus(name):
    name = name.replace(".", "")
    name = name[:2] + '.' + name[3:]
    In_gradus = float(name[1:])/60
    name = float(name[:1] + str(In_gradus))
    name = float('{:.6f}'.format(name))
    return name


def treatment_konserv():
    info_poss = time_dolg_shir()
    j = 0
    for i in info_poss:
            if (haversine(info_poss[i][2], info_poss[i][1])) <= 25:
                print(info_poss[i][0])
                j += 1
    time = j * 0.20
    print("В течении ", time, 'мс робот находился в близи указаных координат')

if __name__ == '__main__':
    treatment_konserv()

