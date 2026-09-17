from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
erp = Flask(__name__, template_folder=os.path.join(basedir, 'templates'), static_folder=os.path.join(basedir, 'static'))

# ================= CONFIG =================
erp.secret_key = os.environ.get('SECRET_KEY', 'nepal')

# SQLite database — use /tmp on Vercel (only writable location in serverless)
if os.environ.get('VERCEL'):
    erp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'
else:
    erp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
erp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(erp)

# ================= MODEL =================
class Registration(db.Model):
    emyid = db.Column(db.Integer, primary_key=True)
    empname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    mobile = db.Column(db.String(20))
    designation = db.Column(db.String(100))
    salary = db.Column(db.String(20))

# create table (safe: won't crash the app if DB is unavailable)
with erp.app_context():
    try:
        db.create_all()
    except Exception as e:
        print('DB init warning:', e)

# ================= PUBLIC ROUTES =================
@erp.route('/')
def home():
    return render_template('index.html')

@erp.route('/about')
def about():
    return render_template('about.html')

@erp.route('/contact')
def contact():
    return render_template('contact.html')

@erp.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')

# ================= ADMIN LOGIN =================
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'super')

@erp.route('/admindashboard', methods=['POST', 'GET'])
def admindashboard():
    # GET: show dashboard directly if already logged in
    if request.method == 'GET':
        if admin_required():
            return render_template('admindas.html')
        return redirect(url_for('adminlogin'))

    username = request.form.get('username')
    password = request.form.get('password')

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        session['login'] = True
        session['name'] = 'Ram'
        return render_template('admindas.html')
    else:
        return render_template('adminlogin.html', ms="Invalid username or password")

# ================= AUTH CHECK =================
def admin_required():
    return 'login' in session and session['login']

# ================= ADD EMPLOYEE =================
@erp.route('/addemployee')
def addemployee():
    if not admin_required():
        return redirect(url_for('adminlogin'))
    return render_template('addemploy.html')

# ================= SHOW EMPLOYEES =================
@erp.route('/showemployee')
def showemployee():
    if not admin_required():
        return redirect(url_for('adminlogin'))

    emplist = Registration.query.with_entities(
        Registration.emyid,
        Registration.empname,
        Registration.designation,
        Registration.salary
    ).all()

    return render_template('showemploy.html', recordlist=emplist)

# ================= SAVE EMPLOYEE =================
@erp.route('/save', methods=['POST'])
def save():
    if not admin_required():
        return redirect(url_for('adminlogin'))

    emp = Registration(
        empname=request.form.get('txtName'),
        email=request.form.get('txtEmailID'),
        mobile=request.form.get('txtMobile'),
        designation=request.form.get('txtDesignation'),
        salary=request.form.get('txtSalary')
    )

    db.session.add(emp)
    db.session.commit()

    return render_template('admin_registration_succes.html')

# ================= PROFILE =================
@erp.route('/profile')
def profile():
    if not admin_required():
        return redirect(url_for('adminlogin'))

    emp_id = request.args.get('eid')

    recordlist = Registration.query.filter_by(emyid=emp_id).all()

    return render_template('profile.html', emplist=recordlist)

# ================= UPDATE =================
@erp.route('/update', methods=['POST'])
def update():
    if not admin_required():
        return redirect(url_for('adminlogin'))

    emp = Registration.query.get(request.form.get('txtEmpID'))

    emp.empname = request.form.get('txtName')
    emp.email = request.form.get('txtEmailID')
    emp.mobile = request.form.get('txtMobile')
    emp.designation = request.form.get('txtDesignation')
    emp.salary = request.form.get('txtSalary')

    db.session.commit()

    return render_template('update.html')

# ================= DELETE =================
@erp.route('/delete')
def delete():
    if not admin_required():
        return redirect(url_for('adminlogin'))

    emp = Registration.query.get(request.args.get('id'))

    db.session.delete(emp)
    db.session.commit()

    return render_template('delete.html')

# ================= SEARCH =================
@erp.route('/searchemployee', methods=['POST', 'GET'])
def search():
    if not admin_required():
        return redirect(url_for('adminlogin'))

    name = request.form.get('name')

    # GET (e.g. opened directly in browser): show the search page
    if request.method == 'GET' or not name:
        return render_template('searchemploy.html')

    recordlist = Registration.query.filter(
        Registration.empname.like(name + '%')
    ).with_entities(
        Registration.emyid,
        Registration.empname,
        Registration.designation
    ).all()

    return render_template('search.html', emplist=recordlist)

# ================= LOGOUT =================
@erp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('adminlogin'))

# ================= RUN =================
if __name__ == '__main__':
    erp.run(debug=True)