import json


def json_posts():
    with open('static/posts.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
        return posts


def post_pk(pk):
    posts = load_posts()
    for post in posts:
        if post['pk'] == pk:
            return post
    return f'Такого поста нет'