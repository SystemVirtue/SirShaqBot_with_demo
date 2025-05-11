FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
CMD ["bash", "-c", "python scripts/fetch_content.py && python scripts/generate_video.py && python scripts/upload_video.py"]
