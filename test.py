# This is just to provide an example of how the library can be used.
# Make sure you set password and username.
from sesarwslib import categories as cat
from sesarwslib.sample import Sample
import os
import StringIO

# Add these environment variables to your run configuration.
# In PyCharm that's Run > Edit Configurations > Environment Variables.
username = os.environ['SESAR_USERNAME']
password = os.environ['SESAR_PASSWORD']
user_code = os.environ['SESAR_USER_CODE']

# These are the minimum requirements, though the constructor does accept more:
sample = Sample.sample(
    sample_type=cat.SampleType.IndividualSample,
    user_code=user_code,
    name='TestSample123',
    material=cat.Material.Rock)

#sample.set_igsn(igsn)
#sample.set_sample_other_name(sample_other_name)
#sample.set_parent_igsn(parent_igsn)
#sample.set_parent_sample_type(parent_sample_type)
#sample.set_parent_name(parent_name)
#sample.set_is_private(is_private)
#sample.set_publish_date(publish_date)
#sample.set_classification(classification)
#sample.set_field_name(field_name)
#sample.set_description(description)
#sample.set_age_min(age_min)
#sample.set_age_max(age_max)
#sample.set_age_unit(age_unit)
#sample.set_geological_age(geological_age)
#sample.set_geological_unit(geological_unit)
#sample.set_collection_method(collection_method)
#sample.set_collection_method_descr(collection_method_descr)
#sample.set_size(size)
#sample.set_size_unit(size_unit)
#sample.set_sample_comment(sample_comment)
#sample.set_latitude(latitude)
#sample.set_longitude(longitude)
#sample.set_latitude_end(latitude_end)
#sample.set_longitude_end(longitude_end)
#sample.set_elevation(elevation)
#sample.set_elevation_end(elevation_end)
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
#sample.set_collector(collector)
#sample.set_collector_detail(collector_detail)
#sample.set_collection_date_precision(collection_date_precision)
#sample.set_current_archive(current_archive)
#sample.set_current_archive_contact(current_archive_contact)
#sample.set_original_archive(original_archive)
#sample.set_original_archive_contact(original_archive_contact)
#sample.set_depth_min(depth_min)
#sample.set_depth_max(depth_max)
#sample.set_depth_scale(depth_scale)
#sample.set_other_names(other_names)
#sample.add_other_names(value)


output = StringIO.StringIO()
sample.export(output, 1)

print output.getvalue()




#client = ws.IgsnClient(username, password)

#print client.get_user_codes()
#client.register_sample(sample)
#print ws.IgsnClient.list_igsns(user_code, 10, 1)
