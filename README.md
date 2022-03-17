# flaskapp

This project demonstrates the following technologies:

  * [Flask](http://flask.pocoo.org/), Python based WEB framework
  * [uWSGI](http://uwsgi-docs.readthedocs.org/), web application deployment solution
  * [nginx](http://nginx.org/), reverse proxy server. Capable of proxying HTTP requests to uWSGI via UNIX-domain sockets
  * [HAProxy](http://www.haproxy.org/), TCP/HTTP load balancer
  * [Docker](https://www.docker.com/), solution for deploying distributed applications in containers
  
  
# Running the containers

Build and run the application in Docker container:

    [sudo] docker-compose build
    [sudo] docker-compose up


# Testing
 After running the Docker container, we can access through IP in whlistIP (if necessary) by [http://localhost:9001](http://localhost:9001) and [http://localhost:9002](http://localhost:9002)
