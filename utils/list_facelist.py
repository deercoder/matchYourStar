#!/usr/bin/env python
import httplib, urllib, base64

headers = {
    'Ocp-Apim-Subscription-Key': 'f157f2833feb46e898122acef0632c23',
}

params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("GET", "/face/v1.0/facelists?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
