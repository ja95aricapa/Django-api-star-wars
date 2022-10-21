FROM python:3.9
COPY . ./
EXPOSE 80
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "80"]
