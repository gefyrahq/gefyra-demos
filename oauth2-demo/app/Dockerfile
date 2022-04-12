FROM python:3.9-slim AS build-env
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8155"]

#FROM gcr.io/distroless/python3
#COPY --from=build-env /usr/local/lib/python3.9/site-packages /usr/lib/python3.9/
#COPY --from=build-env /usr/local/bin/uvicorn /app/uvicorn
#COPY main.py /app/main.py
#WORKDIR /app
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8155"]