from app1 import app
from app1.forms import LoginForm,RegistrationForm
from flask import render_template,redirect,flash,url_for
from flask_login import current_user,login_user,logout_user,login_required
from flask import request
from werkzeug.urls import url_parse
from app1.models import User,Post
from app1 import db
from datetime import datetime
from app1.forms import editProfileAbout



@app.before_request
def rec_last_seen():
    if current_user.is_authenticated:
        current_user.last_seen=datetime.utcnow()
        db.session.commit()

@app.route('/edit_profile',methods=['GET','POST'])
@login_required
def edit_profile():
    form=editProfileAbout()
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.about_me=form.about_me.data
        db.session.commit()
        flash('You Changed Your Profile')
        return redirect(url_for('edit_profile'))
    elif request.method=='GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',form=form)





@app.route('/')
@app.route('/index')
@login_required
def hey():
    return render_template('index.html',title='Home',post=Post)

@app.route('/user/<username>')
@login_required
def userprofile(username):
    user=User.query.filter_by(username=username).first_or_404()
    posts=[
    {'author':user,'body':'Test Post #1'},
    {'author':user,'body':'Test Post #2'}
    ]
    return render_template('user.html',user=user,posts=posts)


@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated :
        return redirect(url_for('hey'))
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations youn have succesfully registered")
        return redirect(url_for('login'))
    return render_template('register.html',title='Registration',form=form)


@app.route('/signin',methods=['POST','GET'])
def login():

    if current_user.is_authenticated:
            return redirect(url_for('hey'))

    Form=LoginForm()
    if Form.validate_on_submit():
        user=User.query.filter_by(username=Form.username.data).first()
        if user is None or not user.check_password(Form.password.data):
            flash('Invalid Username')
            return redirect(url_for('login'))
        login_user(user,remember=Form.remember_me.data)
        next_page=request.args.get('next')
        if not next_page or url_parse(next_page).netloc!='':
            next_page=url_for('hey')
        return redirect(next_page)
        return redirect(url_for('hey'))
        flash('Login requested by user {} and remember me given {}'.format(Form.username.data,Form.remember_me.data))
        return redirect(url_for('hey'))
    return render_template('login.html',title='LoginForm',form=Form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('hey'))
