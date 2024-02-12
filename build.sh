#!/bin/bash

rm -r _site
  python3 scripts/conv_bibtex_to_yaml.py
JEKYLL_ENV=production bundle exec jekyll build
