# foundryvtt-docker
Docker version of Foundry VTT

Courtesy of: https://benprice.dev/posts/fvtt-docker-tutorial/

Generating hashed password for Traefik: https://medium.com/@techupbusiness/add-basic-authentication-in-docker-compose-files-with-traefik-34c781234970

```
echo $(htpasswd -nbB <USER> "<PASS>") | sed -e s/\\$/\\$\\$/g
```
