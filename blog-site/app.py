from flask import Flask, render_template
from posts import Posts
import requests
posts = requests.get("https://api.npoint.io/759afb724056c22504b7").json()
# post=[]
# for pt in posts:
#     pt_new=Posts(id=pt["id"], title=pt["title"], subtitle=pt["subtitle"], body=pt["body"], author = pt["author"], date = pt['date'])
#     post.append(pt_new)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts= posts)
# @app.route('/blog/<int:index>')
# def show_post(index):
#     return render_template("post.html", current_post=post[index-1])
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
