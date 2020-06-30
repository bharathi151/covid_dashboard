from typing import List
from gyaan.adapters.service_adapter import get_service_adapter
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.presenters.dtos import *
from gyaan.constants.exceptions import *

class GetPostsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_posts_wrapper(self, 
                           presenter: PresenterInterface,
                           post_ids: List[int]
                ):
        self.presenter = presenter
        try:
            complete_posts_dto = self.get_posts(post_ids=post_ids)
        except InvalidPostIds as error:
            return self.presenter.raise_invalid_post_ids(error)
        return self.presenter.get_posts_response(
            complete_posts_dto=complete_posts_dto
        )

    def get_posts(self, post_ids: List[int]):
        unique_post_ids = list(set(post_ids))
        invalid_post_ids = self.storage.get_invalid_post_ids(
            post_ids=unique_post_ids
        )
        if invalid_post_ids:
            raise InvalidPostIds(invalid_post_ids=invalid_post_ids)
        post_dtos = self.storage.get_posts_dtos(post_ids=unique_post_ids)
        post_tags_dtos = self.storage.get_posts_tags_dtos(post_ids=unique_post_ids)
        tag_ids = [tag.tag_id for tag in post_tags_dtos]
        tag_dtos = self.storage.get_tags_dtos(tag_ids=tag_ids)

        post_reaction_counts_dtos = self.storage.get_posts_reactions_count(post_ids=unique_post_ids)
        posts_comment_counts_dtos = self.storage.get_posts_comments_count(
            post_ids=unique_post_ids
        )

        comment_ids = self._get_latest_comment_ids(post_ids=unique_post_ids)

        comment_reaction_counts_dtos = \
            self.storage.get_comment_reactions_count(comment_ids=comment_ids)

        comment_replies_counts_dtos = \
            self.storage.get_comment_replies_count(comment_ids=comment_ids)

        comment_dtos = self.storage.get_comment_details_dtos(
            comment_ids=comment_ids
        )

        user_ids = [post_dto.posted_by_id for post_dto in post_dtos if post_dto.posted_by_id]
        user_ids += [
            comment_dto.commented_by_id for comment_dto in comment_dtos if comment_dto.commented_by_id
        ]
        user_ids += [
            comment_dto.approved_by
            for comment_dto in comment_dtos if comment_dto.approved_by
        ]
        user_ids = list(set(user_ids))
        service_adapter = get_service_adapter()
        user_dtos = service_adapter.auth_service.get_user_dtos(
            user_ids=user_ids
        )

        complete_posts_dto = CompletePostDetailsDto(
            post_dtos=post_dtos,
            post_reaction_counts=post_reaction_counts_dtos,
            comment_counts=posts_comment_counts_dtos,
            comment_reaction_counts=comment_reaction_counts_dtos,
            reply_counts=comment_replies_counts_dtos,
            comment_dtos=comment_dtos,
            post_tag_ids=tag_ids,
            tags=tag_dtos,
            users_dtos=user_dtos
        )
        return complete_posts_dto

    def _get_latest_comment_ids(self, post_ids):
        comment_ids = []
        for post_id in post_ids:
            comment_ids += self.storage.get_latest_comment_ids(
                post_id=post_id, no_of_comments=2
            )
        return comment_ids