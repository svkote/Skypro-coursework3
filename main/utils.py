import json

from main.post import Post
from main.comment import Comment


def get_posts_all() -> list:
    """Возвращает все посты"""
    post_list = []

    with open('data/posts.json', 'r', encoding='utf-8') as file:
        posts_data = json.load(file)

    for post in posts_data:
        post_list.append(Post(
            post['poster_name'],
            post['poster_avatar'],
            post['pic'],
            post['content'],
            post['views_count'],
            post['likes_count'],
            post['pk']
        ))

    return post_list


def get_posts_by_user(user_name) -> list:
    """Возвращает посты определенного пользователя.
    Функция должна вызывать ошибку `ValueError` если такого пользователя нет
     и пустой список, если у пользователя нет постов."""
    post_list_by_user = []
    post_list = get_posts_all()

    for post in post_list:
        if post.poster_name.lower() == user_name.lower():
            post_list_by_user.append(post)

    return post_list_by_user


def search_for_posts(query) -> list:
    """Возвращает список постов по ключевому слову"""
    search_post_list = []
    post_list = get_posts_all()

    for post in post_list:
        if query.lower() in post.content.lower():
            search_post_list.append(post)

    return search_post_list


def get_post_by_pk(pk: int):
    """Возвращает один пост по его идентификатору."""
    post_list = get_posts_all()

    for post in post_list:
        if post.pk == pk:
            return post

    return


def get_comments_all() -> list:
    """Возвращает все посты"""
    comments_list = []

    with open('data/comments.json', 'r', encoding='utf-8') as file:
        comments_data = json.load(file)

    for comment in comments_data:
        comments_list.append(Comment(
            comment['post_id'],
            comment['commenter_name'],
            comment['comment'],
            comment['pk']
        ))

    return comments_list


def get_comments_by_post_id(post_id: int) -> list:
    """Возвращает комментарии определенного поста.
    Функция должна вызывать ошибку `ValueError` если такого поста нет
    и пустой список, если у поста нет комментов."""
    search_comment_list_by_pk = []
    comment_list = get_comments_all()

    for comment in comment_list:
        if comment.pk == post_id:
            search_comment_list_by_pk.append(comment)

    return search_comment_list_by_pk
