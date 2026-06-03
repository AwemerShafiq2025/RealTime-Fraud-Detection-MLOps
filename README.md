# RealTime-Fraud-Detection-MLOps

End-to-end MLOps-style project for **real-time fraud detection** with training, serving, containerization, monitoring, and deployment options (Docker Compose + Kubernetes) plus infrastructure provisioning (Terraform).

## Repository Structure

- `main.py` — Service / inference entrypoint (real-time prediction).
- `train.py` — Model training script (generates artifacts).
- `model.pkl` — Trained model artifact.
- `scaler.pkl` — Feature scaler / preprocessing artifact.
- `requirements.txt` — Python dependencies.
- `docker-compose.yml` — Local multi-service run (app + monitoring, etc.).
- `prometheus.yml` — Prometheus scrape configuration.
- `Jenkinsfile` — CI/CD pipeline definition.
- `k8s/`
  - `deployment.yaml` — Kubernetes deployment manifest.
  - `service.yaml` — Kubernetes service manifest.
- `main.tf` — Terraform infrastructure definition (HCL).

## Quick Start (Local)

### 1) Create a virtual environment & install deps

```bash
python -m venv .venv
# Windows:
# .venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 2) (Optional) Train the model

If you want to regenerate the artifacts:

```bash
python train.py
```

### 3) Run the service

```bash
python main.py
```

> Note: Service host/port and API routes depend on `main.py`.

## Docker Compose

```bash
docker compose up --build
```

This uses:

- `docker-compose.yml` for services
- `prometheus.yml` for metrics scraping (if configured)

## Kubernetes (k8s)

Apply manifests:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Check resources:

```bash
kubectl get pods
kubectl get svc
```

## Terraform (Infrastructure)

Initialize & plan:

```bash
terraform init
terraform plan
```

Apply (be careful—may create cloud resources/costs):

```bash
terraform apply
```

## Monitoring

- Prometheus config: `prometheus.yml`
- If the app exposes `/metrics`, Prometheus can scrape it (depending on your `main.py` setup).

## CI/CD

- `Jenkinsfile` contains pipeline steps for build/test/deploy (details depend on your Jenkins setup).

## License

No license file is currently included. If you want, add `LICENSE` (e.g., MIT/Apache-2.0).
