# INTENTIONALLY INSECURE: Trivy should report several Dockerfile findings.
FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod -R 777 /app

EXPOSE 5000

# INTENTIONALLY INSECURE: The application is explicitly run as root.
USER root

CMD ["python", "-m", "app.main"]

