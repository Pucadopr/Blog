from app import app, db
from app.models import User, Post, Category, Comment, Profile

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Category': Category, 'Comment': Comment, 'Profile': Profile}
    