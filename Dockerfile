FROM python:3.11

ADD drone.py .
ADD tello.py .

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org boto3

CMD ["python", "./drone.py"]