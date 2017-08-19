import urllib.request
with urllib.request.urlopen('http://www.npr.org/2017/08/18/148297699/guest-djs-carrie-brownstein-and-fred-armisen') as f:
    print(f.read().decode('utf-8'))
