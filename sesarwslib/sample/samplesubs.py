#!/usr/bin/env python

#
# Generated Thu Dec 11 16:21:16 2014 by generateDS.py version 2.14a.
#
# Command line options:
#   ('-o', 'sesarwslib/sample/sample.py')
#   ('-s', 'sesarwslib/sample/samplesubs.py')
#
# Command line arguments:
#   sesarwslib/sample/sample.xsd
#
# Command line:
#   /usr/local/bin/generateDS.py -o "sesarwslib/sample/sample.py" -s "sesarwslib/sample/samplesubs.py" sesarwslib/sample/sample.xsd
#
# Current working directory (os.getcwd()):
#   SESAR-Web-Services-Lib
#

import sys

import ??? as supermod

etree_ = None
Verbose_import_ = False
(
    XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError(
                        "Failed to import ElementTree from any known place")


def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
            'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class sampleSub(supermod.sample):
    def __init__(self, sample_type=None, igsn=None, user_code=None, name=None, sample_other_name=None, parent_igsn=None, parent_sample_type=None, parent_name=None, is_private=None, publish_date=None, material=None, classification=None, field_name=None, description=None, age_min=None, age_max=None, age_unit=None, geological_age=None, geological_unit=None, collection_method=None, collection_method_descr=None, size=None, size_unit=None, sample_comment=None, latitude=None, longitude=None, latitude_end=None, longitude_end=None, elevation=None, elevation_end=None, primary_location_type=None, primary_location_name=None, location_description=None, locality=None, locality_description=None, country=None, province=None, county=None, city=None, cruise_field_prgrm=None, platform_type=None, platform_name=None, platform_descr=None, collector=None, collector_detail=None, collection_date_precision=None, current_archive=None, current_archive_contact=None, original_archive=None, original_archive_contact=None, depth_min=None, depth_max=None, depth_scale=None, other_names=None):
        super(sampleSub, self).__init__(sample_type, igsn, user_code, name, sample_other_name, parent_igsn, parent_sample_type, parent_name, is_private, publish_date, material, classification, field_name, description, age_min, age_max, age_unit, geological_age, geological_unit, collection_method, collection_method_descr, size, size_unit, sample_comment, latitude, longitude, latitude_end, longitude_end, elevation, elevation_end, primary_location_type, primary_location_name, location_description, locality, locality_description, country, province, county, city, cruise_field_prgrm, platform_type, platform_name, platform_descr, collector, collector_detail, collection_date_precision, current_archive, current_archive_contact, original_archive, original_archive_contact, depth_min, depth_max, depth_scale, other_names, )
supermod.sample.subclass = sampleSub
# end class sampleSub


class age_unitSub(supermod.age_unit):
    def __init__(self):
        super(age_unitSub, self).__init__()
supermod.age_unit.subclass = age_unitSub
# end class age_unitSub


class geological_unitSub(supermod.geological_unit):
    def __init__(self):
        super(geological_unitSub, self).__init__()
supermod.geological_unit.subclass = geological_unitSub
# end class geological_unitSub


class collection_methodSub(supermod.collection_method):
    def __init__(self):
        super(collection_methodSub, self).__init__()
supermod.collection_method.subclass = collection_methodSub
# end class collection_methodSub


class collection_method_descrSub(supermod.collection_method_descr):
    def __init__(self):
        super(collection_method_descrSub, self).__init__()
supermod.collection_method_descr.subclass = collection_method_descrSub
# end class collection_method_descrSub


class size_unitSub(supermod.size_unit):
    def __init__(self):
        super(size_unitSub, self).__init__()
supermod.size_unit.subclass = size_unitSub
# end class size_unitSub


class sample_commentSub(supermod.sample_comment):
    def __init__(self):
        super(sample_commentSub, self).__init__()
supermod.sample_comment.subclass = sample_commentSub
# end class sample_commentSub


class primary_location_typeSub(supermod.primary_location_type):
    def __init__(self):
        super(primary_location_typeSub, self).__init__()
supermod.primary_location_type.subclass = primary_location_typeSub
# end class primary_location_typeSub


class primary_location_nameSub(supermod.primary_location_name):
    def __init__(self):
        super(primary_location_nameSub, self).__init__()
supermod.primary_location_name.subclass = primary_location_nameSub
# end class primary_location_nameSub


class location_descriptionSub(supermod.location_description):
    def __init__(self):
        super(location_descriptionSub, self).__init__()
supermod.location_description.subclass = location_descriptionSub
# end class location_descriptionSub


class localitySub(supermod.locality):
    def __init__(self):
        super(localitySub, self).__init__()
supermod.locality.subclass = localitySub
# end class localitySub


class locality_descriptionSub(supermod.locality_description):
    def __init__(self):
        super(locality_descriptionSub, self).__init__()
supermod.locality_description.subclass = locality_descriptionSub
# end class locality_descriptionSub


class collection_date_precisionSub(supermod.collection_date_precision):
    def __init__(self):
        super(collection_date_precisionSub, self).__init__()
supermod.collection_date_precision.subclass = collection_date_precisionSub
# end class collection_date_precisionSub


class current_archiveSub(supermod.current_archive):
    def __init__(self):
        super(current_archiveSub, self).__init__()
supermod.current_archive.subclass = current_archiveSub
# end class current_archiveSub


class current_archive_contactSub(supermod.current_archive_contact):
    def __init__(self):
        super(current_archive_contactSub, self).__init__()
supermod.current_archive_contact.subclass = current_archive_contactSub
# end class current_archive_contactSub


class original_archiveSub(supermod.original_archive):
    def __init__(self):
        super(original_archiveSub, self).__init__()
supermod.original_archive.subclass = original_archiveSub
# end class original_archiveSub


class original_archive_contactSub(supermod.original_archive_contact):
    def __init__(self):
        super(original_archive_contactSub, self).__init__()
supermod.original_archive_contact.subclass = original_archive_contactSub
# end class original_archive_contactSub


class depth_scaleSub(supermod.depth_scale):
    def __init__(self):
        super(depth_scaleSub, self).__init__()
supermod.depth_scale.subclass = depth_scaleSub
# end class depth_scaleSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'sample'
        rootClass = supermod.sample
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'sample'
        rootClass = supermod.sample
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'sample'
        rootClass = supermod.sample
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'sample'
        rootClass = supermod.sample
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
