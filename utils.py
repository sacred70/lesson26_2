import json
from json import JSONDecodeError
import pprint

file_posts = "static/posts.json"
file_comments = "static/comments.json"
file_bookmarks = "templates/bookmarks.json"

def read_json(file_name):
    #  чтение файла, возвращаем список
    try:
        with open(file_name, "r", encoding='utf-8') as f:
            text = json.load(f)
            return text

    except FileNotFoundError:
        # Будет выполнено, если файл не найден
        print ("Файл не найден")

    except JSONDecodeError:
        # Будет выполнено, если файл найден, но не превращается из JSON
        print("Файл не удается преобразовать")


def get_posts_by_user(user_name):
    # возвращает список постов пользователя
    posts = read_json(file_posts)
    user_posts = []
    search = 0  #  определяет наличие автора
    for post in posts:
        if post['poster_name'].lower() == user_name.lower():
            user_posts.append(post)
            search = 1
    if search == 0:
        return "ERROE ValueError" #  ДОРАБОТАТЬ ОШИБКУ КАК ДОЛЖНО БЫТЬ
    return user_posts


def get_comments_by_post_id(post_id):
    #  возвращает список коментариев по номеру поста
    list_comments = read_json(file_comments)
    comments = []
    #search = 0  # определяет наличие
    for comment in list_comments:

        if comment["post_id"] == post_id:
            comments.append(comment)
            search = 1
    '''
    
        return "ERROR ValueError"  
        '''
    return comments


def search_for_posts(query):
    #  возвращает список постов по ключевому слову
    posts = read_json(file_posts)
    list_posts = []
    count = 0
    for post in posts:
        if query in post["content"] and count<10:
            list_posts.append(post)
            count+=1
    return list_posts


def get_post_by_pk(pk):
    #  возвращает пост по рк
    posts = read_json(file_posts)
    for post in posts:
        if pk == post["pk"]:
            return post

