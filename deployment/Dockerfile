# Use official Python image
FROM python:3.9

# Environment variables you can use this to keep your personal values 
#ENV DB_Name=<REPLACE_WITH_DB_Name>
#ENV DB_User=<REPLACE_WITH_DB_UserName>
#ENV DB_Pass=<REPLACE_WITH_DB_Password>
#ENV DB_HOST=<REPLACE_WITH_DB_ARN>.<REPLACE_WITH_AWS_REGION>.rds.amazonaws.com


# Set working directory
WORKDIR /app


# Copy app files
COPY ./app /app 

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 80

# Run the app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "app:app"]
#CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]
