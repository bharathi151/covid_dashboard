from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.constants.exceptions import *

class DomainPostsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_posts_wrapper(self, presenter: PresenterInterface,
                                 user_id: int, domain_id: int,
                                 limit: int, offset: int):
        try:
            posts_complete_details_dtos = self.get_domain_posts(
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
        return presenter.get_domain_posts_response(posts_complete_details_dtos=posts_complete_details_dtos)

    def get_domain_posts(self, user_id: int, domain_id: int,
                         offset: int, limit: int):
        is_invalid_domain_id = not self.storage. \
                is_valid_domain_id(domain_id=domain_id)
        if is_invalid_domain_id:
            raise InvalidDomainId

        is_user_not_domain_member = not self.storage. \
                is_user_domain_follower(domain_id=domain_id, user_id=user_id)
        if is_user_not_domain_member:
            raise UserNotDomainFollower
        is_invalid_limit = limit <= 0
        if is_invalid_limit:
            raise InvalidLimit(invalid_limit=limit)

        is_invalid_offset = offset < 0
        if is_invalid_offset:
            raise InvalidOffset(invalid_offset=offset)
        post_ids = self.storage.get_domain_post_ids(
                domain_id=domain_id, offset=offset, limit=limit
            )

        from gyaan.interactors.get_posts_interactor import GetPostsInteractor
        get_post_interactor = GetPostsInteractor(storage=self.storage)

        return get_post_interactor.get_posts(post_ids=post_ids)
