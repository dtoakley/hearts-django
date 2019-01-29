
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


Build Hearts Django App

```
$ ./build-local-hearts.sh
```

Build Hearts Node Client
```
$ ./build-local-hearts-client.sh
```

Run Hearts app and services together..
```
$ docker-compose up
```

Or run Hearts app and client in separate terminal windows..
```
$ docker-compose up web
# open new terminal window
$ docker-compose up node

```

Check Hearts app logs with...
```
$ docker logs --follow web
```

Check Hearts node client logs with...
```
$ docker logs --follow node
```


