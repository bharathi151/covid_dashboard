import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.get_district_cumulative_report_day_wise_interactor import DistrictCumulativeDetailsInteractor
from covid_dashboard.presenters.presenter_implementation import PresenterImplementation
from covid_dashboard.storages.district_storage_implementation import StorageImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    district_id = kwargs["district_id"]
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = DistrictCumulativeDetailsInteractor(
        storage = storage,
        presenter = presenter
    )

    response = interactor.get_day_wise_district_cumulative_details(district_id=district_id)

    response_data = json.dumps(response)
    return HttpResponse(response_data, status=200)
    # ---------MOCK IMPLEMENTATION---------
