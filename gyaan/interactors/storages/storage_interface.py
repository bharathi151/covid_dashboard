from abc import ABC
from abc import abstractmethod
from typing import List
from gyaan.interactors.storages.dtos import *
from gyaan.interactors.presenters.dtos import *

class StorageInterface(ABC):
    @abstractmethod
    def is_valid_domain_id(self, domain_id) -> bool:
        pass

    @abstractmethod
    def is_user_domain_follower(self, domain_id: int, user_id: int) -> bool:
        pass

    @abstractmethod
    def get_domain_dto(self, domain_id) -> DomainDto:
        pass

    @abstractmethod
    def get_domain_experts_ids(self, domain_id: int) -> List[int]:
        pass

    @abstractmethod
    def get_domain_experts_dtos(self, experts_ids: List[int]) -> List[UserDto]:
        pass

    @abstractmethod
    def get_users_details_dtos(self, user_ids: List[int]) -> List[UserDto]:
        pass

    @abstractmethod
    def is_user_domain_expert(self, domain_id: int, user_id: int) -> bool:
        pass

    @abstractmethod
    def get_domain_join_requests(self, domain_id: int)  -> List[RequestDto]:
        pass
    @abstractmethod
    def get_domain_stats_dto(self, domain_id: int) -> DomainStatsDto:
        pass

    @abstractmethod
    def get_invalid_post_ids(self, post_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_posts_dtos(self, post_ids: List[int]) -> List[PostDto]:
        pass

    @abstractmethod
    def get_posts_tags_dtos(self, post_ids: List[int]) -> List[PostTagDto]:
        pass

    @abstractmethod
    def get_tags_dtos(self, tag_ids: List[int]) -> List[TagDto]:
        pass

    @abstractmethod
    def get_posts_reactions_count(self, post_ids: List[int]) -> List[PostReactionsCountDto]:
        pass

    @abstractmethod
    def get_posts_comments_count(self, post_ids: List[int]) -> List[PostCommentsCountDto]:
        pass

    @abstractmethod
    def get_latest_comment_ids(
                self, post_id: int, no_of_comments: int) -> List[int]:
        pass

    @abstractmethod
    def get_comment_reactions_count(self, comment_ids: List[int]) -> List[CommentReactionsCountDto]:
        pass

    @abstractmethod
    def get_comment_replies_count(self, comment_ids: List[int]) -> List[CommentRepliesCountDto]:
        pass

    @abstractmethod
    def get_comment_details_dtos(self, comment_ids: List[int]) -> List[CommentDto]:
        pass


