import sqlite3
import json
import requests
from flask import Flask, render_template, request, url_for, flash, redirect, abort, session
from forms import LoginInformation

connection = sqlite3.connect('database/IA2_Database.db', check_same_thread=False)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'  # the secret key should be a long random string for safety
methods = ['GET', 'POST']
apikey = "523532"

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
    form = LoginInformation()
    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')





        usernameDB = 'ryan'
        passwordDB = 'password'





        print(username)
        print(password)
        print("hello")
        if username == usernameDB and password == passwordDB:
            print('yes')
            return redirect('index')
        else:
            return redirect('/')

    return render_template('login.html', form=form)


@app.route('/index', methods=methods)
def index():
    url_album = f"https://www.theaudiodb.com/api/v1/json/{apikey}/searchalbum.php?s=taylor_swift"
    url_top10alltime = f"https://theaudiodb.com/api/v1/json/{apikey}/mostloved.php?format=album"
    url_charts = f"https://theaudiodb.com/api/v1/json/{apikey}/trending.php?country=us&type=itunes&format=singles"
    req = (requests.get(url_charts)).text
    mydata = json.loads(req)
    mydata = mydata['trending']
    print(mydata)
    return render_template('index.html', title='Home', data=mydata)


@app.route('/friends', methods=methods)
def friends():
    return render_template('friends.html', title='Friends')


@app.route('/venues', methods=methods)
def venues():
    return render_template('venues.html', title='Venues')


@app.route('/my_profile', methods=methods)
def my_profile():
    return render_template('my_profile.html', title='My Profile')


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5002)
