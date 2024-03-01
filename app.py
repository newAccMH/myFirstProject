from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

list_of_items = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item = request.form['item']
        list_of_items.append(item)
        return render_template('index.html', items=list_of_items)
    return render_template('index.html', items=list_of_items)


@app.route('/delete/<item>', methods=['POST'])
def delete_item(item):
    if item in list_of_items:
        list_of_items.remove(item)
    return redirect(url_for('index'))


@app.route('/update/<item>', methods=['POST'])
def update_item(item):
    if request.method == 'POST':
        new_item = request.form['new_item']
        if item in list_of_items:
            item_index = list_of_items.index(item)
            list_of_items[item_index] = new_item
        return redirect(url_for('index'))