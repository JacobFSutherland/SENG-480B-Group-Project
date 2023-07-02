from python:3.8-alpine

# Set up working dir
WORKDIR /app

# Copy the helper.py and requirements.txt files to the working directory
COPY helper.py requirements.txt ./

# Install the dependencies from requirements.txt
RUN pip install 

#Install git
RUN apk add git

# Run the python file
CMD ["python", "helper.py"]