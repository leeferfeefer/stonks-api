### Stonks API

For updating all packages: [look here](https://dougie.io/answers/pip-update-all-packages/#:~:text=You%20can%20now%20use%20the,venv%20using%20pip%20freeze%20%3E%20requirements.)


##Running:
to add to requirements file:    
`pip freeze > requirements.txt`

to install dependencies:    
`pip install -r requirements.txt`

to run: `flask run`

to run available to any machine on network: `flask run -host=0.0.0.0`

##SQLite3 DB
Install sqlite3:    
`brew install sqlite3`

To run the DB:   
`sqlite3 ./stonks.db` 


##Virtual Environments:   
To create venv:    
`python3 -m venv venv`

Source venv before attempting to run   
`. venv/bin/activate`   

`deactivate` will exit the venv   




