# Camunda Viewer

This tool is used to view Camunda tasks in a PostgreSQL database.

Note that I have only tested this tool in Camunda 7.15 where it uses a PostgreSQL database.

I hope you find this tool useful, but use it at your own risk.

## Background

This project was originally intended as a study project while I was learning to code in Python and get a better
understanding of PostgreSQL, but it turned out to be a useful side project.

At work, we use Camunda BPMN to create custom workflows. Now, when one of these workflows breaks, you can use the
built-in Camunda UI to try to diagnose the problem. More often than not, the problem was that a variable wasn't assigned
after a migration, or the task was assigned, but the person it was assigned to didn't do the task. I found that in the
native Camunda UI you have to do a lot of drilling into the data to actually find the problems.

After looking at the database structure in Camunda, I found that I could piece together the tables that held all the
data I wanted to see. So I created a Python application to run the queries on the database. Combined with an Angular
frontend, I can now find all the outstanding tasks and what variables are assigned to the task. I also found that I can
easily get the full history of a task, which is not available in the Camunda UI at all.

## Requirements

* Camunda 7.15 or greater (Camunda 8 is not supported)
* Python 3

## Building

* Python 3.10 or greater
* pipenv (python virtual environment tool)
* pyenv (you can skip this one if you edit the version of python needed in the Pipfile)

Run build.sh or build.bat (for Windows) to build the application



