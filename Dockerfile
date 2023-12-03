FROM python:3.8.10-buster

WORKDIR /app

COPY requirements.txt .
# ① Install some dependencies
RUN pip install -r requirements.txt

# ② Copy the setup script
COPY . .

CMD ["python", "app.py"]