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

def test_get_posts_with_duplicate_post_ids_return_unique_posts_details(
    get_response, posts_dtos, user_dtos_without_duplication,
    posts_comments_count_dtos,posts_reaction_counts_dtos,
    comment_replies_counts_dtos, comments_reactions_counts_dtos,
    comment_dtos, post_tags_dtos, tag_dtos):
    #arrange
    post_ids = [1, 1]
    unique_post_ids = [1]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    expected_output = get_response
    post_tags_dtos = post_tags_dtos
    tag_ids = [1]
    tag_dtos = tag_dtos
    posts_dtos = posts_dtos
    posts_reaction_counts_dtos = posts_reaction_counts_dtos
    posts_comments_count_dtos = posts_comments_count_dtos
    comments_reactions_counts_dtos = comments_reactions_counts_dtos
    comment_replies_counts_dtos = comment_replies_counts_dtos
    comment_dtos = comment_dtos
    user_dtos = user_dtos_without_duplication
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

def test_get_posts_with_out_duplicate_post_ids_return_all_posts_details(
        get_response, posts_dtos, user_dtos,
        posts_comments_count_dtos,posts_reaction_counts_dtos,
        comment_replies_counts_dtos, comments_reactions_counts_dtos,
        comment_dtos_approved_by_user, post_tags_dtos, tag_dtos,
        complete_posts_dto
    ):
    #arrange
    post_ids = [1]
    unique_post_ids = [1]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    expected_output = get_response
    post_tags_dtos = post_tags_dtos
    tag_ids = [1]
    tag_dtos = tag_dtos
    posts_dtos = posts_dtos
    posts_dtos = posts_dtos
    posts_reaction_counts_dtos = posts_reaction_counts_dtos
    posts_comments_count_dtos = posts_comments_count_dtos
    comments_reactions_counts_dtos = comments_reactions_counts_dtos
    comment_replies_counts_dtos = comment_replies_counts_dtos
    comment_dtos = comment_dtos_approved_by_user
    user_dtos = user_dtos
    comment_ids = [1, 2]
    complete_posts_dto = complete_posts_dto
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

def test_get_posts_with_duplicate_user_ids_return_posts_details_with_unique_user_ids(
    get_response, posts_dtos, comment_dtos_approved_by_user, user_dtos,
    posts_reaction_counts_dtos, posts_comments_count_dtos, post_tags_dtos,
    comments_reactions_counts_dtos, comment_replies_counts_dtos, tag_dtos,
    complete_posts_dto
    ):
    #arrange
    post_ids = [1]
    unique_post_ids = [1]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    expected_output = get_response
    post_tags_dtos = post_tags_dtos
    tag_ids = [1]
    tag_dtos = tag_dtos
    posts_dtos = posts_dtos
    posts_dtos = posts_dtos
    posts_reaction_counts_dtos = posts_reaction_counts_dtos
    posts_comments_count_dtos = posts_comments_count_dtos
    comments_reactions_counts_dtos = comments_reactions_counts_dtos
    comment_replies_counts_dtos = comment_replies_counts_dtos
    comment_dtos = comment_dtos_approved_by_user
    user_dtos = user_dtos
    comment_ids = [1, 2]
    complete_posts_dto = complete_posts_dto

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

