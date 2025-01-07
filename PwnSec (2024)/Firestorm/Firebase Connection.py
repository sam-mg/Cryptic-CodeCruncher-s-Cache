import pyrebase

config = {
    "apiKey": "AIzaSyAXsK0qsx4RuLSA9C8IPSWd0eQ67HVHuJY",
    "authDomain": "firestorm-9d3db-default-rtdb",
    "databaseURL": "https://firestorm-9d3db-default-rtdb.firebaseio.com/",
    "projectId": "firestorm-9d3db",
    "storageBucket": "firestorm-9d3db.appspot.com",
    "messagingSenderId": "426921051409",
    "appId": "1:426921051409:android:f2b7cc516a47bc7fb2b8b0"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
email = "TK757567@pwnsec.xyz"
password = "C7_dotpsC7t7f_._In_i.IdttpaofoaIIdIdnndIfC"
user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database()
all_data = db.get(user['idToken']).val()
print("Entire Firebase Database content:")
print(all_data)