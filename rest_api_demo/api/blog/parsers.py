from flask_restplus import reqparse

pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('id', choices=('one', 'two'), help='Foo param: {error_msg}', location='path')
pagination_arguments.add_argument('foo', choices=('one', 'two'), help='Foo param: {error_msg}')
pagination_arguments.add_argument('bar', required=True, location='values')
pagination_arguments.add_argument('bar1', required=True, location='json')

parser = reqparse.RequestParser()
parser.add_argument('test', choices=('one', 'two'), location='path')
