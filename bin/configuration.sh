# Application
export APP_TIMEOUT='5'
export TOKEN='test'
export APP_MODE='debug' # debug release

# DB
export REDIS_HOST='r-h.redis.rds.aliyuncs.com:6379'
export REDIS_PASS='pass!'
export PG_URI='postgresql://u:tests@pgm-tests.pg.rds.aliyuncs.com/db'

# Biz
export APP_SETTINGS="{
  \"APP_CONF\": {
    \"APP_NAME\":\"Demo\",
    \"APP_TIMEOUT\":\"$APP_TIMEOUT\",
    \"APP_MODE\":\"$APP_MODE\",
    \"PORT\":9000,
    \"TOKEN\":\"$TOKEN\"
  },
  \"REDIS_CONF\": {
    \"DB\":\"5\",
    \"REDIS_HOST\":\"$REDIS_HOST\",
    \"REDIS_PASS\":\"$REDIS_PASS\"
  },
  \"PG_CONF\": {
    \"PG_URI\":\"$PG_URI\",
    \"NAME\":\"test\"
  }
}"

echo "$APP_SETTINGS" >app_settings.txt
export APP_SETTINGS=$(python -c "import os; import json; print(json.dumps(json.loads(os.environ['APP_SETTINGS'].replace('\n', '')), separators=(',', ':')))" | base64)
echo "$APP_SETTINGS" >>app_settings.txt
