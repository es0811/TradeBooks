from flask import Flask,render_template,url_for,request, redirect, flash
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from database import *
from register import *
from reader import *
from book import *
from mybooks import *
from tradebooks import *
from trade import *

login_manager = LoginManager()
app = Flask(__name__)
login_manager.init_app(app)
app.secret_key = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

@login_manager.user_loader
def load_user(email):
    conn=connect()
    reader=Reader.get(conn,email)
    conn.close()
    return reader

@app.route("/",methods=['GET', 'POST'])
@app.route("/login",methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        conn=connect()
        if conn is None:
            print('Not connected to database')
        email=request.form['email']
        reader,msg=Reader.validate_credentials(conn,request.form['email'],request.form['password'])
        if reader==None:
            flash(msg,'danger')
            return redirect(url_for('login'))
        login_user(reader)
        flash('You have sucessfully logged in!','success')
        conn.close()
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route("/register",methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        conn=connect()
        if conn is None:
            print('Not connected to database')
        result,message=input_validation(conn,request.form['email'], request.form['username'])
        if not result:
            flash(message,'danger')
        else:
            reader=Reader(request.form['email'], request.form['username'], request.form['password'],request.form['fname'],request.form['lname'], request.form['add1'], request.form['add2'], request.form['postalcode'],0,0,0,0)
            registration=register_user(conn,reader)
            if registration:
                flash('User registered successfully','success')
                return redirect(url_for('login'))
            else:
                flash('Registration was not successfull','danger')
                return redirect(url_for('register'))
        conn.close()
    return render_template('register.html')


@app.route('/dashboard')
@login_required
def dashboard():
    conn=connect()
    data={'books_listed':len(list_all_books(conn,current_user.email)), 'books_bought':books_bought(conn,current_user.email), 'books_sold':books_sold(conn,current_user.email)}
    conn.close()
    return render_template('dashboard.html',Title='Dashboard',data=data)

@login_required
@app.route('/listbook',methods=['POST','GET'])
def listbook():
    if request.method=='POST':
        conn =connect()
        print(request.form)
        book=Book(request.form['title'],request.form['author'],request.form['genre'],request.form['description'],request.form['pages'],request.form['condition'],request.form['cover'],current_user.email, request.form['cost'])
        book_listed=book.list(conn)
        if not book_listed:
            flash('Could not list the book!','danger')
        else:
            flash('You have successfully listed your book!','success')
        conn.close()
    return render_template('listbook.html',Title='List Your Book')


@app.route('/mybooks')
@login_required
def mybooks():
    conn=connect()
    books=list_all_books(conn,current_user.email)
    conn.close()
    return render_template('mybooks.html',Title='My Books',books=books)


@app.route('/bookdetails/<book_number>',methods=['POST','GET'])
@login_required
def bookdetails(book_number):
    conn=connect()
    book=get_book(conn,book_number)
    reader=Reader.get(conn,book.email)
    if request.method=='POST':
        buy=buy_book(conn,book,current_user.email)
        if buy:
            msg='You have bought the book named '+book.title
            flash(msg,'success')
            return redirect(url_for('dashboard'))
        else:
            flash('There was an error with buying this book','danger')
            return redirect(url_for('bookdetails',book_number=book_number))
    conn.close()
    return render_template('bookdetails.html',Title='Book Details',book=book, reader=reader)


@app.route('/buybook')
@login_required
def buybook():
    conn=connect()
    books=buy_book_list(conn,current_user.email)
    conn.close()
    return render_template('buybook.html',Title='Buy Books',books=books)

@app.route('/search',methods=['POST','GET'])
@login_required
def search():
    conn=connect()
    books=None
    if request.method=='POST':
        if request.form['title']:
            books=buy_book_list_bytitle(conn,current_user.email,request.form['title'])
        elif request.form['genre']:
            books=buy_book_list_bygenre(conn,current_user.email,request.form['genre'])
        else: flash('Please select a suitable serach criteria','danger')
        conn.close()
    return render_template('search.html',Title='Search Books',books=books)


@app.route('/tradehistory')
@login_required
def tradehistory():
    conn=connect()
    trades=get_trade(conn,current_user.email)
    conn.close()
    return render_template('history.html',Title='Trading History',trades=trades)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('login'))
