# foundryvtt-docker
Docker version of Foundry VTT

Courtesy of: https://benprice.dev/posts/fvtt-docker-tutorial/

Generating hashed password for Traefik: https://medium.com/@techupbusiness/add-basic-authentication-in-docker-compose-files-with-traefik-34c781234970

```
echo $(htpasswd -nbB <USER> "<PASS>") | sed -e s/\\$/\\$\\$/g
```

Additional Steps:
1. Enable s3 support
2. Enable audio / video support

Both are options under `foundrydata/Config`

For s3 support, add `s3.json` with IAM credentials and configure it in Foundry

For audio / video, edit `foundrydata/Config/options.json` and change `proxySSL: false` to `proxySSL: true`
