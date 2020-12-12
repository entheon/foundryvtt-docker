# foundryvtt-docker
Docker version of Foundry VTT

Courtesy of: https://benprice.dev/posts/fvtt-docker-tutorial/

# Setup
1. Clone the repo
2. Make and edit permissions to `acme.json`

```
cd traefik
touch acme.json
chmod 600 acme.json
```

3. Edit `traefik/traefik.yml` with the correct email.

4. Generating hashed password for Traefik: https://medium.com/@techupbusiness/add-basic-authentication-in-docker-compose-files-with-traefik-34c781234970

```
echo $(htpasswd -nbB <USER> "<PASS>") | sed -e s/\\$/\\$\\$/g
```

5. Make and fill in `.env` file with:

```
MONITOR_DOMAIN=`some.domain`
MANAGE_DOMAIN=`some.domain`
PLAY_DOMAIN=`some.domain`
ADMIN_PASSWORD=<password from step 3 with duplicate $ removed>
FOUNDRY_USERNAME=<foundryvtt.com username>
FOUNDRY_PASSWORD=<foundryvtt.com password>
FOUNDRY_ADMIN_KEY=<foundry admin key>
```

Additional Steps:
1. Enable s3 support
2. Enable audio / video support

Both are options under `foundrydata/Config`

For s3 support, add `s3.json` with IAM credentials and configure it in Foundry

For audio / video, edit `foundrydata/Config/options.json` and change `proxySSL: false` to `proxySSL: true`
