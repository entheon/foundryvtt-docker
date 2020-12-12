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
MONITOR_DOMAIN=<traefik domain>
MANAGE_DOMAIN=<portainer domain>
PLAY_DOMAIN=<foundry domain>
ADMIN_PASSWORD=<password from step 3 with duplicate $ removed>
FOUNDRY_USERNAME=<foundryvtt.com username>
FOUNDRY_PASSWORD=<foundryvtt.com password>
FOUNDRY_ADMIN_KEY=<foundry admin key>
```

Note: You must wrap the domains with `!

6. Run generate_compose

```
python3 generate_compose --env <path_to_env_file>
```

7. Run it!

```
docker-compose up -d
```

# Optional config
## AWS S3 Support
1. Create an IAM user on AWS S3 and grant it sufficient permissions to the correct bucket
2. Create `s3.json` with :

```
{
    "accessKeyId": <AWS IAM Access ID>,
    "secretAccessKey": <AWS IAM Secret Access Key>,
    "region": <AWS Bucket Region Codename>
}
```

3. Place this file at `~/Foundry/data/Config`

## Native Audio and Video Support
1. Edit `~/Foundry/data/Config/options.json` and change `proxySSL: false` to `proxySSL: true`

## Automatic Backup
Create a crontab job and paste in the following:

```
0 2 * * * tar -cf /home/<user>/foundry/backups`date +\%F`.tar /home/<user>/foundry/data
```
