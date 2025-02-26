FROM python:latest

WORKDIR /app

EXPOSE 8000

COPY . .

RUN pip install -r requirements.txt

CMD ["python3" , "bakery/manage.py","runserver" , "0.0.0.0:8000"]