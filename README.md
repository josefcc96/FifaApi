
<div id="top"></div>

<div align="center">
  <h1 align="center">Fifa Api</h1>
  <p align="center">
    Api desarrollada para consolidar la informaci贸n de todos los equipos que van a ir al pr贸ximo mundial.
    <br />
  </p>
</div>
<br />


## 馃攷 Acerca del proyecto

La FIFA me ha contactado para que le ayudes a consolidar la informaci贸n de todos los equipos que
van a ir al pr贸ximo mundial, as铆 que te dicen que debes crear una API con un CRUD para cada una
de la siguiente informaci贸n:
* Equipo:
  * Nombre del Equipo
  * Imagen de Bandera
  * Escudo del Equipo
* Jugadores del equipo, con los siguientes datos de cada jugador:
  * Foto del jugador
  * Nombre
  * Apellido
  * Fecha de nacimiento
  * Posici贸n en la que juega
  * N煤mero de camiseta
  * 驴Es titular?
* Cuerpo t茅cnico
  * Nombre
  * Apellido
  * Fecha de nacimiento
  * Nacionalidad
  * Rol (t茅cnico | asistente | m茅dico | preparador)

<p align="right">(<a href="#top">back to top</a>)</p>



### Construido con 

La API fue desarrollada con:.

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Swagger](https://swagger.io/)
* [Postgres](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)


<p align="right">(<a href="#top">back to top</a>)</p>

## 馃殌 Primeros Pasos

### Instalaci贸n 馃敡
Para desplegar la API, tenemos dos alternativas:

#### Usando Entorno Virtual

Para este metodo, es necesario tener instalado Python 3.6 o superior, y posteriormente instalar los requerimientos almacenados en el archivo requirements.txt.

* Creacion del entorno virtual:
```
$ python3 -m pip install virtualenv
$ python3 -m virtualenv venv
```
* Activamos el entorno virtual:
   Esto dep茅ndera de la terminal utilizada: 
   * bash
    ```
      $ source venv/bin/activate
    ```
    * powershell
    ```
      $ .\venv\Scripts\activate
    ```
* Instalar requerimientos
  ```
    $ pip install -r requirements.txt
  ```

Como requisito es necesario tener instalado Postgres, ya que es el motor de base de datos que utilizaremos. La configuracion de nuestra base de datos se encuentra en el archivo settings.py.
Por defecto la api intentara conectarse a la base de datos llamada FIFADB con el usuario admin y la contrase帽a admin en el puerto por defecto (5432).

* Inicio de la api:
Una ves instalados los requerimientos en el entorno virtual y configurado nuestra base de datos, podemos iniciar la api con el siguiente comando:
```
$ python manage.py runserver
```


#### Usando Docker compose

Para desplegar la API mediante este metodo, es necesario tener instalado Docker y Docker Compose.

Con el siguiente comando podemos iniciar un grupo de contenedores con una instancia de nuestra base de datos y un servidor web Gunicorn en el cual se encuentra desplegada nuestra API.

```
docker-compose up
```



## 馃捇 Uso

Esta Api cuenta con la documentacion necesaria para cada uno de sus endpoints, la documentacion fue desarrollada en swagger.
Tambien podemos ver la documentacion en formato redoc en el endpoint
:

https:localhost:8000/api/schema/redoc/
<p align="right">(<a href="#top">back to top</a>)</p>



## 馃攽 Licencia

Distributed under the MIT License.

<p align="right">(<a href="#top">back to top</a>)</p>



## 馃摟 Contact

Jose Francisco Campo Campo - [Linkedin](https://www.linkedin.com/in/jose-f-campo-campo/) - jose.francisco.campo.campo@gmail.com 

Project Link: [https://github.com/josefcc96/FifaApi](https://github.com/josefcc96/FifaApi)

<p align="right">(<a href="#top">back to top</a>)</p>



## 馃摎 Librerias Adicionales:


* [Drf spectacular](https://drf-spectacular.readthedocs.io/en/latest/index.html)

<p align="right">(<a href="#top">back to top</a>)</p>
