import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.blog.business import create_user, create_user_type
from rest_api_demo.api.blog.serializers import user_register, user_type, page_of_blog_posts
from rest_api_demo.api.blog.parsers import pagination_arguments
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import User, UserType

log = logging.getLogger(__name__)

ns = api.namespace('user', description='Requests related to users')


@ns.route('/register')
class Register(Resource):
    @api.expect(user_register)
    def post(self):
        """
        Creates a new user.
        """
        create_user(request.json)
        return "User Created Sucessfully", 201

@ns.route('/register/user_type')
class RegisterUserType(Resource):
    @api.expect(user_type)
    def post(self):
        """
        Creates a new user type.
        """
        create_user_type(request.json)
        return None, 201

