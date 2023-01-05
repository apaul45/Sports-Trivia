FROM python:3.9

WORKDIR /server

COPY ./ /server

RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
