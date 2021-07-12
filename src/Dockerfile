FROM python:3.7

#ADD src /src
ADD .. .

RUN pip install --upgrade pip

CMD ["python", "-m", "unittest", "discover", "-s","Tests"]