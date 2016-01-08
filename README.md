# hello-flask
Sample app to test out Jenkins

## Simple CLI stuff

* `pep8 app.py` : run pep8 against .py
* `py.test --cov` : run pytest including coverage
* `py.test --junitxml=output.xml` : run pytest with XML output
* `pylint app.py` : run pylint against .py 

## Ubuntu 14:04 install

14:04 venv install. To use python3 virtualenvironment

```
sudo apt-get install python3.4-venv
python3 -m venv myvenv
```
or 

```
sudo apt-get install python3-pip
sudo pip3 install virtualenv
virtualenv myvenv
```

update: `virtualenv -p python3 myvenv` also failing, falling back to 2.7 `virtualenv myvenv`