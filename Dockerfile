FROM python:latest

RUN pip install \
	openapi-python-client

# Set the default command to bash.
CMD ["bash"]
