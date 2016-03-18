#Use base python 2.7.11 image.
FROM python:2.7.11

#RUN apt-get update && apt-get install -y \ emacs
#Install python dep for project.
#RUN pip install django
#RUN pip install mysql-python

#Expose docker ports.
EXPOSE 8000
EXPOSE 80

#Add env var used by django to select the prod db.
RUN export PROGENV=prod

#Make a dir, and add the git repo to the new dir.
RUN mkdir /home/proj/
ADD ./ /home/proj/
