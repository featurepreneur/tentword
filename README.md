# TentWord
`tentword` is a Sample library that can be used as a module within your Python project.
## Roadmap
- [x] Simple TentWord with Deadlinks count
- [ ] Get all deadlinks
---------------------------

## Quickstart
First, clone the `tentword` Git repository on your local machine and change your working directory to `tentword/`:
```console
$ git clone https://github.com/tactlabs/tentword.git
$ cd tentword
```
Next, compile the `tentword` package:
```console
$ python setup.py sdist bdist_wheel
running sdist
running egg_info
writing tentword.egg-info/PKG-INFO
writing dependency_links to tentword.egg-info/dependency_links.txt
...
```
Then, install the library using `pip` by specifying the path to `.whl` file in `dist/`:
```console
$ pip install dist/tentword-*-py3-none-any.whl
Processing ./dist/tentword-0.0.7.tar.gz
Processing ./dist/tentword-0.0.7-py3-none-any.whl
...

Then, from a Python interpreter:
```python
>>> import tentword as tw
>>> word = tw.get_word()
```

To verify the location and installation of `tentword` package:
```console
$ pip show tentword
Name: tentword
Version: 0.0.5
Summary: TentWord for Python 3.6+
Home-page: https://github.com/tactlabs/tentword.git
Author: Praabindh, Hari Prasad,Divya,Bairavi,Sharon
Author-email: Praabindh, Hari Prasad,Divya,Bairavi,Sharon
...
```