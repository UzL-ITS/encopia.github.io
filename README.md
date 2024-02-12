# Encopia github.io page

## Contributing

First, please read the tutorials:

https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll

There are docker images to work with and test the page locally.

```
# First build both docker images:

# Make sure latest is really latest :)
host~$ docker pull archlinux:latest
# Build the base image, hopefully this is not necessary every time
host~$ cd base-image
host~$ docker build -t github-pages-base .
# Build the 'end-user' image
host~$ cd ..
host~$ docker build -t encopia-page .

# Finally, start the image, install all dependencies and run the webserver

host~$ docker run --net=host -it -v ~/path/to/encopia.github.io:/home/jekyll/page encopia-page

docker~$ ./install.sh
docker~$ ./serve.sh 

# Connect to the webserver on http://127.0.0.1:4000
```
In order to build the page locally, please use the following instructions:

```
# After having merged the changes into master, keep going on gh-pages-local and get the changes

host~$ git merge -X theirs master

# Then, start the docker again and do

docker~$ ./install.sh
docker~$ ./build.sh

# After successful build, push the changes to gh-pages-local and then do

host~$ git subtree push --prefix _site origin gh-pages
```
