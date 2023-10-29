# Camunda Viewer

This tool is used for viewing Camunda tasks in a PostgreSQL database.

Note that I have only tested this tool in Camunda 7.15 where it is using a PostgreSQL database.

I hope that you find this tool useful, however, use at your own risk.

## Background

This project was originally intended as a study project while I was learning how to code in python and to get a better understanding of PostgreSQL, but it turned out to be a useful side project.

At work we are using Camunda BPMN for creating custom workflows. Now when one of these workflows breaks, you can use the built-in Camunda UI to attempt to diagnose the issue. More often than not, the issue was because a variable wasn't assigned after a migration or the task was assigned, but the person that it was assigned to didn't action the task. I found that in the native Camunda UI, you need to do a lot of drilling into the data to actually find the issues. 

After looking at the database structure in Camunda, I found that I could piece together the tables that held all the data that I wanted to see. So I created a python application to run the queries on the database. Combined with an Angular frontend, I can now find all the outstanding tasks and what variables are assigned to the task. I also found that I can quite easily return full history of a task which is not available in the Camunda UI at all.  

## Requirements

* Camunda 7.15 or greater (Camunda 8 is not supported)
* Python 3

## Building

* Python 3.10 or greater
* pipenv (python virtual environment tool)

Run build.sh or build.bat to build the application



