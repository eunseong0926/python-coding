# pip install firebase-admin
from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Firebase 초기화
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def index():
    posts_ref = db.collection('posts').stream()
    posts = [doc.to_dict() for doc in posts_ref]
    return render_template('index.html', posts=posts)

@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        db.collection('posts').add({'title': title, 'content': content})
        return redirect('/')
    return render_template('write.html')

if __name__ == '__main__':
    app.run(debug=True)