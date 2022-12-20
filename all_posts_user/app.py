from flask import render_template, Blueprint, request
import utils


all_posts_user_blueprint = Blueprint("all_posts_user_blueprint", __name__, template_folder='templates')
file_posts = "static/posts.json"
file_comments = "static/comments.json"
file_bookmarks = "templates/bookmarks.json"


@all_posts_user_blueprint.route("/users/<user_name>/")
#  выводит все посты выбранного пользователя
def user_posts(user_name):
    posts = utils.get_posts_by_user(user_name)


    return render_template("user-feed.html", posts=posts, user_name=user_name)
