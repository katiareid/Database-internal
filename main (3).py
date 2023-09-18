from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "music_mental.db"

def create_connection(db_file):
  try:
    connection = sqlite3.connect(db_file)
    return connection
  except Error as e:
    print(e)
  return None

@app.route('/')
def render_base():
    return render_template('home.html')

@app.route('/about')
def render_about():
    sort = request.args.get('sort', 'ID')
    order = request.args.get('order', 'asc') 
    if order == 'asc':
        new_order = 'desc'
    else:
        new_order = 'asc'
    query = "SELECT ID, Age, Primary_streaming_service, Hours_per_day, While_working, Instrumentalist, Fav_genre, Anxiety, Depression, Insomnia FROM music ORDER BY " + sort +  " " + order 
    con = create_connection(DATABASE)
    cur = con.cursor()
    
    # Query the DATABASE
    cur.execute(query)
    tag_list = cur.fetchall()
    con.close()

    return render_template('about.html', tags=tag_list, order=new_order)

@app.route('/categories1')
def render_ageservicehours():
    sort = request.args.get('sort', 'ID')
    order = request.args.get('order', 'asc') 
    if order == 'asc':
        new_order = 'desc'
    else:
        new_order = 'asc'
    query = "SELECT ID, Age, Primary_streaming_service, Hours_per_day FROM music ORDER BY " + sort +  " " + order 
    con = create_connection(DATABASE)
    cur = con.cursor()
    # Query the DATABASE
    cur.execute(query)
    tag_list = cur.fetchall()
    con.close()

    return render_template('categories1.html', tags=tag_list, order=new_order)
   
@app.route('/categories2')
def render_workinstrumentgenre():
    sort = request.args.get('sort', 'ID')
    order = request.args.get('order', 'asc') 
    if order == 'asc':
        new_order = 'desc'
    else:
        new_order = 'asc'
    query = "SELECT ID, While_working, Instrumentalist, Fav_genre FROM music ORDER BY " + sort +  " " + order 
    con = create_connection(DATABASE)
    cur = con.cursor()

    cur.execute(query)
    tag_list = cur.fetchall()
    con.close()
    print(tag_list)
    return render_template('categories2.html', tags=tag_list, order=new_order)

@app.route('/categories3')
def render_anxietydepressioninsomnia():
    sort = request.args.get('sort', 'ID')
    order = request.args.get('order', 'asc') 
    if order == 'asc':
        new_order = 'desc'
    else:
      new_order = 'asc'
    query = "SELECT ID, Age, Anxiety, Depression, Insomnia FROM music ORDER BY " + sort + " " + order
    con = create_connection(DATABASE)
    cur = con.cursor()

    cur.execute(query)
    tag_list = cur.fetchall()
    con.close()
    print(tag_list)
    return render_template('categories3.html', tags=tag_list, order=new_order)
  
@app.route('/search', methods=['GET', 'POST'])
def render_search():
    search = request.form['search']
    query = "SELECT ID, Age, Primary_streaming_service, Hours_per_day, While_working, Instrumentalist, Fav_genre, Anxiety, Depression, Insomnia FROM music ORDER BY WHERE tag LIKE ? OR description LIKE ?"
    search = "%" + search + "%"
    con = create_connection(DATABASE)
    cur = con.cursor()
    cur.execute(query, (search))
    tag_list = cur.fetchall()
    con.close()
    return render_template("about.html", "categories1.html", "categories2.html", "categories3.html", tags=tag_list, order=new_order())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
  