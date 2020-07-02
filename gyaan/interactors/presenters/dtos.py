import datetime
from dataclasses import dataclass
from typing import Optional, List
from gyaan.interactors.storages.dtos import *

@dataclass()
class DomainDetailsDto:
    domain: DomainDto
    domain_stats: DomainStatsDto
    domain_experts: List[UserDto]
    user_id: int
    is_user_domain_expert: bool
    join_requests: List[RequestDto]
    requested_users: List[UserDto]

@dataclass()
class CompletePostDetailsDto:
    post_dtos: List[PostDto]
    post_reaction_counts: List[PostReactionsCountDto]
    comment_reaction_counts: List[CommentReactionsCountDto]
    comment_counts: List[PostCommentsCountDto]
    reply_counts: List[CommentRepliesCountDto]
    comment_dtos: List[CommentDto]
    post_tag_ids: List[PostTagDto]
    tags: List[TagDto]
    users_dtos: List[UserDto]

@dataclass()
class DomainDetailsWithPostsDto:
    domain_details: DomainDetailsDto
    post_details: CompletePostDetailsDto
