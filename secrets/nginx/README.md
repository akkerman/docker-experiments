3 secrets, all files

example with nginx from

https://docs.docker.com/engine/swarm/secrets/#intermediate-example-use-secrets-with-a-nginx-service


    docker swarm init

    docker secret create site.key site.key
    docker secret create site.crt site.crt
    docker secret create site.conf site.conf

    docker service create \
     --name nginx \
     --secret site.key \
     --secret site.crt \
     --secret source=site.conf,target=/etc/nginx/conf.d/site.conf \
     --publish published=3000,target=443 \
     nginx:latest \
     sh -c "exec nginx -g 'daemon off;'"

    curl --cacert root-ca.crt https://localhost:3000

    openssl s_client -connect localhost:3000 -CAfile root-ca.crt

    docker service rm nginx
    docker secret rm site.crt site.key site.conf
