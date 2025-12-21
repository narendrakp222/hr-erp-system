from flask  import Flask,render_template,request
from flask_mysqldb import MySQL

erp=Flask(__name__)

erp.secret_key='nepal'
erp.config['MYSQL_HOST']='localhost'
erp.config['MYSQL_USER']='root'
erp.config['MYSQL_PASSWORD']=''
erp.config['MYSQL_DB']='hr_erp_db'
mysql=MySQL(erp)


@erp.route('/')
def home():
    return render_template('index.html')

@erp.route('/about')
def about():
    return render_template ('about.html')

@erp.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')
@erp.route('/contact')
def contact():
    return render_template('contact.html')

@erp.route('/admindashboard')
def admindashboard():
    return render_template('admindas.html')

@erp.route('/addemployee')
def addemployee():
    return render_template('addemploy.html')

@erp.route('/showemployee')
def showemployee():
    cur=mysql.connection.cursor()
    cur.execute('select emyid,empname,designation ,salary from registration ')
    emplist=cur.fetchall()
    print(emplist)
    return render_template('showemploy.html',recordlist=emplist)

@erp.route('/searchemployee')
def searchemployee():
    return render_template('/searchemploy.html')

@erp.route('/save',methods=['POST'])
def save():
    i=request.form['txtEmpID']
    n=request.form.get('txtName')
    e=request.form.get('txtEmailID')
    m=request.form.get('txtMobile')
    d=request.form.get('txtDesignation')
    s=request.form.get('txtSalary')

# Database connection open
    cur=mysql.connection.cursor()

# Query Specification
    cur.execute('insert into registration(emyid,empname,email,mobile,designation,salary) values(%s,%s,%s,%s,%s,%s)',(i,n,e,m,d,s))

# Transaction Save/Commit
    mysql.connection.commit()

# Database Connection Close
    cur.close()
    # return 'Success'

    return render_template('admin_registration_succes.html')

erp.run(host='0.0.0.0',debug=True)

