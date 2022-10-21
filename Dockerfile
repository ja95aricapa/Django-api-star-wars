FROM python:3.9
COPY . ./
# COPY ./requirements.txt /src/requirements.txt
# ENV APP_HOME /src
# WORKDIR $APP_HOME
EXPOSE 8000
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000
#RUN python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
#CMD ["python", "manage.py", "makemigrations", "&&", "python", "manage.py", "migrate", "&&", "python", "manage.py", "runserver", "0.0.0.0:8000"]

