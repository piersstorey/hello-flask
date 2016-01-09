# hello-flask
Sample app to test out Jenkins

## Simple CLI stuff

* `pep8 app.py` : run pep8 against .py
* `py.test --cov` : run pytest including coverage
* `py.test --junitxml=output.xml` : run pytest with XML output
* `pylint app.py` : run pylint against .py 

## Ubuntu 14:04 venv install

To use python3 virtualenvironment

```
sudo apt-get install python3.4-venv
python3 -m venv myvenv
```

## Deployment

* `sudo apt-get install git`
* `sudo apt-get install python3`
* `sudo apt-get install python3.4-venv`
* `sudo apt-get install supervisor`
* `mkdir /var/www`
* `sudo chown -R www-data:www-data /var/www `
* `sudo chmod 775 /var/www`
* `cd /var/www`
* `git clone git@github.com:piersstorey/hello-flask.git`
* `cd hello-flask`
* `python3 -m venv myvenv`
* `pip install -r requirements.txt`
* `cp /var/www/hello-world/scripts/hello-world-gunicorn /bin/hello-world-gunicorn`
* `sudo chmod u+x /bin/hello-world-gunicorn`
* `cp /var/www/hello-world/scripts/hello-world-gunicorn.conf /etc/supervisord/conf.d/`
* `supervisorctl reread`
* `supervisorctl update`
* `supervisorctl start hello-world-gunicorn`
* `cp /var/www/hello-world/scripts/hello-world/hell-world.conf /etc/nginx/conf.d/`
* `/etc/init.d/nginx reload`



