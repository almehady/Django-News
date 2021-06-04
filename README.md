# Django News
Django News is an open source web application for news agency or anyone wants to start a news website, build on top of Django web framework.

***
## Quick installation
You can setup a virtual environment installing virtualenv and typing the following commands in terminal:

```$ virtualenv <folder_name>```

Then you can activate it:

``` $ source <folder_name>/bin/activate```

(and optionally you can exit from the virtual environment typing: deactivate)

Once made that you can download the project using git or simply downloading it in a zip format and unzip it and go to the main top folder of workshops:

(using git)

$ git clone https://github.com/almehady/Django-News.git
$ cd workshops_project/
(unzipping it)
$ unzip workshops_project-master.zip
$ cd workshops_project-master/
Using pip (inside the virtual environment) install the necessary dependencies with pip from requirements.txt:

``` $ pip install -r requirements.txt```

We will migrate after setting the database (psql or sqlite)

```$ python manage.py migrate ```

We will run the default django's web server typing:

```$ python manage.py runserver```

***
 ### Home screenshot of django news
![home screen](home_screen.png)
