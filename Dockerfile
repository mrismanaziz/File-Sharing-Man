# Set base-image
FROM python:3.9-slim-buster

ENV TZ="Asia/Jakarta"
ENV GIT_PYTHON_REFRESH=quiet

# Set workdir
WORKDIR /app

# Copy all files/folder from local
COPY . .

# Install dependecies
RUN pip3 install -r req*txt

# command to run
CMD ["bash", "./start"]