
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


