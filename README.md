# docker-experiments

## TODO

* named volume, cross container.  
  serve static content some container from nginx container

* make two services communicate but  
  from different docker-compose files  
  (shared network)

* nginx static and dynamic
    serve static files and proxy dynamic backend with only two containers
    - one nginx container and
    - one python (flask) or nodejs (express) container

## Done

* [multi stage build](./multi-stage-build/) (previously builder pattern)
* [logging](./logging) (rsyslog)
* use uWSGI (nginx, flask)
    * [basics](./wsgi-0)
    * [two containers](./wsgi) (tcp socket)
