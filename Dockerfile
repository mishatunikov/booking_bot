FROM python:3.12

WORKDIR /app

COPY requirements.in .

RUN pip install pip-tools
RUN pip-compile requirements.in
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["python", "main.py"]