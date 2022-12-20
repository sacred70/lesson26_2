import pytest
from api.utils import json_posts, post_pk


def test_load_posts():
    assert type(json_posts()) == list


list_keys = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']


def test_keys_json_posts():
    for post in json_posts():
        keys = [key for key in post.keys()]
        assert keys == list_keys


def test_post_pk():
    for i in range(1, 8):
        assert type(post_pk(i)) == dict


def test_keys_post_pk():
    for i in range(1, 8):
        keys = [key for key in post_pk(i).keys()]
        assert keys == list_keys
