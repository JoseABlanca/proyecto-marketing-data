import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

try:
    conexion= mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

    if conexion.is_connected():
        print("Conexion establecida con exito")
        cursor = conexion.cursor()

        cursor.execute("DROP TABLE IF EXISTS campanas_marketing;")

        cursor.execute("""CREATE TABLE campanas_marketing(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nombre_campana VARCHAR(100),
                            presupuesto_gastado DECIMAL(10,2),
                            clics INT,
                            conversiones INT,
                            canal VARCHAR(50)
                       );""")
        sql_insert ="INSERT INTO campanas_marketing (nombre_campana, presupuesto_gastado,clics,conversiones,canal) " \
                    "VALUES(%s,%s,%s,%s,%s)"
        datos = [
            ("Rebajas",500,1200,45,'Facebook'),
            ('Lanzamiento Producto X', 1200.00, 3500, 110, 'Google Ads'),
            ('Retargeting Web', 300.00, 850, 30, 'Instagram'),
            ('Influencer Tech', 800.00, 5000, 200, 'YouTube')
        ]
        cursor.executemany(sql_insert,datos)
        conexion.commit
        print(f'Tabla camapanas_marketing creada con {cursor.rowcount} registros')
except Exception as e:
    print(f'Error al conectar a la base de datos:{e}')

finally:
    if 'conexion' in locals() and conexion and conexion.is_connected():
        cursor.close()
        conexion.close()
        print("Conexion cerrada")


