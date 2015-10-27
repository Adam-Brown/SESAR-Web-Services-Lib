#!/bin/bash
wget -O sesarwslib/sample/sample.xsd http://app.geosamples.org/sample.xsd
generateDS.py -o sesarwslib/sample/Sample.py sesarwslib/sample/sample.xsd
sed -i 's/^# Generated .\+//' sesarwslib/sample/Sample.py

wget -O sesarwslib/samplev2/samplev2.xsd http://app.geosamples.org/samplev2.xsd
generateDS.py -o sesarwslib/samplev2/SampleV2.py sesarwslib/samplev2/samplev2.xsd
sed -i 's/^# Generated .\+//' sesarwslib/samplev2/SampleV2.py
