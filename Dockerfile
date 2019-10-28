FROM library/archlinux
MAINTAINER Sebastian Łach <root@slach.eu>

# upgrade os
RUN pacman -Syy --noconfirm archlinux-keyring 
RUN pacman -Sqyyu --noconfirm && pacman-db-upgrade

# install dependencies
RUN pacman -S --noconfirm python2 python2-setuptools python2-pip

# copy application
WORKDIR /app
COPY . . 

# install application
RUN python2 setup.py install
RUN python2 setup.py test

# expose ports
EXPOSE 80

# default command
CMD python2 dockerboard/manage.py runserver 0.0.0.0:80

