from flask import render_template, Blueprint, request
import utils

post_blueprint = Blueprint("post_blueprint", __name__, template_folder='templates')
file_posts = "static/posts.json"
file_comments = "static/comments.json"
file_bookmarks = "templates/bookmarks.json"


@post_blueprint.route("/posts/<int:pk>")
#  выводит выбраный пост
def get_post(pk):
    post = utils.get_post_by_pk(pk)
    comments = utils.get_comments_by_post_id(pk)
    len_comments = len(comments)


    return render_template("post.html", post=post, comments=comments, len_comments=len_comments)