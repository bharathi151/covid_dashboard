import datetime
from dataclasses import dataclass
from typing import Optional, List

@dataclass()
class DomainDto:
    name: str
    domain_id: int
    description: str

@dataclass()
class UserDto:
    name: str
    user_id: int
    profile_pic: str

@dataclass()
class DomainStatsDto:
    domain_id: int
    posts_count: int
    followers_count: int
    bookmarks_count: int

@dataclass()
class RequestDto:
    request_id: int
    user_id: int

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
class PostDto:
    post_id: int
    title: str
    content: str
    domian_id: int
    posted_by_id: int
    posted_at: datetime.datetime


@dataclass()
class CommentDto:
    comment_id: int
    post_id: int
    commented_at: datetime.datetime
    commented_by_id: int
    content: str
    approved_by: Optional


@dataclass()
class TagDto:
    tag_id: int
    name: str


@dataclass
class PostTagDto:
    post_id: int
    tag_id: int


@dataclass
class PostReactionsCountDto:
    post_id: int
    reactions_count: int


@dataclass
class CommentReactionsCountDto:
    comment_id: int
    reactions_count: int


@dataclass
class PostCommentsCountDto:
    post_id: int
    comments_count: int


@dataclass
class CommentRepliesCountDto:
    comment_id: int
    replies_count: int


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
