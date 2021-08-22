# URL-Service-Project

## Prerequisites
1) Docker has been installed and is running
2) Clone the respective repository using the command:

`git clone git@github.com:riadinesh/URL-Service-Project.git`

3) Enter the URL-Service Project directory

## Running the Service
Create an image and container by running the file below using the command:

`bash run.sh`

## Launching the Service
Once the program is dockerized, route to the address:
http://127.0.0.1:5000/home

To check whether a URL contains malware, route the address:
http://127.0.0.1:5000/url_name?url=http://test.com

To add malware URLs to the database, route to the address:
http://127.0.0.1:5000/add

To display the list of malware URLs, route to the address:
http://127.0.0.1:5000/display

Navigate throughout the application as desired



Create an image using the command 

`docker build --tag "image name" .`

After the image is created, containerize the image using the command

`docker run --name "container name" -p 5000:5000 "container name"`

Once the program is dockerized, route to the address provided and change the port numbers to 127.0.0.1:5000

Visit the home page by routing to /home

Navigate throughout the application as desired




