# Encopia github.io page

## Contributing

First, please read the tutorials:

https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll

There are docker images, to work with and test the page locally.

```
# First build both docker images:

host~$ cd base-image
host~$ docker build -t github-pages-base .
host~$ cd ..
host~$ docker build -t encopia-page .

# Finally, start the image, install all dependencies and run the webserver

host~$ docker run --net=host -it -v ~/dev/projects/encopia.github.io:/home/jekyll/page encopia-page

docker~$ bundle-2.7 install
docker~$ bundle-2.7 exec jekyll serve 

# Connect to the webserver on http://127.0.0.1:4000
```
