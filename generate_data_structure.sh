#!/bin/bash
wget -O sesarwslib/sample/sample.xsd http://app.geosamples.org/sample.xsd
generateDS.py -o sesarwslib/sample/sample.py -s sesarwslib/sample/samplesubs.py sesarwslib/sample/sample.xsd
