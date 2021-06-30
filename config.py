import os


PGHOST = os.getenv('PGHOST')
PGDATABASE = os.getenv('PGDATABASE')
PGPORT = os.getenv('PGPORT')
PGUSER = os.getenv('PGUSER')
PGPASSWORD = os.getenv('PGPASSWORD')

conn_string = "host=" + PGHOST + " port=" + "5432" + " dbname=" + PGDATABASE + " user=" + PGUSER \
              + " password=" + PGPASSWORD


def app_init(app):
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    return app

