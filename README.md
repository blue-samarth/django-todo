The first thing I did was to create a new Django project. I did this by running the following command in my terminal:

```bash
django-admin startproject django_pro
cd django_pro
python3 manage.py startapp todo
```

This created a new Django project called `django_pro` and a new app called `todo`. I then added the `todo` app to the `INSTALLED_APPS` list in the `todo/settings.py` file.

Next, I created a new model in the `todo/models.py` file to represent a todo item. The model has a `title` field to store the title of the todo item and a `completed` field to store whether the todo item has been completed or not.

I then ran the following commands to create and apply the migrations for the new model:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

run server
```bash
python3 manage.py runserver
```

checked the server is running by visiting 

Now that the model is set up, I created a new view in the `todo/views.py` file to display a list of all todo items. I used a generic `ListView` from Django's class-based views to do this.

after adding veiws we need to add urls to the project
created a new file called `urls.py` in the `todo` app directory and added the following code to it:
using command
```bash
touch todo/urls.py
```

After adding the urls, I added the `todo` app's urls to the project's main `urls.py` file by including the `todo` app's urls in the `urlpatterns` list.
so we need to add some code to the `django_pro/urls.py` file to include the `todo` app's urls.



