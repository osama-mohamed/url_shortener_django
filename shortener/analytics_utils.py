import requests, os, httpagentparser

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
  new_data = {key: None if value in ('-',) else value for key, value in api_result.json().items()}
  return new_data


def get_platform_browser(request):
  platform_browser = httpagentparser.detect(request)
  return platform_browser


def return_analytics_data(request):
  ip = get_client_ip(request)
  data = get_country(ip)
  parsed_data = get_platform_browser(request.META.get('HTTP_USER_AGENT', ''))
  return ip, data, parsed_data