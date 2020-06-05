import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest

from covid_dashboard.constants.exception_messages import DATA_ALREADY_EXISTED
from covid_dashboard.presenters.presenter_implementation import PresenterImplementation


def test_raise_date_already_existed():
    json_presenter = PresenterImplementation()
    exception_message = DATA_ALREADY_EXISTED[0]
    exception_res_status = DATA_ALREADY_EXISTED[1]
    with pytest.raises(BadRequest) as exception:
        json_presenter.raise_date_already_existed()

    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status
