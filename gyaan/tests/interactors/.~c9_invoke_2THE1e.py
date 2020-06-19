import datetime
import pytest
from gyaan.interactors.storages.dtos import *
from gyaan.interactors.presenters.dtos import *

@pytest.fixture()
def get_response():
    response = {
        "domain_id": 1,
        "domain_name": "UI/UX",
        "description": """UX design refers to the term 'user experience design',
                        while UI stands for “user interface design”.
                        Both elements are crucial to a product and
                        work closely together. But despite their professional
                        relationship, the roles themselves are quite different,
                        referring to very different aspects of the product
                        development process and the design discipline."""
    }
    return response

@pytest.fixture()
def posts_dtos():
    posts_dtos = [PostDto(
        post_id=1,
        title="The Evolution of UI/UX Designers Into Product Designers",
        content="Zero UI is a style that’s been looming in the shadow for some time",
        domian_id=1,
        posted_by_id=1,
        posted_at=datetime.datetime(2020, 3, 4, 0, 5, 23, 283000)
        )]
    return posts_dtos

@pytest.fixture()
def posts_reaction_counts_dtos():
    posts_reaction_counts_dtos = [
            PostReactionsCountDto(post_id=1, reactions_count=2)
        ]
    return posts_reaction_counts_dtos

@pytest.fixture()
def posts_comments_count_dtos():
    posts_comments_count_dtos = [
        PostCommentsCountDto(post_id=1, comments_count=2)
    ]
    return posts_comments_count_dtos

@pytest.fixture()
def comments_reactions_counts_dtos():
    comments_reactions_counts_dtos = [
        CommentReactionsCountDto(comment_id=1, reactions_count=2),
        CommentReactionsCountDto(comment_id=2, reactions_count=1)
    ]
    return comments_reactions_counts_dtos

@pytest.fixture()
def comment_replies_counts_dtos():
    comment_replies_counts_dtos = [
        CommentRepliesCountDto(comment_id=1, replies_count=2),
        CommentRepliesCountDto(comment_id=2, replies_count=1)
    ]
    return comment_replies_counts_dtos

@pytest.fixture()
def comment_dtos():
    comment_dtos = [
        CommentDto(
            comment_id=1,
            post_id=1,
            commented_at=datetime.datetime(2020, 3, 5, 0, 4, 10, 25200),
            commented_by_id=2,
            content="""Zero UI is a style that’s been looming in the shadow
                       for some time, but is just now emerging. The idea is
                       easy to understand — the less the user has to think
                       about the interface, the better and more natural it
                       feels. John Brownlee explains the specifics,and how this
                       style is changing everything.""",
            approved_by=4
        ),
        CommentDto(
            comment_id=2,
            post_id=1,
            commented_at=datetime.datetime(2020, 3, 6, 0, 5, 23, 261000),
            commented_by_id=3,
            content="""IS SIMPLICITY A real thing? Or is design the pursuit of
                       something else entirely? A Logic 101 professor once
                       explained to the class I was in that a major factorin
                       screaming matches between people is the lack of a shared
                       definition of a key term.""",
            approved_by=None
        )
        
    ]
    return comment_dtos

@pytest.fixture()
def comment_dtos_approved_by_user():
    comment_dtos=[
        CommentDto(
            comment_id=1,
            post_id=1,
            commented_at=datetime.datetime(2020, 3, 5, 0, 4, 10, 25200),
            commented_by_id=2,
            content="""Zero UI is a style that’s been looming in the shadow
                       for some time, but is just now emerging. The idea is
                       easy to understand — the less the user has to think
                       about the interface, the better and more natural it
                       feels. John Brownlee explains the specifics,and how this
                       style is changing everything.""",
            approved_by=1
        ),
        CommentDto(
            comment_id=2,
            post_id=1,
            commented_at=datetime.datetime(2020, 3, 6, 0, 5, 23, 261000),
            commented_by_id=3,
            content="""IS SIMPLICITY A real thing? Or is design the pursuit of
                       something else entirely? A Logic 101 professor once
                       explained to the class I was in that a major factorin
                       screaming matches between people is the lack of a shared
                       definition of a key term.""",
            approved_by=None
        )
        
    ]
    return comment_dtos

@pytest.fixture()
def user_dtos_without_duplication():
    user_dtos = [
        UserDto(name="user1", user_id=1, profile_pic="url1"),
        UserDto(name="user2", user_id=2, profile_pic="url2"),
        UserDto(name="user3", user_id=3, profile_pic="url3"),
        UserDto(name="user4", user_id=4, profile_pic="url4")
    ]
    return user_dtos

@pytest.fixture()
def user_dtos():
    user_dtos = [
        UserDto(name="user1", user_id=1, profile_pic="url1"),
        UserDto(name="user2", user_id=2, profile_pic="url2"),
        UserDto(name="user3", user_id=3, profile_pic="url3")
    ]
    return user_dtos

@pytest.fixture()
def post_tags_dtos():
     post_tags_dtos = [PostTagDto(post_id=1, tag_id=1)]
     return post_tags_dtos

@pytest.fixture()
def tag_dtos():
    tag_dtos = [TagDto(tag_id=1, name="ui")]
    return tag_dtos

@pytest.fixture()
def complete_posts_dto(posts_dtos, comments_reactions_counts_dtos,
                       posts_comments_count_dtos,posts_reaction_counts_dtos,
                       comment_replies_counts_dtos, tag_dtos, user_dtos,
                       comment_dtos_approved_by_user
                       ):
    complete_posts_dto = CompletePostDetailsDto(
            post_dtos=posts_dtos,
            post_reaction_counts=posts_reaction_counts_dtos,
            comment_counts=posts_comments_count_dtos,
            comment_reaction_counts=comments_reactions_counts_dtos,
            reply_counts=comment_replies_counts_dtos,
            comment_dtos=comment_dtos_approved_by_user,
            post_tag_ids=[1],
            tags=tag_dtos,
            users_dtos=user_dtos
        )
    return complete_posts_dto

@pytest.fixture()
def domain_dto():
    domain_dto = DomainDto(
        name="UI/Ux",
        domain_id=1,
        description="""UX design refers to the term 'user experience design',
                        while UI stands for “user interface design”.
                        Both elements are crucial to a product and
                        work closely together. But despite their professional
                        relationship, the roles themselves are quite different,
                        referring to very different aspects of the product
                        development process and the design discipline."""
    )
    return domain_dto

@pytest.fixture()
def experts_dtos():
    experts_dtos = [
        UserDto(name="user1", user_id=1, profile_pic="url1"),
        UserDto(name="user2", user_id=2, profile_pic="url2")
    ]
    return experts_dtos

@pytest.fixture()
def domain_details_dto(experts_dtos):
    domain_stats_dto = DomainStatsDto(
            domain_id=1,
            posts_count=1,
            followers_count=3,
            bookmarks_count=3
        )
    experts_dtos = experts_dtos
    requests_dtos = [
        RequestDto(request_id=1,user_id=3),
        RequestDto(request_id=2,user_id=4)
    ]
    requested_user_dtos = [
        UserDto(name="user3", user_id=3, profile_pic="url3"),
        UserDto(name="user4", user_id=4, profile_pic="url4")
    ]
    user_id = 1
    is_user_domain_expert = True
    domain_details_dto = DomainDetailsDto(
        domain=domain_dto,
        domain_stats=domain_stats_dto,
        domain_experts=experts_dtos,
        user_id=user_id,
        is_user_domain_expert=is_user_domain_expert,
        join_requests=requests_dtos,
        requested_users=requested_user_dtos
    )
    return