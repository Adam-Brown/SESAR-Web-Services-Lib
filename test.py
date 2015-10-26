# This is just to provide an example of how the library can be used.
# Make sure you set password and username.
from sesarwslib import categories as cat
from sesarwslib.sample import Sample
import sesarwslib.sesarwsclient as ws
import os


# Add these environment variables to your run configuration.
# In PyCharm that's Run > Edit Configurations > Environment Variables.
#username = os.environ['SESAR_USERNAME']
#password = os.environ['SESAR_PASSWORD']
#user_code = os.environ['SESAR_USER_CODE']

# These are the minimum requirements, though the constructor does accept more:
sample = Sample.sampleType(
    user_code=user_code,
    sample_type=cat.SampleType.IndividualSample,
    name='TestSample123',
    material=cat.Material.Rock)

#sample.set_igsn(igsn)
sample.set_parent_igsn('IEEVB00KS')
sample.set_is_private(0)
sample.set_publish_date('01/11/2015') # Check this... the format in the schema, 2015-11-01, doesn't match what the API expects.
#sample.set_classification(classification) # See http://app.geosamples.org/classifications.xsd
#sample.set_classification_comment(classification_comment)
#sample.set_field_name(field_name) # See http://app.geosamples.org/reference/field_names.php
sample.set_description('Up to 2000 characters of description.')
sample.set_age_min(10.22)
sample.set_age_max(10.3)
sample.set_age_unit('Ma') # Ma or years. Plain text.
sample.set_geological_age('10') # Text 500
sample.set_geological_unit('Million years') # Text 500
#sample.set_collection_method(collection_method) # See http://app.geosamples.org/reference/advanced_list.php?srv=collection_method
#sample.set_collection_method_descr(collection_method_descr)
sample.set_size('25') # Text 255
sample.set_size_unit('mm diameter round') # Text 255
sample.set_sample_comment('A test sample comment.') # Text 2000
sample.set_purpose('Just a test') # Text 100
sample.set_latitude(33.1) # -90.0 to 90.0
sample.set_longitude(-55.1) # -180 to 180
sample.set_latitude_end(33.2)
sample.set_longitude_end(-55.2)
sample.set_elevation(400)
sample.set_elevation_end(404)
sample.set_vertical_datum('MSL') # NAVD88 or MSL
#sample.set_northing(northing)
#sample.set_easting(easting)
#sample.set_zone(zone)
#sample.set_navigation_type(navigation_type)
#sample.set_primary_location_type(primary_location_type)
#sample.set_primary_location_name(primary_location_name)
#sample.set_location_description(location_description)
#sample.set_locality(locality)
#sample.set_locality_description(locality_description)
#sample.set_country(country)
#sample.set_province(province)
#sample.set_county(county)
#sample.set_city(city)
#sample.set_cruise_field_prgrm(cruise_field_prgrm)
#sample.set_platform_type(platform_type)
#sample.set_platform_name(platform_name)
#sample.set_platform_descr(platform_descr)
#sample.set_launch_platform_name(launch_platform_name)
#sample.set_launch_id(launch_id)
#sample.set_launch_type_name(launch_type_name)
#sample.set_collector(collector)
#sample.set_collector_detail(collector_detail)
#sample.set_collection_start_date(collection_start_date)
#sample.set_collection_end_date(collection_end_date)
#sample.set_collection_date_precision(collection_date_precision)
#sample.set_current_archive(current_archive)
#sample.set_current_archive_contact(current_archive_contact)
#sample.set_original_archive(original_archive)
#sample.set_original_archive_contact(original_archive_contact)
#sample.set_depth_min(depth_min)
#sample.set_depth_max(depth_max)
#sample.set_depth_scale(depth_scale)
#sample.set_sample_other_names(sample_other_names)
#sample.set_external_urls(external_urls)

client = ws.IgsnClient(username, password)

# 1. Sample registration web service
print client.register_sample(sample)

# 2. Credential web service
#print client.get_user_codes()

# 3. SESAR IGSN list web service for specific user code
#print ws.IgsnClient.list_igsns(user_code, 10, 1)
#print ws.IgsnClient.list_igsns(user_code, 10)
#print ws.IgsnClient.list_igsns(user_code)
