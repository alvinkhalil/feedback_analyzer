#!/bin/bash
echo "Mongo skripti başladı."

# Mongonun tam hazir olmasını gözləyirik çünki tam hazır olmasa inser create işləmləri ola bilər ona görədə error verəcək
until mongo --host localhost --eval "print('MongoDB hazırdır')" > /dev/null 2>&1; do
  sleep 3
done

# Əgərb db, collection varsa skip edəcək yoxdursa create edib jsonu import edəcək
echo "Db yoxlanr..."
DB_EXISTS=$(mongo --host localhost --eval "db.getMongo().getDBNames().indexOf('feedback_db') >= 0" --quiet)

if [ "$DB_EXISTS" = "true" ]; then
  echo "Db var."
else

  mongo --host localhost --eval "db = db.getSiblingDB('feedback_db'); db.createCollection('feedback');"
  echo "Db yaradıldı."
fi

echo "JSON import edilir..."
mongoimport --host localhost --db feedback_db --collection feedback --file /data/feedback.json --jsonArray
echo "Import tamamlandı."
