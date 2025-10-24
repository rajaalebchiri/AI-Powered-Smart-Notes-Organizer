import click
import sqlite3
import datetime

class Note:
    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.tags = tags if tags else []
        self.created_at = datetime.datetime.now()
    
    def __repr__(self):
        return f'Note(title={self.title}, tags={self.tags}, created_at={self.created_at})'


class NoteManager:
    def __init__(self, db_path="notes.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()
    
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            tags TEXT,
            created_at TEXT NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()
    
    def add_note(self, title, content, tags=None):
        tags_str = ",".join(tags) if tags else ""
        existTitle = self.conn.execute("SELECT title FROM notes WHERE title = ?", (title,)).fetchone()
        if not existTitle:
            created_at = datetime.datetime.now().strftime("%Y-%m-%d")
            query = "INSERT INTO notes (title, content, tags, created_at) VALUES (?, ?, ?, ?)"
            self.conn.execute(query, (title, content, tags_str, created_at))
            self.conn.commit()
            return {"title": title, "content": content, "tags": tags, "created_at": created_at}
        raise click.ClickException("A note with this title already exists.")
    
    def get_notes(self, tag=None):
        if tag:
            query = "SELECT title, content, tags, created_at FROM notes WHERE tags LIKE ?"
            cursor = self.conn.execute(query, (f"%{tag}%",))
        else:
            query = "SELECT title, content, tags, created_at FROM notes"
            cursor = self.conn.execute(query)
        notes = []
        for row in cursor.fetchall():
            title, content, tags_str, created_at = row
            tags = tags_str.split(",") if tags_str else []
            notes.append({"title": title, "content": content, "tags": tags, "created_at": created_at})
        return notes

    def update_note(self, title, newtitle=None, new_content=None, new_tags=None):
        existNote = self.conn.execute("SELECT title FROM notes WHERE title = ?", (title,)).fetchone()
        if existNote:
            if newtitle:
                self.conn.execute("UPDATE notes SET title = ? WHERE title = ?", (newtitle, title))
            if new_content:
                self.conn.execute("UPDATE notes SET content = ? WHERE title = ?", (new_content, title))
            if new_tags is not None:
                tags_str = ",".join(new_tags)
                self.conn.execute("UPDATE notes SET tags = ? WHERE title = ?", (tags_str, title))
            self.conn.commit()
            return True
        return False
    
    def delete_note(self, title):
        self.conn.execute("DELETE FROM notes WHERE title = ?", (title,))
        self.conn.commit()

    def delete_all_notes(self):
        self.conn.execute("DELETE FROM notes")
        self.conn.commit()

note_manager = NoteManager()
