import click
from my_cli_app.commands.add import add
from my_cli_app.commands.get_notes import get_notes
from my_cli_app.commands.update_note import update_note
from my_cli_app.commands.delete_all import delete_all
from my_cli_app.commands.delete_note import delete_note

@click.group()
def cli():
    """Notes organizer CLI tool."""
    pass


cli.add_command(add)
cli.add_command(get_notes)
cli.add_command(update_note)
cli.add_command(delete_all)
cli.add_command(delete_note)


if __name__ == '__main__':
    cli()