import urllib
import urllib2
import xml.etree.ElementTree as eTree

SAMPLE_REGISTRATION_SERVICE_URL = 'http://app.geosamples.org/webservices/uploadservice.php'
CREDENTIAL_SERVICE_URL = 'http://app.geosamples.org/webservices/credentials_service.php'
IGSN_LIST_SERVICE_URL = 'http://app.geosamples.org/samples/user_code/'


class Samples:
    def __init__(self, samples):
        self.samples_elem = eTree.Element('samples')

        for sample in samples:
            self.samples_elem.append(sample.sample_elem)

    def to_xml(self):
        return eTree.tostring(self.samples_elem, encoding='utf8')


class IgsnClient:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register_sample(self, sample):
        samples = Samples([sample])
        self.register_samples(samples)

    # 1. Sample registration web service
    def register_samples(self, samples):
        http_body = urllib.urlencode({
            'username': self.username,
            'password': self.password,
            'content': samples.to_xml()
        })

        http_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        req = urllib2.Request(SAMPLE_REGISTRATION_SERVICE_URL, http_body, http_headers)
        try:
            handler = urllib2.urlopen(req)
            print handler.getcode()
            print handler.headers.getheader('content-type')
            print handler.read()

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
    # TODO: must accept no limit or page_no
    @staticmethod
    def list_igsns(user_code, limit, page_no):
        query = IGSN_LIST_SERVICE_URL + '{0}?limit={1}&page_no={2}'.format(user_code, limit, page_no)

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