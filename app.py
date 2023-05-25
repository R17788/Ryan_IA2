import sqlite3
import json
import requests
from flask import Flask, render_template, request, url_for, flash, redirect, abort, session
from forms import LoginInformation, DJSearch, ArtistSearch

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'  # the secret key should be a long random string for safety
methods = ['GET', 'POST']
apikey = "523532"


def strip(string):
    string = str(string)
    string = string.replace('(', "").replace(')', '').replace(',', '').replace("'", "").replace('"', "")
    return string


def get_db_connection():
    connection = sqlite3.connect('database/IA2_Database.db', check_same_thread=False)
    # connection.row_factory = sqlite3.Row
    return connection


def get_from_db(sql):
    conn = get_db_connection()
    value = conn.execute(sql).fetchone()
    conn.close()
    value = strip(value)
    return value


def get_row_from_db(sql):
    conn = get_db_connection()
    value = conn.execute(sql).fetchall()
    conn.close()
    return value


def get_from_db_all(sql):
    cursor = get_db_connection().cursor()
    cursor.execute(sql)
    get_db_connection().close()
    value = cursor.fetchall()

    dictionary = {}

    for i, row in enumerate(value):
        username = row[0]
        dictionary[f"user_{i + 1}"] = username

    return dictionary


# req = requests.get(url) #gets the data from the source
# source = req.text # converts the data into a string format
# data = json.loads(source) #turns the source data into a json file, turning it into a dictionary
#
# print(data.keys()) #gets the keys of the dictionary -
# print(type(data['track'])) #tells the type of the key
# print(data['track']) #<- a list of the data ie: 'for item in list'
# mydata = data['track'] <- defines the data
# return_rendertemplate(data=mydata)
# IN HTML SITE:
# {{ for item in data }}
# {{ item['strArtist'] }}
# {{ item['strAlbum'] }}
# <img src="{{ item['strTrackThumb'] }}">


# create a search function, and append the user's search to the end of the url


@app.route('/', methods=methods)
def login():
    error = None
    form = LoginInformation()
    session['login'] = False
    print(session['login'])

    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')

        # verifying that what the user inputs is an integer
        if username.isnumeric():
            print("is int")
            usernameDB = get_from_db(f"SELECT username FROM users WHERE username = {username};")
            passwordDB = get_from_db(f"SELECT password FROM users WHERE username = {username};")

            # getID = f'SELECT username FROM users WHERE username = {username};'
            # getPassword = f'SELECT password FROM users WHERE username = {username};'
            #
            # conn = get_db_connection()
            # getID = conn.execute(getID).fetchone()
            # getPassword = conn.execute(getPassword).fetchone()
            # conn.close()
            # usernameDB = strip(getID)
            # passwordDB = strip(getPassword)
            #
            # print(getPassword)
            # print(f"username DB: {usernameDB}")
            # print(f"password DB: {passwordDB}")
            #
            # print(f"username: {username}")
            # print(f"password: {password}")
            # print("hello")

            if username == usernameDB and password == passwordDB:
                name = get_from_db(f"SELECT first_name || ' ' || last_name FROM users WHERE username = {username};")
                # getName = f"SELECT first_name || ' ' || last_name FROM users WHERE username = {username};"
                # conn = get_db_connection()
                # getName = conn.execute(getName).fetchone()
                # name = strip(getName)
                # conn.close()
                session['name'] = name
                session['login'] = True
                session['username'] = username

                level = get_from_db(f"SELECT user_type FROM users WHERE username = {username};")
                print(level)
                session['level'] = level
                print(session['level'])
                print(session['login'])
                error = None
                print('yes')
                flash("You were successfully logged in")

                return redirect('index')

            else:
                flash("Invalid username or password")
                error = "Invalid username or password"
                return redirect('/')

        else:
            redirect('/')

    return render_template('login.html', form=form, error=error)


@app.route('/index', methods=methods)
def index():
    if session['login']:
        session['current_page'] = 'home'
        url_album = f"https://www.theaudiodb.com/api/v1/json/{apikey}/searchalbum.php?s=taylor_swift"
        url_top10alltime = f"https://theaudiodb.com/api/v1/json/{apikey}/mostloved.php?format=album"
        url_charts = f"https://theaudiodb.com/api/v1/json/{apikey}/trending.php?country=us&type=itunes&format=singles"
        req = (requests.get(url_charts)).text
        name = session['name']
        mydata = json.loads(req)
        mydata = mydata['trending']
        print(mydata)

        return render_template('index.html', title='Home', data=mydata)
    else:
        return redirect('/')
    return render_template('layout.html')


@app.route('/search', methods=methods)
def search():
    if session['login']:
        session['current_page'] = 'search'
    else:
        return redirect('/')
    return render_template('search.html', title="Search")


@app.route('/venues', methods=methods)
def venues():
    if session['login']:
        print("hi")
    else:
        return redirect('/')
    return render_template('search/venues.html', title="Venues")


@app.route('/dj', methods=methods)
def dj():
    form = DJSearch()
    if session['login']:
        sql = "SELECT * FROM users WHERE user_type = 2"
        djs = get_row_from_db(sql)
        print(djs)

        if form.validate_on_submit():
            search = request.form.get('search')
            if search == "":
                sql = "SELECT * FROM users WHERE user_type = 2"
                djs = get_row_from_db(sql)
            else:
                if request.form.get('category') == 'first_name':
                    search = search.lower()
                    search = f"{search[0].upper()+search[1:len(search)]}"
                    sql = f"SELECT * FROM users WHERE user_type = 2 AND first_name = '{search}'"
                    djs = get_row_from_db(sql)

                if request.form.get('category') == 'last_name':
                    search = search.lower()
                    search = f"{search[0].upper() + search[1:len(search)]}"
                    sql = f"SELECT * FROM users WHERE user_type = 2 AND last_name = '{search}'"
                    djs = get_row_from_db(sql)

                if request.form.get('category') == 'email':
                    sql = f"SELECT * FROM users WHERE user_type = 2 AND email_address = '{search}'"
                    djs = get_row_from_db(sql)

    else:
        return redirect('/')
    return render_template('search/dj.html', title="Venues", data=djs, form=form)


@app.route('/artist', methods=methods)
def artist():
    form = ArtistSearch()
    if session['login']:
        print("hi")
    else:
        return redirect('/')
    return render_template('search/artist.html', title="Venues", form=form)


@app.route('/album', methods=methods)
def album():
    if session['login']:
        print("hi")
    else:
        return redirect('/')
    return render_template('search/album.html', title="Venues")


@app.route('/songs', methods=methods)
def songs():
    if session['login']:
        print("hi")
    else:
        return redirect('/')
    return render_template('search/songs.html', title="Venues")


@app.route('/friends', methods=methods)
def friends():
    if session['login']:
        session['current_page'] = 'friends'
        # sql = f"""SELECT f.friend_username
        #         FROM friends AS f
        #         INNER JOIN users AS u ON u.username = f.friend_username
        #         WHERE f.username IS NOT NULL AND f.username = {session['username']}; """
        #
        # friend_username = get_from_db_all(sql)
        # print(friend_username)

        # cursor = get_db_connection().cursor()
        #
        # # Execute the SQL query

        # cursor.execute(query)
        #
        # # Fetch the results
        # results = cursor.fetchall()
        #
        # # Extract the usernames into a list
        # usernames = [row[0] for row in results]
        #
        # # Print the usernames
        # print(usernames)
        # for username in usernames:
        #     print(username)
        #
        # # Close the database connection
        # get_db_connection().close()

        query = f"""SELECT friend_username
                         FROM friends
                         WHERE friend_username IS NOT NULL AND username = {session['username']};"""

        usernames = get_from_db_all(query)

        data = {}
        i = 1

        for key, value in usernames.items():
            name = get_from_db(f"SELECT first_name || ' ' || last_name FROM users WHERE username = {value}")
            level = get_from_db(f"SELECT user_type FROM users WHERE username = {value}")
            print(key, ":", value, ":", name)
            info = {value: [name, level]}
            print(info)
            data[f"friend_{i}"] = info
            i += 1

        print(data)
    else:
        return redirect('/')
    return render_template('friends.html', title='Friends', data=data)


@app.route('/events', methods=methods)
def events():
    if session['login']:
        session['current_page'] = 'events'
    else:
        return redirect('/')
    return render_template('events.html', title='Events')


@app.route('/my_profile', methods=methods)
def my_profile():
    if session['login']:
        session['current_page'] = 'my_profile'
    else:
        return redirect('/')
    return render_template('my_profile.html', title='My Profile')


@app.route('/logout', methods=methods)
def logout():
    print("logged out")
    session['name'] = None
    print(session['name'])
    session['level'] = None
    print(session['level'])
    session['login'] = False
    print(session['login'])
    session['current_page'] = None
    print(session['current_page'])
    return redirect(url_for('login'))


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5002)
