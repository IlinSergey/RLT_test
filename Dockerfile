FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py /app/
COPY config.py /app/
COPY db.py /app/
COPY utils.py /app/

CMD ["python", "bot.py"]