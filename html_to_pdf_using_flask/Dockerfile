FROM python
WORKDIR /app
ADD . /app
RUN apt update -y
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]