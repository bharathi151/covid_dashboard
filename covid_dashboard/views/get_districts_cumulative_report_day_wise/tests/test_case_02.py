"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from covid_dashboard.factories import *

REQUEST_BODY = """

"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["read", "write"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase02GetDistrictsCumulativeReportDayWiseAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase02GetDistrictsCumulativeReportDayWiseAPITestCase, self).setupUser(
            username=username, password=password
        )
        from django.db.models import Sum
        state = StateFactory()
        districts = DistrictFactory.create_batch(state=state, size=2)
        mandal_1 = MandalFactory(district=districts[0])
        mandal_2 = MandalFactory(district=districts[1])

    def test_case(self):
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.