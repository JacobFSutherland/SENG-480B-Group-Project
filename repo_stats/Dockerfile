from sonarsource/sonar-scanner-cli

# Set up working dir
WORKDIR /app

# Copy the helper.py and requirements.txt files to the working directory
COPY helper.py requirements.txt sonar-project.properties ./

# Install the dependencies from requirements.txt
RUN pip install -r requirements.txt

#Install git
RUN apk add git

# Run the python file
CMD ["python", "helper.py"]