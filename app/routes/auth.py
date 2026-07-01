from flask import Blueprint,render_template,request,redirect,url_for,flash,session

auth_bp = Blueprint('auth', __name__)

USER_CREDENTIALS = {
    'username': 'admin',
    'password': 'password'
}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('task.view_tasks'))
        else:
            flash('Invalid credentials', 'error')
            return redirect(url_for('auth.login'))
    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/register')
def register():
    return render_template('register.html')