from flask import Flask, render_template
#from posts import posts

app = Flask(__name__)


posts = [
    {
        'author': 'Eli Swanson',
        'title': 'A better blog, self-built',
        'content': 'Working on it',
        'date_posted': 'Mar 1, 2020'
    },
    {
        'author': 'Eli Swanson',
        'title': 'A better blog, self-built Part 2',
        'content': 'Working on it',
        'date_posted': 'April 1, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title = "About")


#@app.route("/posts")
#def posts():
#    return render_template('posts.html', posts=posts)




if __name__ == '__main__':
    app.run(debug=True)
