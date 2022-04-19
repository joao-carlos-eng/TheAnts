import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Get a database reference to our blog.
ref = db.reference('server/saving-data/fireblog')