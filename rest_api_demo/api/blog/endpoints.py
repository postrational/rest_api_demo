import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.blog.serializers import blog_post
from rest_api_demo.api.blog.parsers import pagination_arguments, parser
from rest_api_demo.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('posts', description='Operations related to blog posts')


@ns.route('test/<test>')
class TestResource(Resource):

    @api.expect(parser, validate=True)
    def get(self):
        args = parser.parse_args(request)
        return args


@ns.route('/<id>')
class PostsCollection(Resource):

    @api.expect(pagination_arguments, validate=True)
    def get(self):
        """
        Returns list of blog posts.
        """
        args = pagination_arguments.parse_args(request)
        return args

    @api.expect(blog_post)
    def post(self):
        """
        Creates a new blog post.
        """
        api.abort(403)


@ns.route('postman')
class TestResource(Resource):

    @api.expect(parser, validate=True)
    def get(self):
        urlvars = False  # Build query strings in URLs
        swagger = True  # Export Swagger specifications
        data = api.as_postman(urlvars=urlvars, swagger=swagger)
        return data
