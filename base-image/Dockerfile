from archlinux:latest

RUN pacman -Syu --noconfirm git ruby2.7 vim gcc make

RUN useradd -ms /bin/bash jekyll

RUN chown -R jekyll:jekyll /usr/lib/ruby/gems

USER jekyll
WORKDIR /home/jekyll

RUN mkdir /home/jekyll/page && mkdir /home/jekyll/.ruby

ENV GEM_HOME=/home/jekyll/.ruby
ENV PATH=${PATH}:/home/jekyll/.ruby/bin

RUN bundle-2.7 config set path /home/jekyll/.ruby/gems

RUN gem-2.7 install jekyll

