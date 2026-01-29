from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL

erp = Flask(__name__)

# ================= CONFIG =================
erp.secret_key = 'nepal'

erp.config['MYSQL_HOST'] = 'localhost'
erp.config['MYSQL_USER'] = 'root'
erp.config['MYSQL_PASSWORD'] = ''
erp.config['MYSQL_DB'] = 'hr_erp_db'

mysql = MySQL(erp)

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
@erp.route('/admindashboard', methods=['POST'])
def admindashboard():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'admin' and password == 'super':
        session['login'] = True
        session['name'] = 'Ram'
        return render_template('admindas.html')
    else:
        msg = "Invalid username or password"
        return render_template('adminlogin.html', ms=msg)

# ================= PROTECTED ROUTES =================
def admin_required():
    return 'login' in session and session['login']

@erp.route('/addemployee')
def addemployee():
    if not admin_required():
        return redirect(url_for('adminlogin'))
    return render_template('addemploy.html')

@erp.route('/showemployee')
def showemployee():
    if not admin_required():
        return redirect(url_for('adminlogin'))

    cur = mysql.connection.cursor()
    cur.execute('SELECT emyid, empname, designation, salary FROM registration')
    emplist = cur.fetchall()
    cur.close()

    return render_template('showemploy.html', recordlist=emplist)

@erp.route('/searchemployee')
def searchemployee():
    if not admin_required():
        return redirect(url_for('adminlogin'))
    return render_template('searchemploy.html')

# ================= ADD EMPLOYEE =================
@erp.route('/save', methods=['POST'])
def save():
    if not admin_required():
        return redirect(url_for('adminlogin'))

    n = request.form.get('txtName')
    e = request.form.get('txtEmailID')
    m = request.form.get('txtMobile')
    d = request.form.get('txtDesignation')
    s = request.form.get('txtSalary')

    cur = mysql.connection.cursor()
    cur.execute(
        'INSERT INTO registration (empname, email, mobile, designation, salary) VALUES (%s,%s,%s,%s,%s)',
        (n, e, m, d, s)
    )
    mysql.connection.commit()
    cur.close()

    return render_template('admin_registration_succes.html')

<<<<<<< HEAD
# ================= PROFILE =================
@erp.route('/profile')
def profile():
    if not admin_required():
        return redirect(url_for('adminlogin'))
=======
erp.run(host='0.0.0.0',debug=True)
>>>>>>> 394b3bb56de1294e965e5483254d59ab162b094b

    emp_id = request.args.get('eid')

    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT emyid, empname, email, mobile, designation, salary FROM registration WHERE emyid=%s',
        (emp_id,)
    )
    recordlist = cur.fetchall()
    cur.close()

    return render_template('profile.html', emplist=recordlist)

# ================= UPDATE =================
@erp.route('/update', methods=['POST'])
def update():
    if not admin_required():
        return redirect(url_for('adminlogin'))

    i = request.form.get('txtEmpID')
    n = request.form.get('txtName')
    e = request.form.get('txtEmailID')
    m = request.form.get('txtMobile')
    d = request.form.get('txtDesignation')
    s = request.form.get('txtSalary')

    cur = mysql.connection.cursor()
    cur.execute(
        'UPDATE registration SET empname=%s, email=%s, mobile=%s, designation=%s, salary=%s WHERE emyid=%s',
        (n, e, m, d, s, i)
    )
    mysql.connection.commit()
    cur.close()

    return render_template('update.html')

# ================= DELETE =================
@erp.route('/delete')
def delete():
    if not admin_required():
        return redirect(url_for('adminlogin'))

    emp_id = request.args.get('id')

    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM registration WHERE emyid=%s', (emp_id,))
    mysql.connection.commit()
    cur.close()

    return render_template('delete.html')

# ================= SEARCH =================
@erp.route('/search', methods=['POST'])
def search():
    if not admin_required():
        return redirect(url_for('adminlogin'))

    name = request.form.get('name')

    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT emyid, empname, designation FROM registration WHERE empname LIKE %s',
        (name + '%',)
    )
    recordlist = cur.fetchall()
    cur.close()

    return render_template('search.html', emplist=recordlist)

# ================= LOGOUT =================
@erp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('adminlogin'))

# ================= RUN =================
if __name__ == '__main__':
    erp.run(debug=True)
