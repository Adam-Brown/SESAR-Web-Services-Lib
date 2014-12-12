#!/bin/bash
wget -O sesarwslib/sample/sample.xsd http://app.geosamples.org/sample.xsd
generateDS.py -o sesarwslib/sample/Sample.py -s sesarwslib/sample/SampleSubs.py sesarwslib/sample/sample.xsd
