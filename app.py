from flask import Flask, render_template, request, redirect

app = Flask(__name__)

posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        posts.append({
            'title': request.form['title'],
            'content': request.form['content']
        })
        return redirect('/')
    return render_template('create.html')

@app.route('/edit/<int:i>', methods=['GET', 'POST'])
def edit(i):
    if request.method == 'POST':
        posts[i]['title'] = request.form['title']
        posts[i]['content'] = request.form['content']
        return redirect('/')
    return render_template('edit.html', post=posts[i])

@app.route('/delete/<int:i>')
def delete(i):
    posts.pop(i)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
