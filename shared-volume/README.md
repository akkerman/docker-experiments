# Shared Volume

 Create a nodejs/express application with a static front-end.


    node
     |
     - server.js      <- served with node on :3000, proxy with nginx
     + src
        - index.html  <- shared via volume, served statically with nginx
        - srcipt.js   <- shared via volume, served statically with nginx

        
