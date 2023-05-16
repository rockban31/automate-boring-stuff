import requests
res = requests.get('https://www.linkedin.com/in/rohith-jayaram-40694916/')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
else:
    print('url works fine')
finally:
    print('Done with testing')