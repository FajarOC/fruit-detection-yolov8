FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y libgl1

RUN pip install --no-cache-dir -r requirements.txt

RUN python -c "import numpy; print('✅ Numpy tersedia dengan versi:', numpy.__version__)"

COPY app.py .
COPY fruit_detection_model.pt .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
