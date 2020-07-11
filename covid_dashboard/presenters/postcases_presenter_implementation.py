from typing import List
from django.http import response
from django_swagger_utils.drf_server.exceptions import (
    NotFound, BadRequest
)
from covid_dashboard.constants.exception_messages import *
from covid_dashboard.interactors.presenters.presenter_interface import \
    PostCasesPresenterInterface
from covid_dashboard.interactors.storages.dtos import PostCasesDetailsDto


class PostCasesPresenterImplementation(PostCasesPresenterInterface):
    def raise_invalid_cases_details(self) -> response.HttpResponse:
        from covid_dashboard.constants.exception_messages import \
            INVALID_CASES_DEATILS
        import json
        data = json.dumps({
                "response": INVALID_CASES_DEATILS[0],
                "http_status_code": 400,
                "res_status": INVALID_CASES_DEATILS[1]
            })

        response_object = response.HttpResponse(data, 400)
        return response_object


    def post_cases_details_response(self, stats_dto: PostCasesDetailsDto):
        return stats_dto.__dict__

    def raise_invalid_mandal_id_exception(self):
        from covid_dashboard.constants.exception_messages import \
            INVALID_MANDAL
        import json
        data = json.dumps({
                "response": INVALID_MANDAL[0],
                "http_status_code": 404,
                "res_status": INVALID_MANDAL[1]
            })
        response_object = response.HttpResponse(data, 404)
        return response_object

    def raise_date_already_existed(self):
        raise BadRequest(*DATA_ALREADY_EXISTED)