from archlinux:latest

RUN pacman -Syu --noconfirm git ruby vim gcc make python python-virtualenv python-pip

RUN useradd -ms /bin/bash jekyll

RUN chown -R jekyll:jekyll /usr/lib/ruby/gems

USER jekyll
WORKDIR /home/jekyll

RUN mkdir /home/jekyll/page && mkdir /home/jekyll/.ruby

ENV GEM_HOME=/home/jekyll/.ruby
ENV PATH=${PATH}:/home/jekyll/.ruby/bin:/home/jekyll/.local/share/gem/ruby/3.0.0/bin

RUN bundle config set path /home/jekyll/.ruby/gems

RUN gem install jekyll

RUN python3 -m venv venv && source venv/bin/activate && pip install requests bibtexparser PyYAML
ENV PATH="/home/jekyll/venv/bin:$PATH"
