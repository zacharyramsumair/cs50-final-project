# app.py
import os
import pathlib
import requests
import cs50
import json


from cs50 import SQL
from flask import Flask, session, abort, redirect, request, flash, render_template

from flask_session import Session
from tempfile import mkdtemp
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
from cs50 import SQL
from helpers import apology, login_required
import google.auth.transport.requests
from waitress import serve


app = Flask("Traveller")  # naming our application

# Ensure templates are auto-reloaded
# app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///traveller.db")


# with open("csvjson.json", "r") as f:
#     myJson = json.load(f)


app.secret_key = (
    "GeekyHuman.com"  # it is necessary to set a password when dealing with OAuth 2.0
)
os.environ[
    "OAUTHLIB_INSECURE_TRANSPORT"
] = "1"  # this is to set our environment to https because OAuth 2.0 only supports https environments


GOOGLE_CLIENT_ID = os.environ[
    "client_id"
]  # enter your client id you got from Google console
client_secrets_file = os.path.join(
    pathlib.Path(__file__).parent, "client_secret.json"
)  # set the path to where the .json file you got Google console is

flow = Flow.from_client_secrets_file(  # Flow is OAuth 2.0 a class that stores all the information on how we want to authorize our users
    client_secrets_file=client_secrets_file,
    scopes=[
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/userinfo.email",
        "openid",
    ],  # here we are specifing what do we get after the authorization
    redirect_uri="http://127.0.0.1:5000/callback",  # and the redirect URI is the point where the user will end up after the authorization
)


@app.route("/login")  # the page where the user can login
def login():
    (
        authorization_url,
        state,
    ) = (
        flow.authorization_url()
    )  # asking the flow class for the authorization (login) url
    session["state"] = state
    return redirect(authorization_url)


@app.route(
    "/callback"
)  # this is the page that will handle the callback process meaning process after the authorization
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # state does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token, request=token_request, audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")  # defing the results to show on the page
    session["name"] = id_info.get("name")

    # find any google Ids that match the one that came back from the google account used to log in
    result = db.execute(
        "SELECT google_id  FROM favourites WHERE google_id= ? ;", session["google_id"]
    )
    # (session["google_id"]))

    # if results is blank, then this is a new acccount/visitor to our site, so add it to our favourites table
    if result == []:
        # print('yes')
        # Record doesn't exist
        db.execute("INSERT INTO favourites VALUES (?, ?);", session["google_id"], "")
        print("hell yh added")

    #

    # return redirect("/protected_area")  # the final page where the authorized users will end up
    return redirect("/")


@app.route("/logout")  # the logout page and function
def logout():
    # end the session and redirect back to the home page
    session.clear()
    return redirect("/travellers")


@app.route("/travellers")  # the home page where the login button will be located
def home():
    # return "Hello World <a href='/login'><button>Login</button></a>"
    return render_template("animation.html")


# this route is not really in use, but it came with the sample code of how to login and logout with google auth


@app.route("/protected_area")  # the page where only the authorized users can go to
@login_required
def protected_area():
    return f"Hello {session['name']}! <br/> <a href='/logout'><button>Logout</button></a>"  # the logout button
    # return f"Hello {session['name']}! <br/> <a href='/logout'><button>Logout</button></a>"  #the logout button


@app.route("/", methods=["GET", "POST"])
@login_required
def traveller():
    # get all the info about the destinations to load into the cards
    destinations = db.execute("SELECT * FROM destinations;")

    # if it is a post request, get the ids to send to favourites and the page that we should redirect the user to

    if request.method == "POST":
        postedIDS = request.form.get("id")
        redirectPath = request.form.get("redirect")

        # get all the favourite ids that were entered before

        oldIds = db.execute(
            "SELECT favourites  FROM favourites WHERE google_id= ? ;",
            session["google_id"],
        )

        oldIds = oldIds[0]["favourites"]

        # the result is broken up like /1/3/4/5/6/7, so split by / to get a array with each individual id
        newArray = postedIDS.split("/")
        oldArray = oldIds.split("/")

        # check if the elements in the array are unique and if not make them unique
        newArray = list(dict.fromkeys(newArray))
        oldArray = list(dict.fromkeys(oldArray))

        # remove the first element from the array, since this would be "" after the .split("/")
        newArray.pop(0)
        oldArray.pop(0)

        # add the new ids to the old ids
        for id in range(0, len(newArray)):
            if newArray[id] not in oldArray:
                oldIds += "/" + newArray[id]

        # update the list of favourites for the specific user

        db.execute(
            "UPDATE favourites SET favourites = ? WHERE google_id =?;",
            oldIds,
            session["google_id"],
        )

        # redirect the user to the page based on the input in the form

        if redirectPath == "":
            return redirect("/")
        elif redirectPath == "favourites":
            return redirect("/favourites")
        elif redirectPath == "logout":
            return redirect("/logout")

    # if the method of GET
    return render_template("index.html", destinations=json.dumps(destinations))


@app.route("/favourites", methods=["GET", "POST"])
@login_required
def favourites():
    if request.method == "POST":
        # currently not in use, but here for safety
        return apology("post favourites", 403)

    # if method = GET
    else:
        # get all the favourites for this specific user
        favourites = db.execute(
            "SELECT (favourites) FROM favourites WHERE google_id =?;",
            session["google_id"],
        )

        # prepare string eg. /3/2/4/6 into an array with out the values
        favourites = favourites[0]["favourites"]
        favourites = favourites.split("/")
        favourites.pop(0)

        # array to pass into the template
        array = []

        # add all the info for the cards into the variable array
        for x in range(len(favourites)):
            array.append(
                db.execute(
                    "SELECT id, name , images , description, sights ,map from destinations WHERE id=?;",
                    favourites[x].strip(),
                )
            )

        return render_template("favourites.html", array=array)


# test route to check if the jinja templates were working
@app.route("/template")  # the home page where the login button will be located
def template():
    return render_template("myChild.html")


if __name__ == "__main__":
    serve(app, host="127.0.0.1", port=5000)
