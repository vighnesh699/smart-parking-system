from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)

# Dummy data for users, managers, and admins (replace with actual database)
users = [{'username': 'user', 'password': 'password'},]
managers = [{'username': 'manager', 'password': 'password'},]
admins = [{'username': 'admin', 'password': 'password'},]

# Dummy data for parking garages (replace with actual API integration)
garages = [
    {'name': 'Garage 1', 'location': 'Location 1', 'availability': True},
    {'name': 'Garage 2', 'location': 'Location 2', 'availability': False},
    {'name': 'Garage 3', 'location': 'Location 3', 'availability': True}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_login', methods=['POST'])
def user_login():
    username = request.form['username']
    password = request.form['password']
    if any(user['username'] == username and user['password'] == password for user in users):
        return redirect(url_for('user_home'))
    else:
        return "Invalid username or password"

@app.route('/manager_login', methods=['POST'])
def manager_login():
    username = request.form['username']
    password = request.form['password']
    if any(manager['username'] == username and manager['password'] == password for manager in managers):
        return redirect(url_for('manager_dashboard'))
    else:
        return "Invalid username or password"

@app.route('/admin_login', methods=['POST'])
def admin_login():
    username = request.form['username']
    password = request.form['password']
    if any(admin['username'] == username and admin['password'] == password for admin in admins):
        return redirect(url_for('admin_dashboard'))
    else:
        return "Invalid username or password"

@app.route('/user_home')
def user_home():
    return render_template('user_home.html', garages=garages)

@app.route('/manager_dashboard')
def manager_dashboard():
    return render_template('manager_dashboard.html', garages=garages)

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html', garages=garages)

if _name_ == '_main_':
    app.run(debug=True)