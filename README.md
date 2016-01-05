# hello-flask
Sample app to test out Jenkins

## Simple CLI stuff

* `pep8 app.py` : run pep8 against .py
* `py.test --cov` : run pytest including coverage
* `py.test --junitxml=output.xml` : run pytest with XML output
* `pylint app.py` : run pylint against .py 

## Ubuntu 14:04 pvenv bug

There is a bug in the 14:04 venv install. To use python3 virtualenvironment

```
sudo apt-get install python-virtualenv
virtualenv -p python3 myvenv
```
or 

```
sudo apt-get install python3-pip
sudo pip3 install virtualenv
virtualenv myvenv
```