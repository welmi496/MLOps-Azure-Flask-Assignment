# Flask Iris MLOps Pipeline

This project provides a testable Flask API, GitHub Actions continuous integration, and Azure Pipelines continuous delivery to Azure App Service.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python train.py
flask --app app run --port 8000
```

Open `http://127.0.0.1:8000`. In another terminal, run:

```bash
./make_predict_azure_app.sh http://127.0.0.1:8000
```

## Verify quality

```bash
source .venv/bin/activate
flake8 app.py train.py tests
pytest -q
```

## Before cloud deployment

1. Replace `YOUR-ARM-SERVICE-CONNECTION` and `YOUR-APP-NAME` in `azure-pipelines.yml`.
2. Train and commit `iris_model.joblib` by running `python train.py`.
3. Set the App Service startup command to `gunicorn --bind=0.0.0.0:8000 app:app`.
4. Pass the deployed base URL to `make_predict_azure_app.sh`.

See `MLOps_Assignment_Report.docx` for the conceptual answers, deployment procedure, screenshot checklist, and submission fields.
