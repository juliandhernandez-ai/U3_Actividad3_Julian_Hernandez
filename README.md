# U3_Actividad3_Julian_Hernandez
Crear una base de datos automáticamente con Python, Faker y Git
Este proyecto genera de forma automática una base de datos local en MySQL y la llena con 100,000 registros de prueba usando las herramientas SQLAlchemy y Faker. Es un ejercicio para practicar cómo se unen la programación en Python, el manejo de bases de datos y el control de cambios con Git.

Lo que necesitas antes de empezar
Tener instalado Python 3.10 o más reciente.

MySQL Server funcionando en tu computadora.

Un programa como DBeaver (o cualquier visor de bases de datos) para revisar los resultados.

Git configurado y listo.

Cómo instalar y ponerlo en marcha

1. Descarga el código del proyecto:
git clone <https://github.com/juliandhernandez-ai/U3_Actividad3_Julian_Hernandez.git>
cd <U3_Actividad3_Julian_Hernandez>

2. Crea un entorno virtual:
python -m venv venv

- Para activarlo en Windows:
venv\Scripts\activate

- Para activarlo en Mac o Linux:
source venv/bin/activate

3. Instala las bibliotecas necesarias:
pip install -r requirements.txt


4. Ejecuta el programa:
python main.py