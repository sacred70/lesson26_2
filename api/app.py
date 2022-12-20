from flask import jsonify
from flask import Blueprint
from api.utils import json_posts, post_pk
import logging


api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts', methods=['GET'])
def get_all_posts():
    #  возвращает список постов в json
    logging.basicConfig(level=logging.INFO, filename='logs/api.log', format='%(asctime)s [%(levelname)s] %(message)s')
    logging.info('Запрос api/posts')
    return jsonify(json_posts())


@api_blueprint.route('/api/posts/<int:pk>', methods=['GET'])
def get_post_by_id(pk):
    #  возвращает определенный пост в виде json
    path = f'api/posts/{pk}'
    logging.basicConfig(level=logging.INFO, filename='logs/api.log', format='%(asctime)s [%(levelname)s] %(message)s')
    logging.info(f'Запрос {path}')
    return jsonify(post_pk(pk))
