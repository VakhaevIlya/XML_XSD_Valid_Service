# XML Validator?
This service validate XML files using XSD schema.

## How to start service

- Open the project folder

- Create docker image

	`./gradlew createImage`

- Run docker image:

	`docker run -p 80:80 xml_validator`

## How to send files

### 1. You need to send XSD schema to /schema:

	curl -d @schema.xsd 0.0.0.0:80/schema

### 2. Send XML file to /validate:
	
	curl -d @valid.xml 0.0.0.0:80/validate

