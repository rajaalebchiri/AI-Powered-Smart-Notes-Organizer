import click
from my_cli_app.modules.notes import note_manager


@click.command()
def delete_all():
    note_manager.delete_all_notes()
