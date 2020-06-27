"""
Raise Data Alreay existed Exception when already data existed with that mandal_id and date
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from covid_dashboard.factories import *
from covid_dashboard.models.cases_details import CasesDetails

REQUEST_BODY = """
{
    "confirmed_cases": 2,
    "deaths": 1,
    "recovered_cases": 1
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"mandal_id": "1"},
        "query_params": {"date": "2020-5-30"},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase02PostCasesDeatilsAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE
    mandal_id = int(TEST_CASE["request"]["path_params"]["mandal_id"])
    date = TEST_CASE["request"]["query_params"]["date"]
    import json
    request_body_dict = json.loads(REQUEST_BODY)
    confirmed_cases = request_body_dict["confirmed_cases"]
    recovered_cases = request_body_dict["recovered_cases"]
    deaths = request_body_dict["deaths"]
    

    def setupUser(self, username, password):
        super(TestCase02PostCasesDeatilsAPITestCase, self).setupUser(
            username=username, password=password
        )
        mandal = MandalFactory()
        CasesDetailsFactory.create(mandal=mandal, date=self.date, 
                            confirmed_cases=self.confirmed_cases,
                            recovered_cases=self.recovered_cases,
                            deaths=self.deaths)

    def test_case(self):
        response = self.default_test_case()
        import json
        response_content = json.loads(response.content)

        #response_content = json.loads(response.content)
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.