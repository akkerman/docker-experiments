# docker-experiments

## Done

* [multi stage build](./multi-stage-build/) (previously builder pattern)
* [logging](./logging) (rsyslog)
* use uWSGI (nginx, flask)
    * [basics](./wsgi-0)
    * [two containers](./wsgi) (tcp socket)
* [nginx static and dynamic](./shared-volume)
    serve static files and proxy dynamic backend with only two containers
    - one nginx container and one nodejs (express) container

## TODO

* named volume, cross container.  
  serve static content some container from nginx container

* make two services communicate but  
  from different docker-compose files  
  (shared network)


