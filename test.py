# This is just to provide an example of how the library can be used.
# Make sure you set password and username.
from sesarwslib import categories as cat
from sesarwslib.sample import Sample
import StringIO

username = ''  # Set but don't check-in.
password = ''  # Set but don't check-in.
user_code = ''  # Set but don't check-in.


# These are the minimum requirements, though the constructor does accept more:
sample2 = Sample.sample(
    sample_type=cat.SampleType.IndividualSample,
    user_code=user_code,
    name='TestSample123',
    material=cat.Material.Rock)

#sample2.set_igsn(igsn)
#sample2.set_sample_other_name(sample_other_name)
#sample2.set_parent_igsn(parent_igsn)
#sample2.set_parent_sample_type(parent_sample_type)
#sample2.set_parent_name(parent_name)
#sample2.set_is_private(is_private)
#sample2.set_publish_date(publish_date)
#sample2.set_classification(classification)
#sample2.set_field_name(field_name)
#sample2.set_description(description)
#sample2.set_age_min(age_min)
#sample2.set_age_max(age_max)
#sample2.set_age_unit(age_unit)
#sample2.set_geological_age(geological_age)
#sample2.set_geological_unit(geological_unit)
#sample2.set_collection_method(collection_method)
#sample2.set_collection_method_descr(collection_method_descr)
#sample2.set_size(size)
#sample2.set_size_unit(size_unit)
#sample2.set_sample_comment(sample_comment)
#sample2.set_latitude(latitude)
#sample2.set_longitude(longitude)
#sample2.set_latitude_end(latitude_end)
#sample2.set_longitude_end(longitude_end)
#sample2.set_elevation(elevation)
#sample2.set_elevation_end(elevation_end)
#sample2.set_primary_location_type(primary_location_type)
#sample2.set_primary_location_name(primary_location_name)
#sample2.set_location_description(location_description)
#sample2.set_locality(locality)
#sample2.set_locality_description(locality_description)
#sample2.set_country(country)
#sample2.set_province(province)
#sample2.set_county(county)
#sample2.set_city(city)
#sample2.set_cruise_field_prgrm(cruise_field_prgrm)
#sample2.set_platform_type(platform_type)
#sample2.set_platform_name(platform_name)
#sample2.set_platform_descr(platform_descr)
#sample2.set_collector(collector)
#sample2.set_collector_detail(collector_detail)
#sample2.set_collection_date_precision(collection_date_precision)
#sample2.set_current_archive(current_archive)
#sample2.set_current_archive_contact(current_archive_contact)
#sample2.set_original_archive(original_archive)
#sample2.set_original_archive_contact(original_archive_contact)
#sample2.set_depth_min(depth_min)
#sample2.set_depth_max(depth_max)
#sample2.set_depth_scale(depth_scale)
#sample2.set_other_names(other_names)
#sample2.add_other_names(value)


output = StringIO.StringIO()
sample2.export(output, 1)

print output.getvalue()




#client = ws.IgsnClient(username, password)

#print client.get_user_codes()
#client.register_sample(sample1)
#print ws.IgsnClient.list_igsns(user_code, 10, 1)
