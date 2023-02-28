FROM python:3.7-slim as builder
RUN pip install flask requests

FROM builder AS build1
WORKDIR /app
COPY . .

FROM build1 as build2
RUN groupadd -r webservice && useradd --no-log-init -r -g webservice webservice
USER webservice:webservice
CMD ["python", "app.py"]
