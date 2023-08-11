A full-stack web app to learn building flask apps and devops concepts using docker.
```
docker compose up
```

## Commands
Build the image:
```
docker build -t flak-blog .
```

This command runs the container and maps the local port 5000 to the docker port 5000. After running this command you should view the app on your local system at `http://localhost:5000` 
```
docker run -p 5000:5000 -d flask-blog
```

To stop a running container
```
docker stop [CONTAINER]
```

Remove all stopped containers and clean-up unused images
```
docker container prune
```

Remove an image
```
docker rmi [image-ID]
```


## Docker Volumes
First you have to create a shared folder
```
docker volume create shared-tingy
```

List and inspect volumes
```
docker volume ls
docker volume inspect <VOLUME_NAME>
docker volume rm <VOLUME__NAME>
```


Start a container with a volume
```
docker run -d --name flask-blogg --mount source=shared-tingy,target=/secret flask-blog
```
