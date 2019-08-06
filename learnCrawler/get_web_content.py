import urllib.request
import urllib.parse
# must install openssl first see https://slproweb.com/products/Win32OpenSSL.html
import ssl


def get_response(url):
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, context=context) as response:
        content = response.read().decode('utf-8')
    return content



