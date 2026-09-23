#!/usr/bin/env bash
set -euo pipefail

APP_URL="${1:-https://YOUR-APP-NAME.azurewebsites.net}"

curl --fail-with-body --silent --show-error \
  -X POST "${APP_URL}/predict" \
  -H "Content-Type: application/json" \
  -d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
printf '\n'
