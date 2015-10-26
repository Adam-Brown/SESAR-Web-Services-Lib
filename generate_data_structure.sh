#!/bin/bash
wget -O sesarwslib/sample/sample.xsd http://app.geosamples.org/samplev2.xsd
generateDS.py -o sesarwslib/sample/Sample.py sesarwslib/sample/sample.xsd
