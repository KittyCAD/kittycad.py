FROM python:3.13

RUN pip install \
	poetry

WORKDIR /home/user/src/

COPY . /home/user/src/

RUN poetry update && poetry install

# Set the default command to bash.
CMD ["bash"]
