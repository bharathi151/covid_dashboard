import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.get_districts_cumulative_report_day_wise_interactor import DistrictsCumulativeDetailsInteractor
from covid_dashboard.presenters.presenter_implementation import PresenterImplementation
from covid_dashboard.storages.state_storage_implementation import StorageImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = DistrictsCumulativeDetailsInteractor(
        storage = storage,
        presenter = presenter
    )

    response = interactor.get_day_wise_districts_cumulative_details()

    response_data = json.dumps(response)
    return HttpResponse(response_data, status=200)
    # ---------MOCK IMPLEMENTATION---------

