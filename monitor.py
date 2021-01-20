from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import json, time
base_url = 'appdynamics.com'
port = '443'

hostname = base_url
context = ssl.create_default_context()

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        #print("Socket Version: ", ssock.version())
        data = ssock.getpeercert()
        # print(ssock.getpeercert())
        expirationDate = data['notAfter']
        expirationDateTimestamp = time.mktime(time.strptime(expirationDate, '%b  %d %H:%M:%S %Y %Z')) 

print (expirationDate)
print (expirationDateTimestamp)
print ("time now: ", time.mktime(time.localtime()))

# Oct  5 12:00:00 2021 GMT



#{"subject": [[["businessCategory", "Private Organization"]], [["jurisdictionCountryName", "US"]], [["jurisdictionStateOrProvinceName", "Delaware"]], [["serialNumber", "4527594"]], [["countryName", "US"]], [["stateOrProvinceName", "California"]], [["localityName", "San Francisco"]], [["organizationName", "AppDynamics LLC"]], [["commonName", "appdynamics.com"]]], "issuer": [[["countryName", "US"]], [["organizationName", "DigiCert Inc"]], [["organizationalUnitName", "www.digicert.com"]], [["commonName", "DigiCert SHA2 Extended Validation Server CA"]]], "version": 3, "serialNumber": "091C80A4DBD0EAED39531859A555EA63", "notBefore": "Sep 10 00:00:00 2020 GMT", "notAfter": "Oct  5 12:00:00 2021 GMT", "subjectAltName": [["DNS", "appdynamics.com"], ["DNS", "appdynamics.jp"], ["DNS", "www.appdynamics.jp"], ["DNS", "appdynamics.fr"], ["DNS", "www.appdynamics.fr"], ["DNS", "www.appdynamics.de"], ["DNS", "appdynamics.de"], ["DNS", "appdynamics.co.uk"], ["DNS", "www.appdynamics.co.uk"], ["DNS", "www.appdynamics.com"]], "OCSP": ["http://ocsp.digicert.com"], "caIssuers": ["http://cacerts.digicert.com/DigiCertSHA2ExtendedValidationServerCA.crt"], "crlDistributionPoints": ["http://crl3.digicert.com/sha2-ev-server-g2.crl", "http://crl4.digicert.com/sha2-ev-server-g2.crl"]}  
