from flask import Blueprint, jsonify
from api.utils import get_posts_all, get_post_by_pk

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/posts', methods=['GET'])
def get_posts_all_api():
    return jsonify(get_posts_all())


@api_blueprint.route('/posts/<int:post_id>', methods=['GET'])
def get_posts_by_id_api(post_id):
    return jsonify(get_post_by_pk(post_id))
