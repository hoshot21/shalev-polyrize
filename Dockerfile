FROM python:3.8-alpine
WORKDIR /shalev-polyrize
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "./src/API.py"]