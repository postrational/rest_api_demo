from rest_api_demo.database import db
from rest_api_demo.database.models import Post, Category


def create_blog_post(data):
    title = data.get('title')
    body = data.get('body')
    category_id = data.get('category_id')
    category = Category.query.filter(Category.id == category_id).one()
    post = Post(title, body, category)
    db.session.add(post)
    db.session.commit()


def update_post(post_id, data):
    post = Post.query.filter(Post.id == post_id).one()
    post.title = data.get('title')
    post.body = data.get('body')
    category_id = data.get('category_id')
    post.category = Category.query.filter(Category.id == category_id).one()
    db.session.add(post)
    db.session.commit()


def delete_post(post_id):
    post = Post.query.filter(Post.id == post_id).one()
    db.session.delete(post)
    db.session.commit()


def create_category(data):
    name = data.get('name')
    category_id = data.get('id')

    category = Category(name)
    if category_id:
        category.id = category_id

    db.session.add(category)
    db.session.commit()


def update_category(category_id, data):
    category = Category.query.filter(Category.id == category_id).one()
    category.name = data.get('name')
    db.session.add(category)
    db.session.commit()


def delete_category(category_id):
    category = Category.query.filter(Category.id == category_id).one()
    db.session.delete(category)
    db.session.commit()
