"""INTENTIONALLY INSECURE legacy endpoints for the Semgrep demo. Local use only."""

import hashlib
import os
import sqlite3

from flask import Blueprint, jsonify, render_template_string, request

legacy = Blueprint("legacy", __name__)

NOTES_DIR = os.path.join(os.path.dirname(__file__), "notes")

_db = sqlite3.connect(":memory:", check_same_thread=False)
_db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, role TEXT)")
_db.executemany(
    "INSERT INTO users (name, role) VALUES (?, ?)",
    [("alice", "admin"), ("bob", "viewer")],
)
_db.commit()


@legacy.get("/api/users")
def find_user():
    name = request.args.get("name", "")
    # INTENTIONALLY INSECURE: SQL built by string formatting (SQL injection).
    query = f"SELECT id, name, role FROM users WHERE name = '{name}'"
    rows = _db.execute(query).fetchall()
    return jsonify([{"id": r[0], "name": r[1], "role": r[2]} for r in rows])


@legacy.get("/api/notes")
def read_note():
    filename = request.args.get("file", "welcome.txt")
    # INTENTIONALLY INSECURE: user input reaches the file path (path traversal).
    with open(os.path.join(NOTES_DIR, filename), encoding="utf-8") as handle:
        return jsonify({"content": handle.read().strip()})


@legacy.get("/api/greet")
def greet():
    name = request.args.get("name", "friend")
    # INTENTIONALLY INSECURE: user input becomes part of the template (XSS/SSTI).
    return render_template_string("<h1>Hello " + name + "</h1>")


@legacy.get("/api/checksum")
def checksum():
    text = request.args.get("text", "")
    # INTENTIONALLY INSECURE: MD5 is a weak hash.
    return jsonify({"checksum": hashlib.md5(text.encode("utf-8")).hexdigest()})