# docker-experiments

## TODO

* named volume, cross container.  
  serve static content some container from nginx container

* make two services communicate but  
  from different docker-compose files  
  (shared network)

* use uWSGI (nginx, flask)
    * two containers, also serve static via volume

## Done

* [multi stage build](./multi-stage-build/)(previously builder pattern)

* use uWSGI (nginx, flask)
    * [basics](./wsgi-0)
    * [two containers](./wsgi) (tcp socket, context root configurable in nginx)
