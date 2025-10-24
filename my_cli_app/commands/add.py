import click
from my_cli_app.modules.notes import note_manager


@click.command()
@click.argument('title')
@click.argument('content')
@click.option('--tags', '-t', multiple=True, help='Tags associated with the note')
def add(title, content, tags):
    note = note_manager.add_note(title, content, tags)
    click.echo(f'Note "{note}" added successfully.')