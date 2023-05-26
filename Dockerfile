FROM python:3.9

RUN pip install \
	poetry@1.4.2

WORKDIR /home/user/src/

COPY . /home/user/src/

RUN poetry update && poetry install

# Set the default command to bash.
CMD ["bash"]
