import json


def get_posts_all():
    with open('./data/posts.json', 'r', encoding='utf-8') as f:
        posts_all = json.load(f)
    return posts_all


def get_post_by_pk(pk):
    posts = get_posts_all()

    for post in posts:
        if post['pk'] == pk:
            return post

    return f'пост не найден'
