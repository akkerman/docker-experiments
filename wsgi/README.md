# WSGI nginx flask

The idea is to put multiple flask application behind nginx using wsgi.
Although using a unix socket is supposed to be faster,
using a tcp-socket seems a more feasable approach using docker.


## References

* http://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html
* http://flask.pocoo.org/docs/dev/deploying/wsgi-standalone/#uwsgi
* https://github.com/webpatch/Docker-Flask-uWSGI-Nginx
* https://gist.github.com/Larivact/1ee3bad0e53b2e2c4e40
* https://stackoverflow.com/questions/18967441/add-a-prefix-to-all-flask-routes/18967744#18967744
