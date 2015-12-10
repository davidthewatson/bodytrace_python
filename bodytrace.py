import ssl
import requests
import datetime

# Check the version of OPENSSL this code will fail with OPENSSL < 1.0
print ssl.OPENSSL_VERSION

URI = open('uri.txt').read().strip()
IMEI_LIST = [imei.strip() for imei in open('imei_list.txt').readlines()]
auth = tuple(auth.strip() for auth in open('auth.txt').readlines())
responses = []

for imei in IMEI_LIST:
    r = requests.get(str.format(URI, imei), auth=auth)
    if r.status_code == 200:
        responses.append((imei, r))
    else:
        print str.format('Bad Status Code: {} for IMEI: {}',
                         r.status_code,
                         imei)

for (imei, r) in responses:
    print
    json = r.json()
    for ms_since_epoch in json:
        dt = datetime.datetime.fromtimestamp(float(ms_since_epoch)/1000)
        try:
            battery_voltage = json[ms_since_epoch]['batteryVoltage']
            signal_strength = json[ms_since_epoch]['signalStrength']
            weight = json[ms_since_epoch]['values']['weight'] * 0.00220462
        except KeyError as e:
            print "Key error({0}): {1}".format(e.errno, e.strerror)
            continue
        print imei, dt, battery_voltage, signal_strength, weight
