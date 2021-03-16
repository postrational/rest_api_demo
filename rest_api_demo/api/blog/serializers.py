from flask_restplus import fields
from rest_api_demo.api.restplus import api

user_register = api.model('Register new user', {
    'name': fields.String(required=True, description='User name'),
    'email': fields.String(required=True, description='User email'),
    'username': fields.String(required=True, description='User username'),
    'password': fields.String(required=True, description='User password'),
    'user_type': fields.Integer(required=True, description='User type', attribute='UserType.id_user_type')
})

user_type = api.model('Register new user type', {
    'name': fields.String(required=True, description='User name')
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_blog_posts = api.inherit('Page of blog posts', pagination, {
    'items': fields.List(fields.Nested(user_register))
})

category = api.model('Blog category', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a blog category'),
    'name': fields.String(required=True, description='Category name'),
})

category_with_posts = api.inherit('Blog category with posts', category, {
    'posts': fields.List(fields.Nested(user_register))
})
