import click
from my_cli_app.modules.notes import note_manager


@click.command()
@click.option('--tags', '-t', multiple=True, help='Tags associated with the note')
def get_notes(tags):
    notes = note_manager.get_notes(tags)
    if not notes:
        click.echo("No notes found.")
        return
    for note in notes:
        click.echo(f"{note['title']} (Created at: {note['created_at']})")
        click.echo(f"  {note['content']}\n")
        click.echo(f"  Tags: {', '.join(note['tags'])}\n")