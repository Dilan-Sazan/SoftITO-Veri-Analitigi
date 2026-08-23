FROM python:3.12-slim



WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY *.xlsx .
COPY *.py .

EXPOSE 8888

CMD ["bash"]