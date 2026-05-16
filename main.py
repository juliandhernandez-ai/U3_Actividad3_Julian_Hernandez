import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Date, Float, MetaData, Table
from faker import Faker

# 1. CARGA DE CONFIGURACIÓN 🔐
# Cargamos las variables del archivo .env para proteger nuestras credenciales[cite: 41, 42].
load_dotenv()

def obtener_engine():
    """Crea el motor de conexión a la base de datos MySQL."""
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")
    
    # Formato: mysql+pymysql://usuario:password@host:puerto/nombre_bd 
    url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
    return create_engine(url)

# 2. LA FÁBRICA DE DATOS (FAKER) 🏭
def generar_datos_falsos(cantidad=100000):
    """Genera una lista de diccionarios con datos realistas."""
    fake = Faker('es_CO') # Configurado para Colombia
    datos = []
    
    for _ in range(cantidad):
        registro = {
            "nombre": fake.name(),
            "telefono": fake.phone_number(),
            "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=80),
            "ciudad": fake.city(),
            "sexo": fake.passport_gender(),
            "estatura": fake.pyfloat(left_digits=1, right_digits=2, min_value=1.50, max_value=2.00),
            "empleo": fake.job()
        }
        datos.append(registro) # Guardamos en una lista para inserción masiva 
    return datos

# 3. EL PLANO DE LA TABLA (METADATA) 🏗️
def definir_tabla(metadata):
    """Define la estructura de la tabla personas_julian """
    return Table(
        'personas_julian', # Asegúrate de usar el formato personas_julian 
        metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('nombre', String(100)),
        Column('telefono', String(50)),
        Column('fecha_nacimiento', Date),
        Column('ciudad', String(100)),
        Column('sexo', String(10)),
        Column('estatura', Float),
        Column('empleo', String(150))
    )

# 4. FUNCIÓN PRINCIPAL 🤖
def main():
    
    # Inicializamos la conexión y el catálogo de metadatos
    engine = obtener_engine()
    metadata = MetaData() #Funcion de sqlalchemy
    
    # Definimos la tabla y la creamos automáticamente si no existe 
    tabla_personas = definir_tabla(metadata)
    metadata.create_all(engine)
    print(f"✅ Estructura de '{tabla_personas.name}' verificada/creada.")

    # Generamos los 100,000 datos solicitados 
    lista_datos = generar_datos_falsos(100000)

    # Inserción masiva profesional 
    print("Insertando datos en la base de datos...")
    with engine.begin() as conexion:
        conexion.execute(tabla_personas.insert(), lista_datos)
    
    print("✅ ¡Proceso completado con éxito!")

# Bloque de ejecución estándar de Python 
if __name__ == "__main__":
    main()