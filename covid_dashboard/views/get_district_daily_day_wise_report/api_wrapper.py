import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.get_district_daily_report_day_wise_interactor import DistrictDailyDetailsInteractor
from covid_dashboard.presenters.presenter_implementation import PresenterImplementation
from covid_dashboard.storages.district_storage_implementation import StorageImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    query_params = kwargs['request_query_params'].__dict__
    district_id = kwargs["district_id"]
    date = query_params["date"]


    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = DistrictDailyDetailsInteractor(
        storage = storage,
        presenter = presenter
    )

    response = interactor.get_day_wise_district_daily_details(till_date=date, district_id=district_id)

    response_data = json.dumps(response)
    return HttpResponse(response_data, status=200)
    # ---------MOCK IMPLEMENTATION---------

