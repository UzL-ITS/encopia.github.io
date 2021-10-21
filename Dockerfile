FROM github-pages-base:latest

RUN mkdir /home/jekyll/dependency_prep

COPY --chown=jekyll:jekyll Gemfile /home/jekyll/dependency_prep
RUN chmod -R 765 /home/jekyll/dependency_prep

RUN cd /home/jekyll/dependency_prep && bundle-2.7 update

WORKDIR /home/jekyll/page
