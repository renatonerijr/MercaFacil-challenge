FROM python:3.8

# Create code directory and change to it
RUN mkdir /code
WORKDIR /code

# Make sure everything will be displayed in logs. MORE: https://stackoverflow.com/questions/59812009/what-is-the-use-of-pythonunbuffered-in-docker-file
ENV PYTHONUNBUFFERED 1

# Install python requirements
ADD requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the code to the folder
ADD . /code/

ENTRYPOINT ["uvicorn", "--reload", "--host", "0.0.0.0", "app:app"]