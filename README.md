# delivery_system
Este proyecto implementa un sistema de información básico para un servicio de mensajería

El presente documento contiene el getting-started de la aplicación de entregas con todo lo necesario para correr el proyecto en su máquina y usar el frujo principal: Creación de una entrega

## **Getting started**

Para empezar a usar el sistema de entregas necesita ejecutar los sigueintes pasos:

- Clonar el proyecto
    

El proyecto se encuentra alojado en [Github.](https://github.com/entropy16/delivery_system)

Para clonar, dirigirse a una carpeta deseada, abrir una terminal y ejecutar:

`git clone hhtps://github.com/entropy16/delivery_system`

- Abrir la carpeta /delivery_system: `cd delivery_system`
    
- Crear entorno virtual: `python -m venv venv`
    
- Ejecutar el entorno virtual: `source venv/bin/activate`
    
- Instalar requisitos del proyecto: `pip install -r requirements.txt`
    
- Abrir la carpeta delivery_system: `cd delivery_system`
    
- Correr y ejecutar migraciones:
    

Para crear las migraciones en caso de que no esen, primero ejecutamos:

`python manage.py makemigration`

Despues, aplicamos los cambios sobre la base de datos (en este caso SQLite):

`python manage.py migrate`

- Crear un superusuario: `python manage.py createsuperuser --username admin --email admin@example.com`
    
- Correr el proyecto: `python manage.py runserver`
    
El resto de la documentación se encuentra en la colección de Postmand del proyecto: [Delivery System API Documentation](https://www.postman.com/gold-meadow-56857/workspace/delivery-system)

Allí encontrarás los pasos para realizar el flujo principal de la plataforma: Crear una entrega
