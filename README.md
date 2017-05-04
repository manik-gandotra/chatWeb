# chatWeb 
This is a web app created using **Django** that allows users to chat in real time. The users can register on the site and they can create new chat rooms with names of their choice. Another person can open the same chat room so that they can chat among themselves. At this point the website has not been deployed online. **ngrok** was used to test the site.

## Running locally

To run this app locally, you'll need Python, Postgres, and Redis.(http://postgresapp.com/documentation/)

Then, to run:

- Install requirements: `pip install -r requirements.txt` (you almost certainly want to do this in a virtualenv).
- Migrate: `DATABASE_URL=postgres:///... python manage.py migrate`
- To run locally with `runserver`, set `DATABASE_URL` and `REDIS_URL` in your environ, then run `python manage.py runserver`.
