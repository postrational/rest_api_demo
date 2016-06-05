from flask_restplus import fields
from rest_api_demo.api.restplus import api

blog_post = api.model('BlogPost', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a blog post'),
    'title': fields.String(required=True, description='Article title'),
    'slug': fields.String(required=True, pattern='^[a-z0-9-]+$'),
    'excerpt': fields.String(description='Short excerpt of article'),
    'content': fields.String(required=True, description='Article content'),
    'status': fields.String(required=True, enum=['DRAFT', 'PUBLISHED', 'DELETED']),
})
