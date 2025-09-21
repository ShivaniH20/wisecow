📌 Problem Statement 1: Wisecow Application Deployment

Objective: Containerize and deploy the Wisecow application on Kubernetes with secure communication and CI/CD.

✔ Key Deliverables:

Dockerfile → Containerized Wisecow application.

Kubernetes Manifests (wisecow-deployment.yaml, daemonset.yaml, etc.) → Deploy app to Kubernetes cluster.

Service Exposure → Wisecow accessible inside the cluster.

CI/CD (GitHub Actions) → Automates image build & push to registry.

TLS Support (Challenge Goal) → Enabled secure communication.

📌 Problem Statement 2: Automation Scripts

Implemented two automation scripts in Python:

System Health Monitoring (sys_monitor.py)

Monitors CPU, memory, disk usage, and running processes.

Logs warnings if thresholds exceeded.

Application Health Checker (app_check.py)

Sends HTTP requests to check uptime of an application.

Determines if app is UP or DOWN based on status codes.

Additional scripts included:

Backup Automation (backup.py) – Automates directory backups.

Log Analyzer (log_analyzer.py) – Extracts common patterns from logs.

📄 Logs generated: sys_monitor.log, app_health.log, backup.log

📌 Problem Statement 3: Zero-Trust Security with KubeArmor

Objective: Apply a zero-trust policy to the Wisecow workload.

Policy File: kubearmor-policy.yaml

Screenshot: kubearmor-policy-violation.png (showing blocked violation)

Enforced least-privilege access ensuring stricter runtime security.

🛠️ How to Run
Clone this repository:
git clone https://github.com/ShivaniH20/wisecow.git
cd wisecow

Build and run container locally:
docker build -t wisecow-app .
docker run -p 8080:8080 wisecow-app

Deploy on Kubernetes:
kubectl apply -f wisecow-deployment.yaml

Run monitoring scripts:
python sys_monitor.py
python app_check.py

📂 Repository Structure
wisecow/
│── Dockerfile
│── wisecow-deployment.yaml
│── kubearmor-policy.yaml
│── kubearmor-policy-violation.png
│── sys_monitor.py
│── app_check.py
│── backup.py
│── log_analyzer.py
│── *.log (generated log files)

Summary
Successfully containerized and deployed Wisecow on Kubernetes.
Implemented automation scripts for monitoring, backups, and health checks.
Secured workloads using KubeArmor zero-trust runtime policies.
Delivered a CI/CD pipeline for automated build and deployment.
This demonstrates strong skills in DevOps, automation, and cloud-native security.

✨ Author: Shivani H
🔗 Repo: ShivaniH20/wisecow
