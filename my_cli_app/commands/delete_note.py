import click
from my_cli_app.modules.notes import note_manager

@click.command()
@click.argument('title')
def delete_note(title):
    note = note_manager.delete_note(title)
    if not note:
        click.echo("No note with that title found.")
        return
    click.echo(f'Note "{title}" deleted successfully.')