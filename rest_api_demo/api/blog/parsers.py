from flask_restplus import reqparse

pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('page', type=int, required=False, location='values')
pagination_arguments.add_argument('per_page', type=int, required=False, location='values', choices=[10, 20, 30, 40, 50])

parser = reqparse.RequestParser()
parser.add_argument('test', choices=('one', 'two'), location='path')
# pagination_parser.add_argument('id', choices=('one', 'two'), help='Foo param: {error_msg}', location='path')
# pagination_parser.add_argument('foo', choices=('one', 'two'), help='Foo param: {error_msg}')
