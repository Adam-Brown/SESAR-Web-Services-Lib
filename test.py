#!/usr/bin/python
# This is just to provide an example of how the library can be used.
# Make sure you set password and username.
from sesarwslib import categories as cat
from sesarwslib.sample import Sample
from datetime import datetime
import sesarwslib.sesarwsclient as ws
import os

# Add these environment variables to your run configuration.
# In PyCharm that's Run > Edit Configurations > Environment Variables.
#username = os.environ['SESAR_USERNAME']
#password = os.environ['SESAR_PASSWORD']
#user_code = os.environ['SESAR_USER_CODE']

# These are the minimum requirements, though the constructor does accept more:
sample = Sample.sample(
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
#sample.set_purpose('Just a test') # Text 100 V2 ONLY
sample.set_latitude(33.1) # -90.0 to 90.0
sample.set_longitude(-55.1) # -180 to 180
sample.set_latitude_end(33.2)
sample.set_longitude_end(-55.2)
sample.set_elevation(400)
sample.set_elevation_end(404)

#sample.set_elevation_unit('meters') # V1 ONLY
#sample.set_vertical_datum('MSL') # NAVD88 or MSL V2 ONLY

#sample.set_northing(northing) # V2 ONLY
#sample.set_easting(easting) # V2 ONLY
#sample.set_zone(zone) # V2 ONLY


sample.set_primary_location_type('Type of phyiscal feature that your sample was collected from.') # Text 255
sample.set_primary_location_name('Name of the primary_location_type that you entered') # Text 255
sample.set_location_description('Additional information about the specific place where your sample was collected') # Text 2000
sample.set_locality('Name of the specific place where your sample was collected. This could be the  name of a mine, a volcanic field, a vent field, or similar') # Text 255
sample.set_locality_description('Additional information about the specific place where your sample was collected') # Text 255
sample.set_country('Australia') # Text 255 see http://app.geosamples.org/reference/countries.php
sample.set_province('Western Australia') # Text 255
sample.set_county('Western Australia') # Text 255
sample.set_city('Caraboooda') # Text 255
sample.set_cruise_field_prgrm('VNTR02WT') # Text 255 See http://app.geosamples.org/reference/advanced_list.php?srv=cruise_field_prgrm for what other users have entered. http://www.rvdata.us/catalog is mentioned in V1
sample.set_platform_type('Type of platform for the cruise.') # Text 255
sample.set_platform_name('Name of platform for the cruise.') # Text 2000
sample.set_platform_descr('Description of the platform for the cruise.') # Text 200
sample.set_navigation_type('GPS') # See http://app.geosamples.org/reference/navtypes.php
sample.set_launch_platform_name('Not Applicable') # Text 100, see http://app.geosamples.org/reference/launchtypes.php
#sample.set_launch_id(launch_id) # V2 ONLY
#sample.set_launch_type_name(launch_type_name) # V2 ONLY
sample.set_collector('Name of the person who collected the sample.') # Text 255
sample.set_collector_detail('Institution, address, & email of the collector or chief scientist.') # Text 2000
sample.set_collection_start_date(datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p'))
sample.set_collection_end_date(datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p'))
sample.set_collection_date_precision('time') # year, month, day, time
sample.set_current_archive('Name of institution, museum, or repository where the sample is currently stored.') # Text 300
sample.set_current_archive_contact('Address and/or email of the person who should be contacted for information about or access to the sample.') # Text 1000
sample.set_original_archive('Name of institution, museum, or repository where the sample was originally stored.') # 300
sample.set_original_archive_contact('Address and/or email of the person who should be contacted for information about the sample\'s original archive.') # Text 1000
sample.set_depth_min(1.9) # decimal
sample.set_depth_max(2.0) # decimal
sample.set_depth_scale('Unit in which the depth is provided, e.g., MBSF') # Text 255
#sample.set_sample_other_names(sample_other_names) # V2 ONLY
#sample.set_external_urls(external_urls) # V2 ONLY

client = ws.IgsnClient(username, password)

# 1. Sample registration web service
print client.register_sample(sample)

# 2. Credential web service
#print client.get_user_codes()

# 3. SESAR IGSN list web service for specific user code
#print ws.IgsnClient.list_igsns(user_code, 10, 1)
#print ws.IgsnClient.list_igsns(user_code, 10)
#print ws.IgsnClient.list_igsns(user_code)
