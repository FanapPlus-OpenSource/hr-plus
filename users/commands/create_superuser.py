from flask import Blueprint
import click
from datetime import datetime
import pytz
from users.utils.user import CreateSchema
from users.services.user import UserService

bp = Blueprint('students', __name__, cli_group='user')

create_schema = CreateSchema()


@bp.cli.command('create-superuser')
def create():
    user_info = {
        'first_name': click.prompt('Please Your First Name', type=str),
        'last_name': click.prompt('Please Your Last Name', type=str),
        'email': click.prompt('Please Your Email Address', type=str),
        'password': click.prompt('Please Your Password', type=str, hide_input=True, confirmation_prompt=True),
        'is_active': True,
        'is_staff': True,
        'date_joined': datetime.now(pytz.utc).replace(hour=0, minute=0, second=0,
                                                      microsecond=0).astimezone(pytz.utc).isoformat(),
    }

    if errors := create_schema.validate(user_info):
        click.echo(click.style('User Could Not be Created', fg='red'))
        for field in errors:
            for message in errors[field]:
                click.echo(click.style('{}: {}'.format(field, message), fg='red'))
    else:
        user, _ = UserService.create_superuser(user_info)
        if user['status'] is True:
            click.echo(click.style('User Created Successfully!', fg='green'))
        else:
            click.echo(click.style('Something Went Wrong!', fg='red'))
