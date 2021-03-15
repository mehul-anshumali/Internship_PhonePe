FROM perl:latest

RUN cpanm List::MoreUtils

COPY . /perlapp

WORKDIR /perlapp

CMD ["perl","main.pl"," > index.html"]