# First steps

Welcome!


## Initial setup
You're going to write your first lines of Python. But first we need to check everything is right!

If you want to try it directly in your browser: [open the jupyter notebook](/1.first_steps/first_steps_variables.ipynb)

If you want to setup python and this project locally follow these steps.

1. Check you have Python installed:
  - type python in a terminal, it should say something like this:
  ```
  $> python
  Python 3.6.1 (default, Apr  4 2017, 09:40:51)
  [...]
  Type "help", "copyright", "credits" or "license" for more information.
  >>>
  ```
  if not: you need to install python. You will find everything you need on Google :) or you can go to [installation](#installation)

**MAC OS users should use an up to date version of python** (python 3.6 for this guide) since the default system version is the old 2.7 and you should learn python 3

2. (optional) Install some tools which are going to make your life easier:
  - [pip](https://pypi.python.org/pypi/pip) is a package manager. It installs dependencies, librairies, ...
  - [jupyter](http://ipython.org/) is an improved command line interface. You can use it in a browser.
  - [virtualenv](https://virtualenv.pypa.io/en/latest/) is useful if you have different python projects and you want them to have their own dependencies. You should use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) to handle virtualenv creation


3. First program

A easy way to start coding in python is by using a command line interface (CLI). It's what you get when you type "python" or "ipython".
You could write your entire program in the CLI, but you don't want to do this since thiss would be very hard to keep it clean and organized.

Still, it's easy to start with the CLI because you can write code and immediately see what happens.

In this course you won't even need python on your computer since there is a [notebook already available](/1.first_steps/first_steps_variables.ipynb) on GitHub, **go check it first!**

If you want to run this notebook on your own computer:
- [clone this repo](https://help.github.com/articles/cloning-a-repository/)
- (optional) create a python3 virtualenv
- install dependencies `pip install -r requirements.txt`

then run `jupyter notebook` to launch jupyter notebook server, it should open a browser tab in which you could navigate to `1.first_steps -> first_steps_variables.ipynb`


## Installation
<a name="installation"></a>

(if you did not have Python installed)

Go to [python.org](https://www.python.org/downloads/) and choose a version which suits your needs.
There is even a [Beginners Page](https://wiki.python.org/moin/BeginnersGuide/Download) !
