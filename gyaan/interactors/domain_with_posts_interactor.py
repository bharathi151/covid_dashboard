from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.constants.exceptions import *
from gyaan.interactors.presenters.dtos import DomainDetailsWithPostsDto


class DomainWithPostsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_with_posts_wrapper(self, user_id: int, domain_id: int,
                                      offset: int, limit: int,
                                      presenter: PresenterInterface):
        try:
            domain_with_posts_dto = self.get_domain_with_posts(
                user_id=user_id,
                domain_id=domain_id,
                offset=offset,
                limit=limit
            )
        except InvalidDomainId:
            return presenter.raise_invalid_domain_id_exception()
        except UserNotDomainFollower:
            return presenter.raise_invalid_domain_member_exception()
        except InvalidLimit as error:
            return presenter.raise_invalid_limit_exception(error=error)
        except InvalidOffset as error:
            return presenter.raise_invalid_offset_exception(error=error)

        return presenter.get_domain_with_posts_response(
            domain_with_posts_dto=domain_with_posts_dto
        )

    def get_domain_with_posts(self, user_id: int, domain_id: int,
                              offset: int, limit: int):
        from gyaan.interactors.domain_details_interactor import \
            GetDomainDetailsInteractor
        from gyaan.interactors.domain_posts_interactor import \
            DomainPostsInteractor

        domain_details_interactor = GetDomainDetailsInteractor(
            storage=self.storage
        )

        domain_details = domain_details_interactor.get_domain_details(
            user_id=user_id,
            domain_id=domain_id
        )

        domain_posts_interactor = DomainPostsInteractor(
            storage=self.storage
        )
        domain_posts = domain_posts_interactor.get_domain_posts(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit
        )

        return DomainDetailsWithPostsDto(
            domain_details=domain_details,
            post_details=domain_posts
        )
