import click
from my_cli_app.modules.notes import note_manager

@click.command()
@click.argument('title')
@click.option('--newtitle', '-nt', help='New title for the note')
@click.option('--content', '-c', help='New content for the note')
@click.option('--tags', '-t', multiple=True, help='New tags for the note')
def update_note(title, newtitle, content, tags):
    note = note_manager.update_note(title, newtitle, content, tags)
    if not note:
        click.echo("No note with that title found.")
        return
    click.echo(f'Note "{title}" updated successfully.')