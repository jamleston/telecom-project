FROM python:3.10
ENV APP_HOME=/app
WORKDIR $APP_HOME
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
