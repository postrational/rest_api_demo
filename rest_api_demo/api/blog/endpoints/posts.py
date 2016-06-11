import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.blog.business import create_blog_post, create_category
from rest_api_demo.api.blog.serializers import blog_post, pagination, page_of_blog_posts, category
from rest_api_demo.api.blog.parsers import pagination_arguments, parser
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Post, Category

log = logging.getLogger(__name__)

ns = api.namespace('blog/posts', description='Operations related to blog posts')


@ns.route('/')
class PostsCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_blog_posts)
    def get(self):
        """
        Returns list of blog posts.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        posts_query = Post.query
        posts_page = posts_query.paginate(page, per_page, error_out=False)

        return posts_page

    @api.expect(blog_post)
    def post(self):
        """
        Creates a new blog post.
        """
        create_blog_post(request.json)
        return None, 201


@ns.route('/archive/<year>/')
@ns.route('/archive/<year>/<month>/')
@ns.route('/archive/<year>/<month>/<day>/')
class PostsArchiveCollection(Resource):

    @api.expect(pagination_arguments, validate=True)
    def get(self, year, month=None, day=None):
        """
        Returns list of blog posts from a specified time period.
        """
        args = pagination_arguments.parse_args(request)
        return args
