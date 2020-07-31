#!/usr/bin/env python3

import os
import sys
import yaml
import argparse
import subprocess


def run(*args, **kwargs):
    print("Command: {}".format(args))

    sys.stdout.flush()
    try:
        return subprocess.run(args, shell=False, check=True, cwd=os.path.join(os.path.dirname(__file__), ".."), encoding='utf-8', **kwargs)
    except subprocess.CalledProcessError as e:
        logging.error('\n'.join([
            "The command exited with an error:",
            "  " + " ".join(args),
            "  " + e.stdout if e.stdout else "",
            "  " + e.stderr if e.stderr else "",
        ]))
        raise

def get_config(files, env=None):
    params = ["docker-compose"]

    if env:
        params.append("--env-file")
        params.append(env)

    for file in files:
        params.append("--file")
        params.append(file)

    params.append("config")

    process = run(*params, capture_output=True)

    return process.stdout

def main():
    parser = argparse.ArgumentParser(
        description="Generate docker-compose.yml for FoundryVTT")
    parser.add_argument(
        "--env", action="store", default=None,
        help="Use env file with docker-compose")
    args = parser.parse_args()

    # Concatenate all three compose files together for ease of use
    root_dir = os.path.dirname(os.path.abspath(__file__))
    files = [
        os.path.join(root_dir, "traefik", "docker-compose.yml"),
        os.path.join(root_dir, "foundryvtt", "docker-compose.yml"),
        os.path.join(root_dir, "portainer", "docker-compose.yml")
    ]

    compose_file_path = os.path.join(root_dir, "docker-compose.yml")
    with open(compose_file_path, "w") as compose_file:
        compose_config = get_config(files=files, env=args.env)
        compose_file.write(compose_config)


if __name__ == "__main__":
    main()
