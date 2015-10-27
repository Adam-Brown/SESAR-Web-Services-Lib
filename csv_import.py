#!/usr/bin/python
# This is just to provide an example of how the library can be used.
# Make sure you set password and username.
import csv
import os
import sys
from itertools import izip_longest
from sesarwslib.sample import Sample
from datetime import datetime
import sesarwslib.sesarwsclient as ws

csv_path = sys.argv[1]

# Add these environment variables to your run configuration.
# You can add this to a git-ignored file called env.bash and then source it when you run your session:
#   export SESAR_USERNAME="xxxx"
#   export SESAR_PASSWORD="xxxx"
#   export SESAR_USER_CODE="xxxx"

username = os.environ['SESAR_USERNAME']
password = os.environ['SESAR_PASSWORD']
user_code = os.environ['SESAR_USER_CODE']

STRING_TYPE   = 0
DATETIME_TYPE = 1
INT_TYPE      = 2
DECIMAL_TYPE  = 3

# http://app.geosamples.org/reference/sampletypes.php
allowed_sample_types = [
    'Core',
    'Core Half Round',
    'Core Piece',
    'Core Quarter Round',
    'Core Section',
    'Core Section Half',
    'Core Sub-Piece',
    'Core Whole Round',
    'CTD',
    'Cuttings',
    'Dredge',
    'Grab',
    'Hole',
    'Individual Sample',
    'Oriented Core',
    'Other',
    'Rock Powder',
    'Site',
    'Terrestrial Section',
    'Trawl',
    'Bead',
    'Chemical Fraction',
    'Cube',
    'Culture',
    'Cylinder',
    'Gas',
    'Liquid',
    'Mechanical Fraction',
    'Powder',
    'Slab',
    'Smear',
    'Specimen',
    'Squeeze Cake',
    'Thin Section',
    'Toothpick',
    'U-Channel',
    'Wedge'
]

# http://app.geosamples.org/reference/materials.php
allowed_materials = [
    'Biology',
    'Gas',
    'Ice',
    'Liquid>aqueous',
    'Liquid>organic',
    'Mineral',
    'NotApplicable',
    'Other',
    'Particulate',
    'Rock',
    'Sediment',
    'Soil',
    'Synthetic'
]

required_headings = {
    'sample_type':                  allowed_sample_types,                                
    'name':                         STRING_TYPE,    # string 0 to 255  TODO: is this really allowed to be empty?
    'material':                     allowed_materials
}

optional_headings = {
    'parent_igsn':                  STRING_TYPE,    # string 9 (must be valid IGSN)
    'is_private':                   INT_TYPE,       # 0 = no,    1 = yes
    'publish_date':                 STRING_TYPE,    # MM/DD/YYYY
    'classification':               STRING_TYPE,    # http://app.geosamples.org/reference/classifications.php # TODO: restrict. This one is huge.
    'field_name':                   STRING_TYPE,    # http://app.geosamples.org/reference/field_names.php # TODO: restrict. This one is huge.
    'description':                  STRING_TYPE,    # string 0 to 2000
    'age_min':                      DECIMAL_TYPE,
    'age_max':                      DECIMAL_TYPE,
    'age_unit':                     STRING_TYPE,    # string 0 to 255
    'geological_age':               STRING_TYPE,    # string 0 to 500
    'geological_unit':              STRING_TYPE,    # string 0 to 500
    'collection_method':            STRING_TYPE,    # string 0 to 255
    'collection_method_descr':      STRING_TYPE,    # string 0 to 1000
    'size':                         STRING_TYPE,    # string 0 to 255
    'size_unit':                    STRING_TYPE,    # string 0 to 255
    'sample_comment':               STRING_TYPE,    # string 0 to 2000
    'latitude':                     DECIMAL_TYPE,   # decimal -90.0 to 90.0
    'longitude':                    DECIMAL_TYPE,   # decimal -180.0 to 180.0
    'latitude_end':                 DECIMAL_TYPE,   # decimal -90.0 to 90.0
    'longitude_end':                DECIMAL_TYPE,   # decimal -180.0 to 180.0
    'elevation':                    DECIMAL_TYPE,   # decimal -6000.0 to 9000.0 (Minimum elevation)
    'elevation_end':                DECIMAL_TYPE,   # decimal -6000.0 to 9000.0 (Maximum elevation)
    'elevation_unit':               STRING_TYPE,    # string must be "Meters" (case sensitive)
    'primary_location_type':        STRING_TYPE,    # string 0 to 255
    'primary_location_name':        STRING_TYPE,    # string 0 to 255
    'location_description':         STRING_TYPE,    # string 0 to 2000
    'locality':                     STRING_TYPE,    # string 0 to 255
    'locality_description':         STRING_TYPE,    # string 0 to 2000
    'country':                      STRING_TYPE,    # http://app.geosamples.org/reference/countries.php # TODO: restrict
    'province':                     STRING_TYPE,    # string 0 to 255
    'county':                       STRING_TYPE,    # string 0 to 255
    'city':                         STRING_TYPE,    # string 0 to 255
    'cruise_field_prgrm':           STRING_TYPE,    # http://www.rvdata.us/catalog # TODO: restrict
    'platform_type':                STRING_TYPE,    # string 0 to 255
    'platform_name':                STRING_TYPE,    # string 0 to 2000
    'platform_descr':               STRING_TYPE,    # string 0 to 2000
    'collector':                    STRING_TYPE,    # string 0 to 255
    'collector_detail':             STRING_TYPE,    # string 0 to 2000
    'collection_start_date':        DATETIME_TYPE,  # Must be in format YYYY-MM-DD HH-mm-ss, e.g. 2015-01-01 13:09:22
    'collection_end_date':          DATETIME_TYPE,  # Must be in format YYYY-MM-DD HH-mm-ss, e.g. 2015-01-01 13:09:22
    'collection_date_precision':    STRING_TYPE,    # year, month, day, time
    'current_archive':              STRING_TYPE,    # string 0 to 300
    'current_archive_contact':      STRING_TYPE,    # string 0 to 1000
    'original_archive':             STRING_TYPE,    # string 0 to 300
    'original_archive_contact':     STRING_TYPE,    # string 0 to 1000
    'depth_min':                    DECIMAL_TYPE,   # decimal
    'depth_max':                    DECIMAL_TYPE,   # decimal
    'depth_scale':                  STRING_TYPE,    # string 0 to 255
    'other_names':                  STRING_TYPE,    # string 0 to 255
    'navigation_type':              STRING_TYPE,    # http://app.geosamples.org/reference/navtypes.php # TODO: restrict
    'launch_platform_name':         STRING_TYPE     # http://app.geosamples.org/reference/launchtypes.php # TODO: restrict
}

allowed_headings = required_headings.copy()
allowed_headings.update(optional_headings)

igsnClient = ws.IgsnClient(username, password, 1)

with open(csv_path, 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    first = True
    headings = []
    samples = []

    for row in csvreader:
        if first:
            first = False
            headings = row
            headings_error = False

            # Check that all the provided headings are allowed:
            for heading in headings:
                if heading not in required_headings.keys() and heading not in optional_headings.keys():
                    print 'Error: \'%s\' heading is not allowed.' % heading
                    headings_error = True

            # Make sure the required headings have been provided:
            for required_heading in required_headings.keys():
                if required_heading not in headings:
                    print 'Error: \'%s\' heading is required.' % required_heading
                    headings_error = True

            if headings_error:
                sys.exit()
        else:
            sample_metadata = dict(zip(headings, row))
            
            sample = Sample.sampleType(user_code = user_code)
            
            validation_error = False            
            for heading, value in sample_metadata.iteritems():
                value_type = allowed_headings[heading]
                
                eval_string = ''
                
                if type(value_type) is list:
                    if value not in value_type:
                        print 'Error: \'%s\' is not an allowed value for \'%s\'.' % (value, heading)
                        validation_error = True
                    else:
                        # If we're happy that the value is allowed then we just treat it as a string.
                        value_type = STRING_TYPE
                
                if value_type == STRING_TYPE:
                    eval_string = "sample.set_%s('%s')" % (heading, value.replace("\\", "\\\\").replace("'", "\\'"))
                
                elif value_type == DATETIME_TYPE:
                    datetime_value = datetime.strptime(value, '%Y-%m-%d %H:%I:%S')
                    eval_string = "sample.set_%s(datetime_value)" % (heading)

                elif value_type == INT_TYPE or value_type == DECIMAL_TYPE:
                    eval_string = "sample.set_%s(%s)" % (heading, value)

                if validation_error:
                    sys.exit()
                
                eval(eval_string)

            samples.append(sample)

# Register in groups of 10:
sample_groups = izip_longest(*(iter(samples),) * 10)

for sample_group in sample_groups:
     sample_group = filter(None, sample_group)
     igsns = igsnClient.register_samples(sample_group)
     for i in range(0, len(igsns)):
        print '{0} => {1}'.format(igsns[i], sample_group[i].get_name())