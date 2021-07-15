#!/bin/bash

rm -r _site
JEKYLL_ENV=production bundle-2.7 exec jekyll build
