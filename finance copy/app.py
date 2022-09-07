import os
import datetime;
import cs50;


from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    # """Show portfolio of stocks"""
    stocks = db.execute(
        "SELECT symbol, number,price,name FROM registry WHERE user_id = ? ORDER BY id ASC;", session["user_id"])

    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = cash[0]['cash']
    totalStocks = 0
    for stock in stocks:
        stock['price'] = lookup(stock['symbol'])['price']
        totalStocks +=  stock['price'] * stock['number']



    return render_template("portfolio.html" , stocks=stocks , totalStocks=totalStocks, cash = cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    # """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)

        if not request.form.get("shares") or float(request.form.get("shares")) <= 0 :
            return apology("must provide shares", 403)

        symbol = request.form.get("symbol")
        shares = float(request.form.get("shares"))

        stock = lookup(symbol)

        if not stock == None:
            cash = db.execute('SELECT cash FROM users where id = ?;' , session["user_id"])
            print(float(cash[0]['cash'] - stock['price'] * shares))
            if  float(cash[0]['cash'] - stock['price'] * shares) < 0:
                return apology("You do not have enough cash available")

            timestamp = datetime.datetime.now()
            cash = cash[0]['cash'] - stock['price'] * shares
            db.execute("UPDATE users SET cash = ?;", cash)
            db.execute("INSERT INTO history (user_id, symbol,name, number , type, price, timestamp, priceAt) VALUES (?,?,?,?,?,?,?,?);",
                       session["user_id"], symbol, stock['name'], shares, "BUY", stock['price'], timestamp , stock['price'])

            owned = db.execute("SELECT number FROM registry WHERE user_id = ? and symbol = ?;", session["user_id"], symbol )


            if owned == []:
                db.execute("INSERT INTO registry (user_id, symbol,name, number , type, price) VALUES (?,?,?,?,?,?);",
                       session["user_id"], symbol, stock['name'], shares, "BUY", stock['price'])
            else:
                # db.execute("INSERT INTO registry (user_id, symbol,name, number , type, price) VALUES (?,?,?,?,?,?);",
                #        session["user_id"], symbol, stock['name'], shares + owned[0]['number'], "BUY", stock['price'])

                db.execute("UPDATE registry SET number = ? , price = ? WHERE user_id = ? AND symbol = ?",shares + owned[0]['number'], stock['price']
                , session["user_id"], symbol)




        else:
            return apology("Stock Symbol entered does not exist")

        flash('Stock bought')

        return redirect("/")

    else:
        return render_template("buyRequest.html")


@app.route("/history")
@login_required
def history():
    # """Show history of transactions"""
    history = db.execute("SELECT * from history WHERE user_id =?", session["user_id"])
    print(history)
    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        flash('You were successfully logged in')
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    flash('You were successfully logged out')

    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        # check if all fields filled in (shorthand method)
        if not request.form.get("symbol"):
            return apology("Missing Symbol", 400)

        # put form inputs into variables
        symbol = request.form.get("symbol")

        response = lookup(symbol)
        response['price'] = usd(response['price'])

        if response == None:
            return apology("Stock Symbol entered does not exist")

        return render_template("quoteResponse.html", response=response)

    else:
        return render_template("quoteRequest.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # check if all fields filled in (shorthand method)
        if not request.form.get("username") or not request.form.get("password") or not request.form.get("confirmation"):
            return apology("Must fill out all fields", 400)

        # put form inputs into variables
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # check if the password was confirmed accurately
        if not password == confirmation:
            return apology("Passwords do not match", 400)

        # check if username is already taken

        takenUsername = db.execute(
            "SELECT username FROM users WHERE username = ?;", username)

        if takenUsername != []:
            return apology("This username has been taken", 403)

        # create hash from password
        hash = generate_password_hash(password)

        # add user to database
        db.execute(
            "INSERT INTO users (username, hash) VALUES (?,?);", username, hash)

        # log the user in and create a session for them
        user = db.execute(
            "SELECT id,username FROM users WHERE username = ?", username)

        session["user_id"] = user[0]['id']

        # after register, redirect
        flash('You were successfully registered and logged in')

        return redirect("/")

    else:
        return render_template("register.html")




@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    # """Sell shares of stock"""
    if request.method == "POST":
        if not request.form.get("stock") or not request.form.get("shares"):
            return apology("Must fill out all fields", 400)

        # put form inputs into variables
        stock = request.form.get("stock")
        shares = request.form.get("shares")


        # check if stock is accutually owned and if the shares number is too much
        stockInfo = db.execute("SELECT number FROM registry where user_id =? AND symbol = ?", session["user_id"], stock)

        if stockInfo ==[]:
            return apology("You do not own this stock", 400)



        if float(shares) > float(stockInfo[0]['number']):
            return apology("Put a valid number of stocks", 400)

        number  = float(stockInfo[0]['number']) - float(shares)
        db.execute("UPDATE registry SET number = ? WHERE symbol = ? AND user_id =?;", number, stock,session["user_id"] )

        checkStock = lookup(stock)
        timestamp = datetime.datetime.now()

        # update history
        db.execute("INSERT INTO history (user_id , symbol, name , number, type , price, timestamp, priceAt) VALUES(?,?,?,?,?,?,?,?);",
        session["user_id"], stock, checkStock['name'] , number, "SELL", checkStock['price'], timestamp , checkStock['price'])

        # add back to cash
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = cash[0]['cash']
        cash = cash + float(shares) * checkStock['price']

        db.execute("UPDATE users SET cash = ? WHERE id =?;", cash, session["user_id"])

        flash('Stock sold')

        return redirect("/")




    else:
        stocks = db.execute("SELECT symbol FROM registry where user_id = ?", session["user_id"] )

        return render_template("sellRequest.html", stocks = stocks)




@app.route("/cash", methods=["GET", "POST"])
@login_required
def cash():
    # add cash
    if request.method == "POST":

        if not request.form.get("cash") :
            return apology("Must fill out all fields", 400)

        # put form inputs into variables
        currentCash = float(request.form.get("cash"))

        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = cash[0]['cash']
        cash = cash + currentCash
        db.execute("UPDATE users SET cash = ? WHERE id =?;", cash, session["user_id"])
        flash('Cash added')

        return redirect("/")

    else:
        return render_template("cash.html")
