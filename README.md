
# Hearts -- A creative brainstorming app

Hearts is an Avaaz project that makes it simple and easy for teams to share ideas and vote of them! It's a Django 
project with a create-react-app client (hearts-client).

## Requirements

* [Docker Engine](https://store.docker.com/editions/community/docker-ce-desktop-mac) (Tested with docker v17.12.0-ce)
* git - (to check out this project!)

## To build

```bash
$ cd <AVAAZ_HOME>
$ git clone ssh://git@git.avaaz.org:7999/developers/hearts-django.git
$ cd hearts-django
```

Copy `local-dev-config.sh.dist` to `local-dev-config.sh` and edit for your own settings. See local-dev-config.sh.dist for a description of each setting.

Build everything. This takes much longer the first time as the image layers are pulled down:

```bash
$ ./build-all.sh
```

## To run

Start everything:

```bash
$ ./start-all.sh
```

Hearts App is now available at localhost:3000 and you can login with the superuser credentials:
username: admin
password: abcd1234

#Logs 

You can check Hearts app logs with...
```
$ docker logs --follow local-dev-hearts
```

And the check Hearts node client logs with...
```
$ docker logs --follow local-dev-node
```

## To list the running containers

```bash
$ docker container ls
```
