import urllib
import urllib2
import xml.etree.ElementTree as eTree
import StringIO


SAMPLE_REGISTRATION_SERVICE_URL = 'http://app.geosamples.org/webservices/uploadservice.php'
CREDENTIAL_SERVICE_URL = 'http://app.geosamples.org/webservices/credentials_service.php'
IGSN_LIST_SERVICE_URL = 'http://app.geosamples.org/samples/user_code/'


class IgsnClient:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register_sample(self, sample):
        return self.register_samples([sample])[0]

    # 1. Sample registration web service
    def register_samples(self, samples):
        output = StringIO.StringIO()
        output.write('<samples>')
        for sample in samples:
            sample.export(output, 0)
        
        output.write('</samples>')
        
        # This is really poor but for some reason the XSD describes the sample as "sampleType" but the API expects it to be called "sample"
        output_xml = output.getvalue().replace('<sampleType>', '<sample>').replace('</sampleType>', '</sample>')
        
        print output.getvalue()

        http_body = urllib.urlencode({
            'username': self.username,
            'password': self.password,
            'content': output_xml
        })

        http_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        req = urllib2.Request(SAMPLE_REGISTRATION_SERVICE_URL, http_body, http_headers)
        try:
            handler = urllib2.urlopen(req)
            # handler.getcode()
            # handler.headers.getheader('content-type')

            # <results> <status>message</status><igsn>XXXX</igsn><status>message</status><igsn>XXXX</igsn> </results>
            result = handler.read()
            results_elem = eTree.fromstring(result)

            igsns = []
            for child in results_elem:
                if child.tag == 'igsn':
                    igsns.append(child.text)

            return igsns

        except urllib2.HTTPError as httpError:
            # This might happen, for example, if the sample ID already exists.
            print httpError.read()

    # 2. Credential web service
    def get_user_codes(self):
        http_body = urllib.urlencode({
            'username': self.username,
            'password': self.password
        })

        http_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        req = urllib2.Request(CREDENTIAL_SERVICE_URL, http_body, http_headers)
        handler = urllib2.urlopen(req)

        # handler.getcode()
        # <results><valid>yes</valid><user_codes><user_code>IEXXX</user_code></user_codes></results>
        result = handler.read()

        results_elem = eTree.fromstring(result)

        valid = False
        user_codes = []
        for child in results_elem:
            if child.tag == 'valid':
                valid = child.text == 'yes'
            elif child.tag == 'user_codes':
                for user_code_elem in child:
                    user_codes.append(user_code_elem.text)

        return {'valid': valid, 'user_codes': user_codes}

    # 3. SESAR IGSN list web service for specific user code
    @staticmethod
    def list_igsns(user_code, limit=None, page_no=None):
        # Build the constraint if limit is set.
        # Only add the page number if limit is set too.
        constraint = ''
        if limit is not None:
            constraint = "?limit=" + str(limit)
            if page_no is not None:
                constraint += "&page_no=" + str(page_no)

        query = IGSN_LIST_SERVICE_URL + user_code + constraint

        http_headers = {'Accept': 'application/xml'}
        req = urllib2.Request(query, None, http_headers)
        handler = urllib2.urlopen(req)

        """
            Example response:
            <samples>
                <sample>
                    <igsn>IEXXX0001</igsn>
                    <url>http://app.geosamples.org/webservices/display.php?igsn=IEXXX0001</url>
                </sample>
                ...
            </samples>
        """

        # TODO: Make robust
        # handler.getcode()
        result = handler.read()

        samples_elem = eTree.fromstring(result)

        igsns = []

        for sample_elem in samples_elem:
            for elem in sample_elem:
                if elem.tag == 'igsn':
                    igsn = elem.text
                elif elem.tag == 'url':
                    url = elem.text
                else:
                    # TODO: Make a better error
                    raise Exception("Error")

            if igsn and url:
                igsns.append({'igsn': igsn, 'url': url})

        return igsns