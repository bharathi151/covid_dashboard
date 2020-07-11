import pytest
import json
from django_swagger_utils.drf_server.exceptions import NotFound

from covid_dashboard.constants.exception_messages import INVALID_MANDAL
from covid_dashboard.presenters.postcases_presenter_implementation import PostCasesPresenterImplementation


def test_raise_invalid_mandal_id_exception():
    json_presenter = PostCasesPresenterImplementation()
    exception_message = INVALID_MANDAL[0]
    exception_res_status = INVALID_MANDAL[1]

    response = json_presenter.raise_invalid_mandal_id_exception()

    data = json.loads(response.content)
    assert data['response'] == exception_message
    assert data["res_status"] == exception_res_status
    assert data["http_status_code"] == 404
