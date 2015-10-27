#!/bin/bash
wget -O sesarwslib/sample/sample.xsd http://app.geosamples.org/sample.xsd
generateDS.py -o sesarwslib/sample/Sample.py sesarwslib/sample/sample.xsd

wget -O sesarwslib/sample/samplev2.xsd http://app.geosamples.org/samplev2.xsd
generateDS.py -o sesarwslib/sample/SampleV2.py sesarwslib/sample/samplev2.xsd
