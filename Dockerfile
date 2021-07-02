FROM github-pages-base:latest

RUN mkdir /home/jekyll/dependency_prep
COPY Gemfile /home/jekyll/dependency_prep

RUN cd /home/jekyll/dependency_prep && bundle-2.7 update

WORKDIR /home/jekyll/page
