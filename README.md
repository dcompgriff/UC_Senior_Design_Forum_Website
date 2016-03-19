hw3_senior_design_forum
=======================
This django web app provides the ability to archive senior design projects grouped by departments and year.  Projects can be added using the Add Project button on the main page.  A project consists of a title, poster board image, topic, abstract, group members, advisor, and future work.  This is the current functionality that the web app supports for users.  Administrators for the web app, using the django admin interface, can add departments and years for each department.

# Web Services Used
1. Amazon s3 - Used for storing the poster board image
2. Amazon ec2 - hosting the django app itself
3. Google Cloud SQL - database backend for the web app
