import pytest
from django_swagger_utils.drf_server.exceptions import Unauthorized

from covid_dashboard.constants.exception_messages import INVALID_PASSWORD
from covid_dashboard.presenters.presenter_implementation import PresenterImplementation


def test_raise_invalid_password_exception():
    json_presenter = PresenterImplementation()
    exception_message = INVALID_PASSWORD[0]
    exception_res_status = INVALID_PASSWORD[1]
    with pytest.raises(Unauthorized) as exception:
        json_presenter.raise_invalid_password_exception()

    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status
