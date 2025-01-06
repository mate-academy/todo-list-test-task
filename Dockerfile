FROM python:3.11-slim


WORKDIR /src

COPY ./src/requirements.txt /src//requirements.txt
RUN pip install --no-cache-dir -r /src/requirements.txt


COPY ./src /src

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]