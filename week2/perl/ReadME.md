# Perl 

## :pushpin: Install Docker in Mac
Follow this detailed post to download and install Docker Desktop on your system - :point_right: https://hub.docker.com/editions/community/docker-ce-desktop-mac/

## Build a Docker Image 

```
docker build -t perlapp .
```

```
-t - tag name
perlapp - name of image
. - Built an image from same folder.
```

## Run the Docker File

```
docker run -it perlapp
```
