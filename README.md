hw3_senior_design_forum
=======================
This django web app provides the ability to archive senior design projects grouped by departments and year.  Projects can be added using the Add Project button on the main page.  A project consists of a title, poster board image, topic, abstract, group members, advisor, and future work.  This is the current functionality that the web app supports for users.  Administrators for the web app, using the django admin interface, can add departments and years for each department.

# Web Services Used
1. Amazon s3 - Used for storing the poster board image
2. Amazon ec2 - hosting the django app itself
3. Google Cloud SQL - database backend for the web app
4. Django "\<program degree>\<year>" service which returns a list of projects formatted with html and css for a given year and program.
5. Django "\years\" endpoint, which returns the set of all years stored in the database.
6. Django "\addprojectform\" endpoint, returns an html div for inputing new project info.
7. Django "\project\" which takes a set of information about a new project, and stores it in the cloud sql database. 