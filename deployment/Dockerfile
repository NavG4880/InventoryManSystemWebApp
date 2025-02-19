# Use official Python image
FROM python:3.9

# Environment variables 
#ENV DB_Name=AWSProjectPartManagDB
#ENV DB_User=AWSProjectUser
#ENV DB_Pass=AWSProjectPassword
#ENV DB_HOST=awsprojectstack-awsprojectpartmanagdb-c9rqmzsj4ifs.chg844k20aok.ap-southeast-2.rds.amazonaws.com
#ENV DB_HOST=awspartmanagementdb.chg844k20aok.ap-southeast-2.rds.amazonaws.com
# Switch user
#RUN groupadd -g 1000 ec2-user && useradd -r -u 1000 -g ec2-user ec2-user

# Set working directory
WORKDIR /app


## Copy the requirements.txt file first to leverage Docker caching
#COPY requirements.txt /app/

# Copy app files
COPY ./app /app 

# Install dependencies
RUN pip install -r requirements.txt
## Install dependencies
#RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 80

# Run the app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "app:app"]
#CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]
