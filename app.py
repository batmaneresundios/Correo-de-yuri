from flask import Flask
from flask import render_template,request
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='correo_yuri'
mysql.init_app(app)


@app.route('/')
def index():
    sql = "INSERT INTO `trabajador` (`rut`, `nombre_completo`, `sexo`, `cargo`, `direccion`, `fecha_ingreso`, `id_area`, `id_departamento`, `id_usuario`) VALUES ('1934254', 'Alexis Santana Contreras', 'Masculino', 'Jefe', 'Los Maquis 155', '2023-06-01', '2', '2', '2');"
    conn= mysql.connect()
    cursor= conn.cursor() #Donde se almacenan datos
    cursor.execute(sql)
    conn.commit()
    return render_template('empleados/index.html')

@app.route('/create')
def create():
    return render_template('empleados/crear.html')

@app.route('/store', methods=['POST'])
def storage():
    rut=request.form['RUT']
    nombre=request.form['nombre_completo']
    sexo=request.form['sexo']
    cargo=request.form['cargo']
    direccion=request.form['direccion']
    fecha=request.form['fecha_ingreso']    

   
    sql = "INSERT INTO `trabajador` (`rut`, `nombre_completo`, `sexo`, `cargo`, `direccion`, `fecha_ingreso`) VALUES (%s,%s,%s,%s,%s,%s);"
    
    datos = (rut,nombre,sexo,cargo,direccion,fecha)
    conn= mysql.connect()
    cursor= conn.cursor() #Donde se almacenan datos
    cursor.execute(sql,datos)
    conn.commit()
    return render_template('empleados/index.html')



if __name__=='__main__':
    app.run(debug=True)