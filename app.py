from flask import Flask
from ribbon.app import ribbon_blueprint
from post.app import post_blueprint
from search.app import search_blueprint
from all_posts_user.app import all_posts_user_blueprint

app = Flask(__name__)
app.register_blueprint(ribbon_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(all_posts_user_blueprint)


app.run()
