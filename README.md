# Entrega1Tacchetti

Entrega Proyecto Para Curso Python CoderHouse
Alumno: Tacchetti Franco

Entrega1Tacchetti/rentapp :
- Contiene:
    models.py
    forms.py
    views.py

Entrega1Tacchetti/template/rentapp:
- Contient todos los templates necesarios para la visualizacion de:
    Creacion y Visualizacion de objectos en la DB:
        - Tenant
        - Rentable Car
        - Rentable Place

Testing Flow:

- python manage.py runserver
- Dirigirse al localhost especificado
- Clickear en cada uno de los formularios para crear cada uno de los siguiente objectos:
        - Tenant
        - Rentable Car
        - Rentable Place
- Con cada creacion el usuario debe ser redirigido a la detail view de tal objeto en el que se especifica:
    -la fecha de cracion y los datos de tal objeto

- Clickear Home Button para ser redirigido a la vista principal

- Utilizar el buscador en el navbar:
    - Especificar First Name or Last Name or Email para visualizar el Tenant Creado con esos datos (pueden buscar John)
    - Especificar Place Location del Rent Place Creado para visualizar un Rentable Place (pueden buscar Bahía Blanca)
    - Especificar el car model del Rentable Car para visualizar un Rentable Car (pueden buscar Subaru)

- Los resultados deben ser clickleables y redirigir a la Detail View del objeto especificado

- rentapp/tests.py contiene cuatro casos de testeo. Para ejecutarlos ir a root del proyecto y en cmd correr "python.py manage.py test rentapp"

- Problema con signals.py no pude hacer que funcione el singaling para que se cree un profile para un usuario cuando este ultimo es creado

Video: https://drive.google.com/drive/folders/1y3SHPBxOiFMBpgme0-yQiZ3wx908eyMU?usp=sharing

