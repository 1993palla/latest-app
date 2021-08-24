import re
from flask import Blueprint,render_template,request, flash
auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html', boolean=True)


@auth.route("/logout")
def logout():
     return render_template('login.html', boolean=True)


@auth.route("/sign-up", methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        phoneNumber = request.form.get('txtEmpPhone')
        dob = request.form.get('dob')
        password = request.form.get('password')
        gender = request.form.get('gender')
        confirm_password = request.form.get('confirmPassword')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First Name must be greater than 1 characters.', category='error')
        elif len(lastName) < 2:
            flash('Last Name must be greater than 1 characters.', category='error')
        elif len(phoneNumber) < 13:
                        flash('Mobile Number must be greater than 1 characters.', category='error')

        elif password !=confirm_password:
                        flash('Passwords don\'t match.', category='error')

        elif len(password)< 7:
            flash('Passwords must be at least 7 characters.', category='error')
        else:
            #add User to database
            flash('Account Created!.', category='success')
    return render_template('sign_up.html')