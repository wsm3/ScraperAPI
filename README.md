
Dockerfile for build Scraper API. Python Flask Chrome and PhantomJS.

### Information

The image is build with the following dependencies:
- latest Chrome and chromedriver
- latest stable PhantomJS webkit (v2.1.1)
- Python 3
- Xvfb and the python wrapper - pyvirtualdisplay


# USE
# Guide for the docker installation @digitalocean
	https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04
	

# 1 Build the docker
    docker build . -t scraperapi:scraper


# 2 Run the docker
    docker run --privileged -p 5056:5056 -d -it scraperapi:scraper
    
    
# 3 Get page html
Your can use Chrome or PhantomJS drivers.

####Chrome
```bash
curl -i http://localhosy:5056/get_page?url=https://google.com
```


####PhantomJS
```bash
curl -i http://localhosy:5056/get_page?url=https://google.com&driver=PhantomJS
```


## response:
	200:
	- status_code: 200
	- html: html code
	500:
	- status_code: 500
	- erro: error message