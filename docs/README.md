# CV Feedback Sharing

only the backend has been developed using django framework , you can try it now locally using any API testing tool such as [Postman](https://www.getpostman.com/)
because it not hosted yet


### Database ERD
![SQL ERD](/erd.png?raw=true)

### Activity diagram
![webiste activity diagram](/activity.png?raw=true)

## Getting Started
These instructions will get you a copy of the REST API running on your local machine for development and testing purposes.

### Installing dependencies
run the following npm command in the project's folder in order to download and install all dependencies
```
git clone https://github.com/hossain-mo/CV-Feedback-Sharing
install python 3.7.x
install django (python -m pip install Django)
```

### Creating a local mySQL database

- download and install [XAMPP](https://www.apachefriends.org/index.html) or any other similar software to start a local mySQL server with InnoDB engine.
- create a new database with any cvfeedbacksharing.
- run the following commands to populate the database:
  - python manage.py makemigrations
  - python manage.py migrate
- open your local server if you use xampp by the following steps
  - start apache 
  - start mysql
  
  

###  Running and testing the REST API

now run the following command to start the API

`
python manage.py runserver
`

the API is now running! you communicate with it using tools like [postman](https://www.getpostman.com/)

if everything is setup properly, all tests should pass without any issues.
## License
MIT, see the LICENSE.md file for details.
 An awesome project.
