FROM python:3.11
WORKDIR /
RUN pip install --upgrade pip
RUN pip install gunicorn
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
