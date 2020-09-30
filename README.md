# Sample_Task
Created a simple web application that allows a user to create ad campaigns and display the ad campaigns according to id if campaign is active.

Tools and Techology used:

Python(2.7) Django(1.11.3) DjangoRest Framework(3.6.3) Pycharm(IDE) Sqlite (Embedded database)

Steps to run the project:

Clone/download the project repository from github.

At first check whether Python is installed or not :

Check it by running command : python –version , if it is not installed then download and install Python

Download Pycharm IDE (Professional version)

pip install -r requirements.txt file (Run this command from your terminal/command prompt)

Open project which you downloaded from github in Pycharm or any editor.

Go to campaign_project folder where manage.py file is present from your terminal.

  Run command : python manage.py makemigrations

  Run command : python manage.py migrate

  Run command: python manage.py createsuperuser (creates admin for project)

  Run command : python manage.py runserver

Go to your browser and hit : localhost:8000/users

Description about the rest calls:

  a) url(r'^admin/', include(admin.site.urls))

on browser hit : localhost:8000/admin

This will redirect to django default admin page over which admin operations can be performed.

  b) url(r'^users/', views.UserList.as_view()),

Hit : localhost:8000/users

Provides get and post calls:

Provides list of all campaigns stored.

Example of response from server:

{ "partner_id": "A67", "duration": 19, "ad_content": "string_of_content_to_display_as_ad", "creation_time": "06:25:57.494104" }, { "partner_id": "1", "duration": 677, "ad_content": "soemadvertisement", "creation_time": "06:25:57.494104" },

Provides a form to post/add campaigns in JSON structure :

{ "partner_id": "5rHgv", "duration": 677, "ad_content": "sample ad"

}

c) url(r'^index/(?P<partner_id>.*)/$', views.UserDetail.as_view())

Hit : localhost:8000/index/A67

Example for response : { "partner_id": "A67", "duration": 19, "ad_content": "string_of_content_to_display_as_ad", "creation_time": "06:25:57.494104" }

Note : In place of A67 provide any partner id

Response ad campaign for particular partner id if campaign is active
