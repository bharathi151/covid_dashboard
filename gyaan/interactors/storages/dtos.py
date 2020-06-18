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
