from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import json, datetime
import xml.etree.ElementTree as ET

tree = ET.parse('monitor.xml')
root = tree.getroot()

targets = root.findall("./monitor-run-task/variables/targets/target")

for target in targets:
  hostname = target.text
  port = target.get("port")

  context = ssl.create_default_context()
  try:
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            data = ssock.getpeercert()
            expirationDateDT = datetime.datetime.strptime(data['notAfter'], '%b  %d %H:%M:%S %Y %Z') 
    
    now = datetime.datetime.today()
    daysLeft = expirationDateDT - now
    
    DEFAULT_METRIC_PREFIX="name=Custom Metrics|CertMonitor|" + hostname + "|Days Until Cert Expiration,value=" + str(daysLeft.days)
    print(DEFAULT_METRIC_PREFIX)
  except:
    pass
