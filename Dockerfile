FROM python:3.9.0-alpine
EXPOSE 8000
ADD requirements.txt .
RUN pip install --requirement requirements.txt
COPY /transparencia/ .
CMD ["python", "manage.py", "runserver"]
