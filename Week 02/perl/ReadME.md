# Perl 

## :round_pushpin: Install Docker in Mac
Follow this detailed post to download and install Docker Desktop on your system - :point_right: https://hub.docker.com/editions/community/docker-ce-desktop-mac/

## :round_pushpin: Build a Docker Image 

```
docker build -t perlapp .
```

```
-t - tag name
perlapp - name of image
. - Built an image from same folder.
```

## :round_pushpin: Run the Docker Container

```
docker run -it perlapp
```

By following above steps it will generate the HTML content in the bash only. You have to type the following command to redirect its output to a ```index.html``` file.:

```
perl main.py > index.html
```

Generated HTML content will be copied to ```index.html``` file. Then paste this ```index.html``` file in browser to see the web page.

## :round_pushpin: Output

HTML Output:

<img src="https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week2/perl/perl_html.png">


