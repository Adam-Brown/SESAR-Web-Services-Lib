SESAR-Web-Services-Lib
======================

SESAR web services library for IGSN management (Python)

This project is a work in progress.

Useful links:
- http://www.iedadata.org/services/sesar_api
- http://app.geosamples.org/reference/classifications.php
- https://pypi.python.org/pypi/SESAR-Web-Services-Library/

sample_type:        http://app.geosamples.org/reference/sampletypes.php
name:               string 0 to 255
material:           http://app.geosamples.org/reference/materials.php
parent_igsn:        string 9 (must be valid IGSN)
is_private:         0 = no, 1 = yes
publish_date:       string 10 in format: MM/DD/YYYY
classification:     http://app.geosamples.org/reference/classifications.php
field_name:         http://app.geosamples.org/reference/field_names.php
description:        string 0 to 2000
age_min:            decimal
age_max:            decimal
age_unit:           string 0 to 255
geological_age:     string 0 to 500
geological_unit:    string 0 to 500
collection_method:  string 0 to 255
collection_method_descr:    string 0 to 1000
size:               string 0 to 255
size_unit:          string 0 to 255
sample_comment:     string 0 to 2000
latitude:           decimal -90.0 to 90.0
longitude:          decimal -180.0 to 180.0
latitude_end:       decimal -90.0 to 90.0
longitude_end:      decimal -180.0 to 180.0
elevation:          decimal -6000.0 to 9000.0 (Minimum elevation)
elevation_end:      decimal -6000.0 to 9000.0 (Maximum elevation)
elevation_unit:     string must be "Meters" (case sensitive)
primary_location_type:  string 0 to 255
primary_location_name:  string 0 to 255
location_description:   string 0 to 2000
locality:               string 0 to 255
locality_description:   string 0 to 2000
country:                http://app.geosamples.org/reference/countries.php
province:               string 0 to 255
county:                 string 0 to 255
city:                   string 0 to 255
cruise_field_prgrm:     http://www.rvdata.us/catalog
platform_type:          string 0 to 255
platform_name:          string 0 to 2000
platform_descr:         string 0 to 2000
collector:              string 0 to 255
collector_detail:       string 0 to 2000
collection_start_date:  YYYY-MM-DD-HH-mm-ss  !! TODO: This has to be converted to a datetime object
collection_end_date:    YYYY-MM-DD-HH-mm-ss  !! TODO: This has to be converted to a datetime object
collection_date_precision: year, month, day, time
current_archive:        string 0 to 300
current_archive_contact: string 0 to 1000
original_archive:       string 0 to 300
original_archive_contact: string 0 to 1000
depth_min:              decimal
depth_max:              decimal
depth_scale:            string 0 to 255
other_names:            string 0 to 255
navigation_type:        http://app.geosamples.org/reference/navtypes.php
launch_platform_name:   http://app.geosamples.org/reference/launchtypes.php
