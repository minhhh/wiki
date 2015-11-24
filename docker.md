# DOCKER
Docker allows you to package an application with all of its dependencies into a standardized unit for software development.

Docker containers wrap up a piece of software in a complete filesystem that contains everything it needs to run: code, runtime, system tools, system libraries – anything you can install on a server. This guarantees that it will always run the same, regardless of the environment it is running in.

## Images
Docker images are read-only templates from which Docker containers are launched.

### List all images
```
    docker images
```

### Build image from Dockerfile
```
    docker build -t nginx-example .
```

### Remove image
```
    docker rmi busybox
```

### Show history info about a particular images
```
    docker history minhhh/dev
```

### Tag a particular image to a name

```
    docker tag 94535f57d8b2 minhhh/dev:0.1
```

### Saving and loading images to/from tar
```
    # Export the contents of a container's filesystem as a tar archive
    docker export red_panda > latest.tar

    docker import latest.tar

    # Save an image to a tar archive
    docker save busybox > busybox.tar
    docker load --input busybox.tar
```

## Container

### Create and start a container from an image
```
    docker run ubuntu /bin/bash
```

### Start and stop container
```
    docker start 196691c7e0cd
    docker stop 196691c7e0cd
```

## Remove old containers
```
    docker rm 5d4bdae290a4

    # remove all container
    docker rm $(docker ps -a -q)
```

### Running a secondary process in a running container
* [`docker exec`](http://docs.docker.com/engine/reference/commandline/exec/)
```
    docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
```

* To enter running containter
```
    # This will create a new Bash session in the container ubuntu_bash
    docker exec -it ubuntu_bash bash
```

### Commit modified container to image
```
    docker commit 5d4bdae290a4 minhhh/test:0.1
    docker tag 5d4bdae290a4 minhhh/test
```

### Info
* docker ps - show running container
* docker logs - get logs from container
* docker events - gets events from container.
* docker port - shows public facing port of container.
* docker top - shows running processes in container.
* docker stats - shows containers' resource usage statistics.
* docker diff - shows changed files in the container's FS.

### Import export
* docker cp - copies files or folders between a container and the local filesystem..
* docker export - turns container filesystem into tarball archive stream to STDOUT.

## Volumes
```
    docker run -v /home/core/share:/var/www:rw -p 80:80 -d nginx-example
```

## Dockerfile
* How to write good Dockerfile
    * [Best practices for writing Dockerfiles](https://docs.docker.com/engine/articles/dockerfile_best-practices/)
    * [If you run SSHD in your Docker containers, you're doing it wrong!](https://jpetazzo.github.io/2014/06/23/docker-ssh-considered-evil/)

## Inspecting container

* Inspect container
```
    docker inspect fe5f199c07ed

    "Ports": { // this show mapping from container port to host's port
        "27017/tcp": [
            {
                "HostIp": "0.0.0.0",
                "HostPort": "27017"
            }
        ],
        "28017/tcp": [
            {
                "HostIp": "0.0.0.0",
                "HostPort": "28017"
            }
        ]
    },
    "Networks": {
        "bridge": {
            ...
            "Gateway": "172.17.0.1",
            "IPAddress": "172.17.0.3",
            ...
        }
    }
```

## Loggin into container
* detach from docker http://stackoverflow.com/questions/19688314/how-do-you-attach-and-detach-from-dockers-process
```
    Ctrl+p + Ctrl+q
    sudo docker exec -ti [CONTAINER-ID] bash
```

* SSH into your docker
    * https://geraldkaszuba.com/quickly-ssh-into-a-docker-container/

## Misc
* [Forward host port to docker container](http://stackoverflow.com/questions/17770902/forward-host-port-to-docker-container)



# REFERENCES
* [The Tale of a Docker-based Continuous Delivery Pipeline](https://www.youtube.com/watch?v=xNfCEie5_RA)
* [Getting Started with Docker](https://serversforhackers.com/getting-started-with-docker/)
* [Docker Tutorial Series](http://rominirani.com/2015/07/19/docker-tutorial-series/)
* [Docker Tutorial Series](http://blog.flux7.com/blogs/docker/docker-tutorial-series-part-1-an-introduction)
* [The Docker Ecosystem](https://www.digitalocean.com/community/tutorial_series/the-docker-ecosystem)
* [Docker cheat sheet](https://github.com/wsargent/docker-cheat-sheet)
