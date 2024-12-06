# Chatbot
- Install the required dependencies.
with pip install -r requirements.py.

- Run with python chatbot.py

Make sure you have different env for backend and chatbot.

- For the chatbot please export with export OPENAI_API_KEY=yourkey


# TrackMyJob - backend

This is the backend API to TrackMyJob web application which allows users to track the status of thier jobs with an intutive web interface. All their data is stored and queried at the backend.
Authentication is required to access thier data.

The backend is a RESTful API made using Flask, flask-restful, sqlalchemy, jwt and Postgres.

Check out the frontend code : [frontend](https://github.com/vineetg3/trackmyjob-frontend)

## Project Status
This project is completed with the planned functionality. Will be developing more with new features.

## Open Endpoints

Open endpoints require no Authentication.

* Login : `POST /api/auth/login`
* Signup : `POST /api/auth/signup`


## Endpoints that require Authentication

Closed endpoints require a valid Token to be included in the header of the
request. A Token can be acquired from the Login view above.

* **Userjobs**
- `GET /api/userjobs` : Gets the list of queried userjobs. Default no query is applied. (Query is sent as json)
- `POST /api/userjob` : Adds a new job for that user
- `GET /api/userjob/<int:pk>` : Gets the specified user job (job card)
- `PUT /api/userjob/<int:pk>` : Updates the specified user job (job card)
- `DELETE /api/userjob/<int:pk>` : Deletes the specified user job (job card)

---

## Installation and Setup

These commands work on linux based systems. Other OS commands would be similar

- Make sure you have installed git.
- create a db in backend folder with `sqlite3 mydb.db`
- Create a virtual environment with venv.
`python3 -m venv backend-env`
- Activate the virtual environment and enter into the folder
- Clone this repository in that folder.
- Install required Python packages.
`pip install -r requirements.txt`

**After installing**
- Initialise the database
`flask db init`
- If the models are changed.The following commands must be executed each time
```
flask db migrate
flask db upgrade
```
**Running the server**

`flask run`

---

Note: Config file has

-Secret key for JWT
-Postgres Database URI



# TrackMyJob - frontend

This web application allows users to track the status of thier jobs with an intutive web interface. All their data is stored and queried at the backend.
TrackMyJob(frontend) is built with React,Bootstrap,JS, and Redux.
A user can use it for thier university applications as well !

Check out the live version : [trackmyjob](https://trackmyjob.herokuapp.com/)

The backend for this project is at the following link: [Click me!](https://github.com/vineetg3/trackmyjob-backend)

## Project Status
This project is completed with the planned functionality. 
Users can do CRUD operations with information they provide such as Job title, company, status of the job(applied, interviews, archived, etc..), date of application, etc. However, users need to sign up and login so that thier information is stored for future use.
Feature requests are welcome!


## Screenshots

![Login Page](/images/loginpage.png)

![Sign Up Page](/images/signUpPage.png)

![Dashboard Page](/images/dashboardpage.png)

## Installation and Setup

Clone down this repository. You will need `node` and `npm` installed globally on your machine.  

Installation:

`npm install`  

To Run Test Suite:  

`npm test`  

To Start Server:

`npm start`  

To Visit App:

`localhost:3000/`  

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

Note : This project uses config.json file for its configuration settings such as Server URL, etc.
While cloning this repository , do not forget to create one and add your local settings.
Currently the file has:
1. SERVER_BASE_URL


