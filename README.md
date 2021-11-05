# Backend of the 8Agency Test

## Build development server

Run `python -m venv .venv`

Run `.\.venv\Scripts\activate` in Windows or `. .venv/bin/activate` if you are in Linux

Run `pip install -r requirements.txt` to install the exact requirements that were used in development

Create a file called `.env` in the root directory. Place these contents in it:

```
FLASK_APP=run
FLASK_ENV=development
DATABASE_URL=sqlite://
```

Save, and afterwards run `flask run` to start the development server

This will make it listen on port 5000 by default.

### Now, once you have built this development server, and the frontend development server, you can navigate to <http://localhost:4200/> to use the application