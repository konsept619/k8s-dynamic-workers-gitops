FROM registry.redhat.io/rhel9/python-312-minimal:9.7

USER 0

WORKDIR /app

COPY src/main.py /app/

ENV PYTHONUNBUFFERED=1

USER 1001

CMD ["python", "main.py"]

