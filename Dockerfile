FROM python:3.11-slim
WORKDIR /app
COPY web_server.py /app/
COPY index.html /app/
EXPOSE 8080
CMD ["python", "web_server.py"]
