set -e
#flake8  --exclude server,tmp
source ./bin/configuration.sh
if [ -d ../server/data/configuration.sh ]; then
  source ../server/data/configuration.sh
fi
export PYTHONPATH="."
python3.9 server/fastapi_server.py
