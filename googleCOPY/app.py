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


app = Flask("Traveller")  # naming our application

# Ensure templates are auto-reloaded
# app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///traveller.db")


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


# def login_required(function):  #a function to check if the user is authorized or not
#     def wrapper(*args, **kwargs):
#         if "google_id" not in session:  #authorization required
#             return abort(401)
#         else:
#             return function()
#     print('=======================')
#     print(wrapper)
#     return wrapper


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
    return redirect(
        "/protected_area"
    )  # the final page where the authorized users will end up


@app.route("/logout")  # the logout page and function
def logout():
    session.clear()
    return redirect("/")


@app.route("/traveller")  # the home page where the login button will be located
def home():
    return "Hello World <a href='/login'><button>Login</button></a>"


@app.route("/protected_area")  # the page where only the authorized users can go to
@login_required
def protected_area():
    return f"Hello {session['name']}! <br/> <a href='/logout'><button>Logout</button></a>"  # the logout button
    # return f"Hello {session['name']}! <br/> <a href='/logout'><button>Logout</button></a>"  #the logout button


@app.route("/", methods=["GET", "POST"])
# @login_required
def traveller():
    if request.method == "POST":
        return apology("post travel", 403)

    else:
        destinations = db.execute("SELECT name FROM destinations LIMIT 5;")
       
        # url='https://images.unsplash.com/photo-1662577848352-376ab9fce8c0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80'
        return render_template(
            "index.html", destinations=destinations
        )


@app.route("/favourites", methods=["GET", "POST"])
@login_required
def favourites():
    if request.method == "POST":
        return apology("post favourites", 403)

    else:
        return apology("get favourites")
