#import pytest
from api.utils import json_posts, post_pk


list_keys = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']


def test_json_posts():
    # проверяем возвращается ли список
    assert type(json_posts()) == list


def test_keys_json_posts():
    # сверяем ключи
    for post in json_posts():
        # сверяем список ключей поста создавая список через генератор списков
        keys = [key for key in post.keys()]
        assert keys == list_keys


def test_post_pk():
    # проверяем возвращается ли словарь
    for i in range(1, 8):
        assert type(post_pk(i)) == dict


def test_keys_post_pk():
    # сверяем ключи
    for i in range(1, 8):
        # сверяем список ключей поста создавая список через генератор списков
        keys = [key for key in post_pk(i).keys()]
        assert keys == list_keys
