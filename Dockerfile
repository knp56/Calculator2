FROM python:latest

#ADD src /src
ADD src /src

ENV PYTHONPATH "${PYTHONPATH}:/src/Calculator:/src/CsvReader:/src/Test:/src/Operations:/src/Statistics:/src"

RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install scipy

CMD ["python", "-m", "unittest", "discover", "-s","Test"]