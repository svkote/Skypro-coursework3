from flask import render_template, request, Blueprint
from main.utils import *

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
posts = get_posts_all()
comments = get_comments_all()


@main_blueprint.route('/')
def page_index():
    return render_template('index.html', posts=posts)


@main_blueprint.route('/posts/<int:post_id>')
def page_post(post_id):
    found_post = get_post_by_pk(post_id)
    comments_found_post = get_comments_by_post_id(post_id)
    return render_template('post.html', post=found_post, comments=comments_found_post)


# @main_blueprint.route('/search', method=['GET'])
# def page_search():
#     query = request.args.get('s')
#     found_posts = search_for_posts(query)
#     return render_template('search.html', posts=found_posts)
