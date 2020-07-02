from unittest.mock import create_autospec
import datetime
import pytest

from gyaan.interactors.storages.dtos import *
from gyaan.interactors.presenters.dtos import *
from gyaan.interactors.get_posts_interactor import GetPostsInteractor
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.storages.storage_interface import StorageInterface
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest

def test_get_posts_with_invalid_post_ids_return_invalid_post_ids_exception():
    #arrange
    post_ids = [1, 2, 3]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.get_invalid_post_ids.return_value = [2, 3]
    presenter.raise_invalid_post_ids.side_effect = NotFound
    interactor = GetPostsInteractor(
        storage = storage
    )

    #act
    with pytest.raises(NotFound):
        interactor.get_posts_wrapper(
            presenter=presenter,
            post_ids=post_ids
        )

    #assert
    storage.get_invalid_post_ids.assert_called_once_with(post_ids=[1, 2, 3])
    presenter.raise_invalid_post_ids.assert_called_once()
    call_args = presenter.raise_invalid_post_ids.call_args
    call_obj = call_args.args
    error_obj = call_obj[0].invalid_post_ids
    assert error_obj == [2, 3]

def test_get_posts_with_duplicate_post_ids_return_unique_posts_details():
    #arrange
    post_ids = [1, 1]
    unique_post_ids = [1]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    expected_output = get_res
    post_tags_dtos = [PostTagDto(post_id=1, tag_id=1)]
    tag_ids = [1]
    tag_dtos = [TagDto(tag_id=1, name="ui")]
    posts_dtos = [PostDto(
        post_id=1,
        title="The Evolution of UI/UX Designers Into Product Designers",
        content="Zero UI is a style that’s been looming in the shadow for some time",
        domian_id=1,
        posted_by_id=1,
        posted_at=datetime.datetime(2020, 3, 4, 0, 5, 23, 283000)
        )]
    posts_reaction_counts_dtos = [
        PostReactionsCountDto(post_id=1, reactions_count=2)
    ]
    posts_comments_count_dtos = [
        PostCommentsCountDto(post_id=1, comments_count=2)
    ]
    comments_reactions_counts_dtos = [
        CommentReactionsCountDto(comment_id=1, reactions_count=2),
        CommentReactionsCountDto(comment_id=2, reactions_count=1)
    ]
    comment_replies_counts_dtos = [
        CommentRepliesCountDto(comment_id=1, replies_count=2),
        CommentRepliesCountDto(comment_id=2, replies_count=1)
    ]
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
    user_dtos = [
        UserDto(name="user1", user_id=1, profile_pic="url1"),
        UserDto(name="user2", user_id=2, profile_pic="url2"),
        UserDto(name="user3", user_id=3, profile_pic="url3"),
        UserDto(name="user4", user_id=4, profile_pic="url4")
    ]
    comment_ids = [1, 2]
    complete_posts_dto = CompletePostDetailsDto(
            post_dtos=posts_dtos,
            post_reaction_counts=posts_reaction_counts_dtos,
            comment_counts=posts_comments_count_dtos,
            comment_reaction_counts=comments_reactions_counts_dtos,
            reply_counts=comment_replies_counts_dtos,
            comment_dtos=comment_dtos,
            post_tag_ids=tag_ids,
            tags=tag_dtos,
            users_dtos=user_dtos
        )
    storage.get_invalid_post_ids.return_value = []
    storage.get_posts_dtos.return_value = posts_dtos
    storage.get_posts_tags_dtos.return_value = post_tags_dtos
    storage.get_tags_dtos.return_value = tag_dtos
    storage.get_posts_reactions_count.return_value = posts_reaction_counts_dtos
    storage.get_posts_comments_count.return_value = posts_comments_count_dtos
    storage.get_latest_comment_ids.return_value = comment_ids
    storage.get_comment_reactions_count.return_value = comments_reactions_counts_dtos
    storage.get_comment_replies_count.return_value = comment_replies_counts_dtos
    storage.get_comment_details_dtos.return_value = comment_dtos
    storage.get_users_details_dtos.return_value = user_dtos
    presenter.get_posts_response.return_value = expected_output

    interactor = GetPostsInteractor(
        storage = storage
    )
    #act
    response = interactor.get_posts_wrapper(
        presenter=presenter,
        post_ids=post_ids
    )

    #assert
    assert response == expected_output
    storage.get_invalid_post_ids.assert_called_once_with(post_ids=unique_post_ids)
    storage.get_posts_dtos.assert_called_once_with(post_ids=unique_post_ids)
    storage.get_posts_tags_dtos.assert_called_once_with(post_ids=unique_post_ids)
    storage.get_tags_dtos.assert_called_once_with(tag_ids=[1])
    storage.get_posts_reactions_count.assert_called_once_with(post_ids=unique_post_ids)
    storage.get_posts_comments_count.assert_called_once_with(post_ids=unique_post_ids)
    storage.get_latest_comment_ids.assert_called_once_with(post_id=1, no_of_comments=2)
    storage.get_comment_reactions_count.assert_called_once_with(comment_ids=comment_ids)
    storage.get_comment_replies_count.assert_called_once_with(comment_ids=comment_ids)
    storage.get_comment_details_dtos.assert_called_once_with(comment_ids=comment_ids)
    storage.get_users_details_dtos.assert_called_once_with(user_ids=[1, 2, 3, 4])
    presenter.get_posts_response.assert_called_once_with(complete_posts_dto=complete_posts_dto)

def test_get_posts_with_out_duplicate_post_ids_return_all_posts_details():
    #arrange
    post_ids = [1]
    unique_post_ids = [1]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    expected_output = {
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
    post_tags_dtos = [PostTagDto(post_id=1, tag_id=1)]
    tag_ids = [1]
    tag_dtos = [TagDto(tag_id=1, name="ui")]
    posts_dtos = [PostDto(
        post_id=1,
        title="The Evolution of UI/UX Designers Into Product Designers",
        content="Zero UI is a style that’s been looming in the shadow for some time",
        domian_id=1,
        posted_by_id=1,
        posted_at=datetime.datetime(2020, 3, 4, 0, 5, 23, 283000)
        )]
    posts_reaction_counts_dtos = [
        PostReactionsCountDto(post_id=1, reactions_count=2)
    ]
    posts_comments_count_dtos = [
        PostCommentsCountDto(post_id=1, comments_count=2)
    ]
    comments_reactions_counts_dtos = [
        CommentReactionsCountDto(comment_id=1, reactions_count=2),
        CommentReactionsCountDto(comment_id=2, reactions_count=1)
    ]
    comment_replies_counts_dtos = [
        CommentRepliesCountDto(comment_id=1, replies_count=2),
        CommentRepliesCountDto(comment_id=2, replies_count=1)
    ]
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
    user_dtos = [
        UserDto(name="user1", user_id=1, profile_pic="url1"),
        UserDto(name="user2", user_id=2, profile_pic="url2"),
        UserDto(name="user3", user_id=3, profile_pic="url3")
    ]
    comment_ids = [1, 2]
    complete_posts_dto = CompletePostDetailsDto(
            post_dtos=posts_dtos,
            post_reaction_counts=posts_reaction_counts_dtos,
            comment_counts=posts_comments_count_dtos,
            comment_reaction_counts=comments_reactions_counts_dtos,
            reply_counts=comment_replies_counts_dtos,
            comment_dtos=comment_dtos,
            post_tag_ids=tag_ids,
            tags=tag_dtos,
            users_dtos=user_dtos
        )
    storage.get_invalid_post_ids.return_value = []
    storage.get_posts_dtos.return_value = posts_dtos
    storage.get_posts_tags_dtos.return_value = post_tags_dtos
    storage.get_tags_dtos.return_value = tag_dtos
    storage.get_posts_reactions_count.return_value = posts_reaction_counts_dtos
    storage.get_posts_comments_count.return_value = posts_comments_count_dtos
    storage.get_latest_comment_ids.return_value = comment_ids
    storage.get_comment_reactions_count.return_value = comments_reactions_counts_dtos
    storage.get_comment_replies_count.return_value = comment_replies_counts_dtos
    storage.get_comment_details_dtos.return_value = comment_dtos
    storage.get_users_details_dtos.return_value = user_dtos
    presenter.get_posts_response.return_value = expected_output

    interactor = GetPostsInteractor(
        storage = storage
    )
    #act
    response = interactor.get_posts_wrapper(
        presenter=presenter,
        post_ids=post_ids
    )

    #assert
    assert response == expected_output
    storage.get_invalid_post_ids.assert_called_once_with(post_ids=unique_post_ids)
    storage.get_posts_dtos.assert_called_once_with(post_ids=unique_post_ids)
    storage.get_posts_tags_dtos.assert_called_once_with(post_ids=unique_post_ids)
    storage.get_tags_dtos.assert_called_once_with(tag_ids=[1])
    storage.get_posts_reactions_count.assert_called_once_with(post_ids=unique_post_ids)
    storage.get_posts_comments_count.assert_called_once_with(post_ids=unique_post_ids)
    storage.get_latest_comment_ids.assert_called_once_with(post_id=1, no_of_comments=2)
    storage.get_comment_reactions_count.assert_called_once_with(comment_ids=comment_ids)
    storage.get_comment_replies_count.assert_called_once_with(comment_ids=comment_ids)
    storage.get_comment_details_dtos.assert_called_once_with(comment_ids=comment_ids)
    storage.get_users_details_dtos.assert_called_once_with(user_ids=[1, 2, 3])
    presenter.get_posts_response.assert_called_once_with(complete_posts_dto=complete_posts_dto)

def test_get_posts_with_duplicate_user_ids_return_posts_details_with_unique_user_ids():
    #arrange
    post_ids = [1]
    unique_post_ids = [1]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    expected_output = {
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
    post_tags_dtos = [PostTagDto(post_id=1, tag_id=1)]
    tag_ids = [1]
    tag_dtos = [TagDto(tag_id=1, name="ui")]
    posts_dtos = [PostDto(
        post_id=1,
        title="The Evolution of UI/UX Designers Into Product Designers",
        content="Zero UI is a style that’s been looming in the shadow for some time",
        domian_id=1,
        posted_by_id=1,
        posted_at=datetime.datetime(2020, 3, 4, 0, 5, 23, 283000)
        )]
    posts_reaction_counts_dtos = [
        PostReactionsCountDto(post_id=1, reactions_count=2)
    ]
    posts_comments_count_dtos = [
        PostCommentsCountDto(post_id=1, comments_count=2)
    ]
    comments_reactions_counts_dtos = [
        CommentReactionsCountDto(comment_id=1, reactions_count=2),
        CommentReactionsCountDto(comment_id=2, reactions_count=1)
    ]
    comment_replies_counts_dtos = [
        CommentRepliesCountDto(comment_id=1, replies_count=2),
        CommentRepliesCountDto(comment_id=2, replies_count=1)
    ]
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
    user_dtos = [
        UserDto(name="user1", user_id=1, profile_pic="url1"),
        UserDto(name="user2", user_id=2, profile_pic="url2"),
        UserDto(name="user3", user_id=3, profile_pic="url3")
    ]
    comment_ids = [1, 2]
    complete_posts_dto = CompletePostDetailsDto(
            post_dtos=posts_dtos,
            post_reaction_counts=posts_reaction_counts_dtos,
            comment_counts=posts_comments_count_dtos,
            comment_reaction_counts=comments_reactions_counts_dtos,
            reply_counts=comment_replies_counts_dtos,
            comment_dtos=comment_dtos,
            post_tag_ids=tag_ids,
            tags=tag_dtos,
            users_dtos=user_dtos
        )
    storage.get_invalid_post_ids.return_value = []
    storage.get_posts_dtos.return_value = posts_dtos
    storage.get_posts_tags_dtos.return_value = post_tags_dtos
    storage.get_tags_dtos.return_value = tag_dtos
    storage.get_posts_reactions_count.return_value = posts_reaction_counts_dtos
    storage.get_posts_comments_count.return_value = posts_comments_count_dtos
    storage.get_latest_comment_ids.return_value = comment_ids
    storage.get_comment_reactions_count.return_value = comments_reactions_counts_dtos
    storage.get_comment_replies_count.return_value = comment_replies_counts_dtos
    storage.get_comment_details_dtos.return_value = comment_dtos
    storage.get_users_details_dtos.return_value = user_dtos
    presenter.get_posts_response.return_value = expected_output

    interactor = GetPostsInteractor(
        storage = storage
    )
    #act
    response = interactor.get_posts_wrapper(
        presenter=presenter,
        post_ids=post_ids
    )

    #assert
    assert response == expected_output
    storage.get_invalid_post_ids.assert_called_once_with(post_ids=unique_post_ids)
    storage.get_posts_dtos.assert_called_once_with(post_ids=unique_post_ids)
    storage.get_posts_tags_dtos.assert_called_once_with(post_ids=unique_post_ids)
    storage.get_tags_dtos.assert_called_once_with(tag_ids=[1])
    storage.get_posts_reactions_count.assert_called_once_with(post_ids=unique_post_ids)
    storage.get_posts_comments_count.assert_called_once_with(post_ids=unique_post_ids)
    storage.get_latest_comment_ids.assert_called_once_with(post_id=1, no_of_comments=2)
    storage.get_comment_reactions_count.assert_called_once_with(comment_ids=comment_ids)
    storage.get_comment_replies_count.assert_called_once_with(comment_ids=comment_ids)
    storage.get_comment_details_dtos.assert_called_once_with(comment_ids=comment_ids)
    storage.get_users_details_dtos.assert_called_once_with(user_ids=[1, 2, 3])
    presenter.get_posts_response.assert_called_once_with(complete_posts_dto=complete_posts_dto)

