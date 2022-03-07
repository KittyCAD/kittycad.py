FROM python:latest

RUN pip install \
	poetry

WORKDIR /usr/src/

COPY . /usr/src/

RUN poetry install

# Set the default command to bash.
CMD ["bash"]
