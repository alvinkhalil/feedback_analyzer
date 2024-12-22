FROM mongo:5.0


COPY mongo-init.sh /docker-entrypoint-initdb.d/mongo-init.sh
COPY feedback.json /data/feedback.json

RUN chmod +x /docker-entrypoint-initdb.d/mongo-init.sh
