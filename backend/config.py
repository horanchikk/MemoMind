DOCS_ROOT = './backend/docs'
DOCS_TITLE = 'Voluntix API Docs'
DOCS_MODELS = [
    # ('ModelName', 'path/to/model.py')
    ('UserModel', '../models/__init__.py'),
    ('NoteModel', '../models/__init__.py'),
    ('SignUpUser', '../models/__init__.py'),
    ('LogInUser', '../models/__init__.py'),
    ('EditUserProfile', '../models/__init__.py'),
    ('CreateNote', '../models/__init__.py'),
    ('EditNote', '../models/__init__.py'),
]
DOCS_MOUNTS = [
    # ('/path/in/api', 'path/to/mount.py')
    ('user', '../mounts/user.py'),
    ('note', '../mounts/note.py'),
]
DOCS_EXCEPTIONS = [
    # 'path/to/exceptions/file.py'
    '../exceptions.py',
]