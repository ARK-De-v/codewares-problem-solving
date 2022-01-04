def number(bus_stops):
    r =0
    for i in bus_stops:
        r += i[0]-i[1]
    return r
