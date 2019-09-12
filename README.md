#Project RC-car API
The current version of the project uses a RESTful API developed with Python. The framework for this is the Flask package. This API can be hosted in a Docker container on the Raspberry Pi for easy communication with the GPIO pins. On this page is documented how the API can be run locally but also how you can deploy it to a Docker container.

#Endpoints
At this moment the following endpoints can be used. The parameters must be sent in a form with a POST request. Make sure that the key of the form attribute is 'direction' or 'speed', and the value is one of the values below. Each endpoint also needs an API-key that has to be sent in the URL by adding `apikey=<key>` at the end.  
If a request (GET or POST) is sent to the basic URL (i.e. without `/direction` or `/speed`) a quick reference page is shown (it does not need an API-key).

##.../direction
- forward
- reverse
- left
- right

##.../speed
- stop
- slow (not yet implemented)
- medium (not yet implemented)
- fast (not yet implemented)

#API-key
For a key to use this API, contact one of the administrators of this repository.

#Run API in Docker
A Docker file contains all the commands needed to build an image. For now you don't have to change anything and you can use the Dockerfile in the repo. In the future it will have to be modified as the project changes.

###Steps

1. Make sure you are in the repo root directory and that you have the latest version.
2. Start the command line in the root directory.
3. `sudo docker build -t rc-car-api:<version> .` (don't forget the dot at the end!) Replace <version> with your own version number of course. After this, you could also use `latest` as <version>, so that Docker automatically sees this as the latest version.
4. `sudo docker run --privileged -d -p 5000:5000 rc-car-api:latest`. The `--privileged` flag is only needed here if the container needs to be able to receive a connection outside the network. For example, the website is hosted with Azure, so it is in a different network than the Raspberry.
5. After the container has been spun up, an ID appears in the command line. This ID can be used to request logs or to stop a container.
6. `sudo docker logs <containerID>` allows you to see the logs of the entered container. This allows you to check if API is running or if there are any errors.
7. If the container is running correctly, you should not get any error messages at the logs, and the following message: `* Running on <host>:5000/ (Press CTRL+C to quit)`.