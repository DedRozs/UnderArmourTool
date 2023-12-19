web: python3 manage.py collectstatic --noinput && gunicorn core.wsgi --log-file=- --config gunicorn-cfg.py 
migrations: python3 manage.py migrate

freeze: sleep 3000