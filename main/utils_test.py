import pytest
from main.utils import get_posts_all, get_comments_all


expected_keys_in_post = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
expected_keys_in_comment = ['post_id', 'commenter_name', 'comment', 'pk']


def test_get_posts_all():
    assert type(get_posts_all()) == list


def test_get_comments_all():
    assert type(get_comments_all()) == list


def test_keys_in_get_post_all():
    for post in get_posts_all():
        keys = [key for key in post.__dict__]
        assert keys == expected_keys_in_post


def test_keys_in_get_comments_all():
    for comment in get_comments_all():
        keys = [key for key in comment.__dict__]
        assert keys == expected_keys_in_comment

