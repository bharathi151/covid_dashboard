import pytest
from django_swagger_utils.drf_server.exceptions import NotFound

from covid_dashboard.constants.exception_messages import INVALID_MANDAL
from covid_dashboard.presenters.presenter_implementation import PresenterImplementation


def test_raise_invalid_mandal_id_exception():
    json_presenter = PresenterImplementation()
    exception_message = INVALID_MANDAL[0]
    exception_res_status = INVALID_MANDAL[1]
    with pytest.raises(NotFound) as exception:
        json_presenter.raise_invalid_mandal_id_exception()

    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status
