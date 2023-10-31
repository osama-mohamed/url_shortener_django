from .models import Analytics


def create_new_analytics(ip, data, parsed_data, obj):
  country_code = data.get('country_code')
  country_name = data.get('country_name')
  region_name = data.get('region_name')
  city_name = data.get('city_name')
  latitude = data.get('latitude')
  longitude = data.get('longitude')
  zip_code = data.get('zip_code')
  time_zone = data.get('time_zone')
  net_provider = data.get('as')
  net_provider_code = data.get('asn')

  platform_name = parsed_data.get('platform').get('name')
  platform_version = parsed_data.get('platform').get('version')
  os_name = parsed_data.get('os').get('name')
  os_version = parsed_data.get('os').get('version')
  browser_name = parsed_data.get('browser').get('name')
  browser_version = parsed_data.get('browser').get('version')
  Analytics.objects.create(
    short_url=obj,
    ip_address=ip,
    country=country_name,
    country_code=country_code,
    region_name=region_name,
    city_name=city_name,
    latitude=latitude,
    longitude=longitude,
    zip_code=zip_code,
    time_zone=time_zone,
    net_provider=net_provider,
    net_provider_code=net_provider_code,
    platform=platform_name,
    platform_version=platform_version,
    os=os_name,
    os_version=os_version,
    browser=browser_name,
    browser_version=browser_version,
  )