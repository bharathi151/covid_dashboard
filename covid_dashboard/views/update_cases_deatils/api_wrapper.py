import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.update_cases_details_interactor import UpdateCasesDetailsInteractor
from covid_dashboard.presenters.presenter_implementation import PresenterImplementation
from covid_dashboard.storages.user_storage_implementation import StorageImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    query_params = kwargs['request_query_params'].__dict__
    date = query_params["date"]
    mandal_id = kwargs['mandal_id']
    request_data = kwargs['request_data']
    confirmed_cases = request_data['confirmed_cases']
    deaths = request_data['deaths']
    recovered_cases = request_data['recovered_cases']

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = UpdateCasesDetailsInteractor(
        storage = storage,
        presenter = presenter
    )

    interactor.update_cases_details(
        mandal_id=mandal_id,
        date=date,
        confirmed_cases=confirmed_cases,
        deaths=deaths,
        recovered_cases=recovered_cases)

    return HttpResponse(status=200)
    # ---------MOCK IMPLEMENTATION---------
