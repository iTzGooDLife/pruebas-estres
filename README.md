# Pruebas-estres

Run debug mode:
	* Usar el entorno virtual
	* `python3 -m flask --app main run --port 5000 --debug`

Build uwsgi with 4 workers:
	* Usar el entorno virtual
	* ir al directorio app
	* `uwsgi --http :5000 --master -p 4 --wsgi-file wsgi.py --callable app`
