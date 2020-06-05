import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.sign_in_interactor import LogInUserInteractor
from covid_dashboard.presenters.presenter_implementation import PresenterImplementation
from covid_dashboard.storages.user_storage_implementation import StorageImplementation
from common.oauth2_storage import OAuth2SQLStorage

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    user_name = request_data['user_name']
    password = request_data['password']

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    oauth2_storage = OAuth2SQLStorage()
    interactor = LogInUserInteractor(
        storage = storage,
        presenter = presenter,
        oauth2_storage=oauth2_storage
    )

    response = interactor.log_in_user(
        user_name=user_name,
        password=password
    )

    response_data = json.dumps(response)
    return HttpResponse(response_data, status=201)
    # ---------MOCK IMPLEMENTATION---------
