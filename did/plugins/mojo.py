import base64
import re
import urllib2
import urllib

import datetime

# count
# after
# then loop through until we find an event that's
# older than the UNTIL date

#after = utils.dt_parse('2015-10-01T01:01:01.45+0000')
# FIXME: force utc timezone aware!
# Get rid of hard-coded +0000
after = datetime.datetime.utcnow().strftime('%Y-%m-%dT%I:%M:%S.0+0000')

user_id = 4050
endpoint = "/api/core/v3/people/{0}/activities?"
base_url = "https://mojo.redhat.com"
url = base_url + endpoint.format(user_id)

user = "cward"
password = ""

user_pass = base64.encodestring('%s:%s' % (user, password)).replace("\n", "")
auth = "Basic " + user_pass

headers = {"Authorization": auth}
request = urllib2.Request(url, None, headers)

data = {
    'count': 5,
    'after': after,
}
data = urllib.urlencode(data)

full_url = url + data

def load(request, data):
    try:
        _json = urllib2.urlopen(request).read()
        return _json
    except urllib2.HTTPError, e:
        print e.code
        print e.read()
        raise

_json = load(request, data)

# Remove the security string from the top of the response
_json = re.sub(r"^throw.*;\s*", "", _json)

class MojoApi(object):
    """ MojoAPI investigator """

    def __init__(self):
        """ Initialize MojoAPI """
        pass

    @staticmethod
    def user_history(user, stats):
        """ Perform issue search for given stats instance """
        #log.debug("User History: {0}".format(user))
        pass



#if __name__ == "__main__":
    #args = {'filter': 'author(http://mojo.redhat.com/api/core/v3/people/cward'}
    #m = MojoApi()
    #m.user_history()
