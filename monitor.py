from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import json, datetime

#todo: get from xml
hostname = 'appdynamics.com'
port = '443'

context = ssl.create_default_context()

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        data = ssock.getpeercert()
        expirationDate = data['notAfter']
        expirationDateDT = datetime.datetime.strptime(expirationDate, '%b  %d %H:%M:%S %Y %Z') 

now = datetime.datetime.today()
daysLeft = expirationDateDT - now

DEFAULT_METRIC_PREFIX="name=Custom Metrics|CertMonitor|" + base_url + "|Days Until Cert Expiration, value=" + str(daysLeft.days)

print(DEFAULT_METRIC_PREFIX)
