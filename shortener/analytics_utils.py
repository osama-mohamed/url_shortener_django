import requests, os, httpagentparser
from dotenv import load_dotenv

load_dotenv()
APIKEY = os.getenv('APIKEY')

def get_client_ip(request):
  x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
  if x_forwarded_for:
    ip = x_forwarded_for.split(',')[0]
  else:
    ip = request.META.get('REMOTE_ADDR')
  return ip


def get_country(ip):
  payload = {'key': APIKEY, 'ip': ip, 'format': 'json'}
  api_result = requests.get('https://api.ip2location.io/', params=payload)
  return api_result.json()


def get_platform_browser(request):
  platform_browser = httpagentparser.detect(request)
  return platform_browser