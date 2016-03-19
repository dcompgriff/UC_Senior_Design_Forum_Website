hw3_senior_design_forum
=======================
Initial static page:
http://127.0.0.1:8000/static/index.html

Temporary Admin Credentials:
uname: whoami
ps: whatdoyouwant

##############################################################

##############################################################

# Site Description
This django web app provides the ability to archive senior design projects grouped by departments and year.  Projects can be added using the Add Project button on the main page.  A project consists of a title, poster board image, topic, abstract, group members, advisor, and future work.  This is the current functionality that the web app supports for users.  Administrators for the web app, using the django admin interface, can add departments and years for each department.

# Web Services Used
Amazon s3 - Used for storing the poster board image
Amazon ec2 - hosting the django app itself
Google Cloud SQL - database backend for the web app
