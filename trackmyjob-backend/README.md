# TrackMyJob - backend

This is the backend API to TrackMyJob web application which allows users to track the status of thier jobs with an intutive web interface. All their data is stored and queried at the backend.
Authentication is required to access thier data.

The backend is a RESTful API made using Flask, flask-restful, sqlalchemy, jwt and Postgres.

Check out the live version : [trackmyjob](https://trackmyjob.herokuapp.com/)

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
- Create a virtual environment with venv.
`python3 -m venv backend-env`
- Create a db in backend folder with `sqlite3 mydb.db`
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


