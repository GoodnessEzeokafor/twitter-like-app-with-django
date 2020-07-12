### Setting Up A Django Project On Docker

simply click <a href="https://docs.docker.com/compose/django/">here</a> for more reference

### Follow this steps
* Create an empty project directory.
    You can name the directory something easy for you to remember. This directory is the context for your application image. The directory should only contain resources to build that image.
* Create a new file called <b>Dockerfile</b> in your project directory.The Dockerfile defines an application’s image content via one or more build commands that configure that image. Once built, you can run the image in a container. For more information on Dockerfile, see the Docker user guide and the Dockerfile reference.
* Add the following content to the <b>Dockerfile</b>.<br />
    <code>FROM python:3</code><br>
    <code>ENV PYTHONUNBUFFERED 1</code> <br>
    <code> RUN mkdir /code   </code> <br>
    <code> WORKDIR /code </code> <br>
    <code> COPY requirements.txt /code/  </code> <br>
    <code> RUN pip install -r requirements.txt  </code> <br>
    <code>COPY . /code/</code>
    This Dockerfile starts with a Python 3 parent image. The parent image is modified by adding a new code directory. The parent image is further modified by installing the Python requirements defined in the requirements.txt file.
* Save and close the <b>Dockerfile</b>.

* Create a requirements.txt in your project directory.

    This file is used by the RUN<code> pip install -r requirements.txt </code>command in your Dockerfile.
* Add the required software in the file. <br />
    <code>
        Django>=2.0,<3.0
        psycopg2-binary>=2.8
    </code>
