# Activación

- Clonar el proyecto:
```bash
git clone https://github.com/adgibertoni/Entrega1-Gibertoni
```

- Crear y activar entorno virtual:
    ### 1. python -m venv venv
    ### 2. .\venv\Scripts\activate

- Instalar el archivo requirements.txt:
```bash
pip install -r requirements.txt
```

- Navegar hacia la carpeta del proyecto nba_blog

- Ejecutar el servidor:
```bash
python manage.py runserver
```

# Funcionalidades

- Herencia de HTML desde el index al resto de las apps.

- En la barra de navegación (superior derecha) se encuentran las diferentes apps (1 por cada models):
    ### 1. Jugadores.
    ### 2. Equipos.
    ### 3. Reportes.

- Cada app tiene el botón "crear/agregar" para poder agregar un registro a través de un formulario.
    ### ·La sección de Reportes utiliza CRUD·

- Desde el home se puede utilizar la búsqueda en BD para los jugadores cargados.

- Se incluye el archivo db.sqlite3 para que ya tenga precargado algunos datos en cada sección/app.
