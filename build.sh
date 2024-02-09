#!/bin/bash

rm -r _site
JEKYLL_ENV=production bundle exec jekyll build
