import os

def get_cpu_load():
    """ Returns a list CPU Loads"""
    result = []
    cmd = "WMIC CPU GET LoadPercentage "
    response = os.popen(cmd + ' 2>&1','r').read().strip().split("\r\n")
    for load in response[1:]:
       result.append(int(load))
    return result

if __name__ == '__main__':
    print get_cpu_load()


while 1:
    print get_cpu_load()
