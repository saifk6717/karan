FROM python:3.6
WORKDIR /usr/app/src
RUN pip install pandas
COPY main.py marvel.py ./
CMD ["python", "main.py"]
CMD ["python", "marvel.py"]
