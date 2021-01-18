# Repositorio de proyecto de reforestación

## Actividades del Sprint 0
- [X]  Definición del nombre del equipo
- [X]  Definición de Requerimientos
- [X]  Diseño de Mockups
- [X]  Definición del lenguaje (Python / Django)
- [X]  Levantar página del sitio
- [X]  Elección de la fuente de información
- [X]  Definición de formatos de solicitudes al sistema
- [X]  Modelo de datos de la fuente de información
- [ ]  Por definir (otros)

### Documentos del Sprint 0
* [Link del levantamiento de requerimientos](documentos/Requerimientos.pdf)
* [Link de Modelo de BD para el proyecto](documentos/modelo-bd-arbolado.pdf)
* [Link de diseño de mockups de las UI y sistema](documentos/mock_ups.pdf)
* [Link de Modelo de BD para el proyecto versión 2](documentos/modelo-bd-arbolado-2.pdf)
* [Link de diseño de mockups de las UI y sistema final](documentos/mock_ups_final.pdf)

## Equipo de trabajo
![Brenda](https://github-readme-stats.vercel.app/api?username=marbrehi&theme=buefy&layout=compact)
![Melani](https://github-readme-stats.vercel.app/api?username=Bestobetsa&theme=dracula&layout=compact)
![Adrian](https://github-readme-stats.vercel.app/api?username=AdrianPardo99&theme=vue-dark&layout=compact)
![Kevin](https://github-readme-stats.vercel.app/api?username=Kevin-Garcia-Martinez&theme=prussian&layout=compact)
![Luis](https://github-readme-stats.vercel.app/api?username=LuisEnriqueHdz&theme=solarized-light&layout=compact)
![Samuel](https://github-readme-stats.vercel.app/api?username=SamAlJuMa&theme=gotham&layout=compact)


## Desplegado de aplicación
Para desplegar la aplicación hecha en Django es necesario pensar que se hará uso de Python 3 para trabajar con todo lo previamente establecido, con ello tendremos que tomar en cuenta lo siguiente o seguir los siguientes pasos para desplegar la aplicación:

__Instalación de dependencias y demás__

Primero que otra cosa es necesario preparar el entorno virtual el cual a través de virtualenv o sin el podremos desplegar la aplicación de Django, por un lado, mientras que por el otro es necesario tener instalado el gestor de BD Postgres SQL
### Postgres
Entorno de windows:

Se puede instalar y/o descargar desde [esta página](https://www.postgresql.org/download/)

Entornos basados en Unix

__Debian__

Para el caso de sistemas basados en Debian seguir [esta página](https://www.postgresql.org/download/linux/debian/)

__RedHat__

Para el caso de sistemas basados en RedHat seguir con ejemplo en Fedora 32 [en el siguiente tutorial de instalación](https://comoinstalar.me/como-instalar-postgresql-en-fedora-32/)

### Instalación de dependencias de Django y Python
Finalmente para instalar y adecuar la aplicación para desarrollar, modificar o ejecutar es necesario realizar lo siguiente:
```bash
  # En la carpeta requirements realizar en caso de entorno virtual:
  pip3 install -r local.txt
  # En caso de instalacion directa en sistema Unix
  sudo pip3 install -r local.txt
  # Caso en el que se desea solo instalar en la carpeta del usuario:
  pip3 install -r local.txt --user
```
### En Postgresql
Para terminar la parte de configuración crearemos una BD especifica para trabajar o desplegar nuestra aplicación, por tanto en la consola escribir:
```bash
  # En Windows:
  CREATE DATABASE arboladodb
  CREATE USER <USUARIO>
  \c arboladodb
  ALTER ROLE <USUARIO> WITH PASSWORD '<CONTRASEÑA>';

  # En Unix
  createdb arboladodb
  psql arboladodb
  # Una vez entrando a la shell de Postgres:
  alter role <USUARIO> with password '<CONTRASEÑA>';
```
__Nota importante:__ Es necesario saber que una vez realizando todo esto de Postgres es necesario modificar el archivo _secret.json_ en los apartados _USER_ y _PASSWORD_ para que de este modo se pueda desplegar correctamente la aplicación

### Desplegando la aplicación por primera vez \(Versión 1\)
Para comenzar debemos inicialmente modificar unos archivos de la aplicación:

#### Primer archivo:
El primer file a modificar esta localizado en _/Proyecto_Arbolado/Proyecto_Arbolado/settings/base.py_

En el que modificaremos la línea cuyo contenido es:
```python
  'applications.processors.home_contact'
```
Y la comentaremos
#### Segundo archivo:
El segundo archivo a modificar esta localizado en _/Proyecto_Arbolado/apllications/home/views.py_ en el cual cambiaremos una línea de código:
```python
  # Linea original:
  context["home"] = Home.objects.latest('created')
  # Cambia por:
  context["home"] = 'Hola'
```

## Terminando
Para finalizar esto lo que haremos es:
```bash
  python manage.py makemigrations
  python manage.py migrate
  # En caso de mandar errores evitar el migrate y escribir las siguientes dos lineas
  python manage.py migrate auth
  python manage.py migrate --run-syncdb
```
De modo en que ya tendremos listo casi todo para visualizar la aplicación, después crearemos el superusuario para la aplicación con:
```bash
  python manage.py createsuperuser
  # Solicitara correo y contraseña
```
Finalmente con ello podremos ejecutar nuestra aplicación de Django, en la cual llenaremos los ultimos datos en el panel de _Main Page_ en el cual llenaremos con los datos de:
```bash
  Title_name="Sistema de Administración de Arbolado de la CDMX"
  About_title="Gestión de Arbolado"
  Background_image="<Llenar con la imagen que esta en la carpeta de media del proyecto>"
  Contact_email="saa_management@gob.mx"
  Contact_phone="55 7896 1256"
  Contact_message="Todos los Derechos Reservados"
```
Con esto tendremos que regresar a los dos archivos que modificamos y regresarlos a su estado original, de modo en que ya podemos ejecutar la aplicación con:
```bash
  python manage.py runserver
```
__Nota:__ Es indispensable tener la BD en postgres vacia por lo que si esta trabajando con una versión anterior o algun estilo, podemos hacer lo siguiente para eliminar la base de datos:
```sql
  # Primero detener todo lo que pueda consumir la DB
  # Caso windows o algo parecido
  drop database arboladodb
  # Caso Unix
  dropdb arboladodb
```
Y volver a crear
