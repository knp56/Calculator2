FROM python:latest

#ADD src /src
ADD . /src

ENV PYTHONPATH "${PYTHONPATH}:/src/Calculator:src/CsvReader:/src/Test:/src/Statistics:/src"

RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install scipy

CMD [ "python", "-m", "unittest", "discover", "-s", "/src/Test" ]