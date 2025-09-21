# 🚀 Wisecow Deployment & Automation Project  

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)  
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/)  
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)  
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)  
[![Security](https://img.shields.io/badge/KubeArmor-Security-critical?style=for-the-badge&logo=shield&logoColor=white)](https://kubearmor.io/)  

This repository contains solutions for **Problem Statement 1, 2, and 3**, covering containerization, Kubernetes deployment, automation scripts, and zero-trust security using KubeArmor.

---

## 📌 Problem Statement 1: Wisecow Application Deployment  

**Objective:** Containerize and deploy the Wisecow application on Kubernetes with secure communication and CI/CD.  

✔ **Key Deliverables**  
- `Dockerfile` → Containerized Wisecow application  
- Kubernetes Manifests (`wisecow-deployment.yaml`, `daemonset.yaml`, etc.) → Deploy app to Kubernetes cluster  
- Service Exposure → Wisecow accessible inside the cluster  
- GitHub Actions Workflow → Automates image build & push to registry  
- TLS Support (Challenge Goal) → Enabled secure communication  

---

## 📌 Problem Statement 2: Automation Scripts  

Implemented multiple automation scripts in Python:  

- **System Health Monitoring (`sys_monitor.py`)**  
  Monitors CPU, memory, disk usage, and running processes. Logs warnings if thresholds exceeded.  

- **Application Health Checker (`app_check.py`)**  
  Sends HTTP requests to check uptime of an application. Determines if app is UP or DOWN based on status codes.  

- **Additional scripts:**  
  - `backup.py` – Automates directory backups  
  - `log_analyzer.py` – Extracts common patterns from logs  

📄 **Logs generated:** `sys_monitor.log`, `app_health.log`, `backup.log`  

---

## 📌 Problem Statement 3: Zero-Trust Security with KubeArmor  

**Objective:** Apply a zero-trust policy to the Wisecow workload.  

- Policy File: `kubearmor-policy.yaml`  
- Screenshot: `kubearmor-policy-violation.png` (showing blocked violation)  
- Enforced least-privilege access ensuring stricter runtime security  

---

## 🛠️ How to Run  

Clone this repository:  
```bash
git clone https://github.com/ShivaniH20/wisecow.git
cd wisecow

docker build -t wisecow-app .
docker run -p 8080:8080 wisecow-app

kubectl apply -f wisecow-deployment.yaml

python sys_monitor.py
python app_check.py

📂 Repository Structure
wisecow/
├── Dockerfile
├── wisecow-deployment.yaml
├── kubearmor-policy.yaml
├── kubearmor-policy-violation.png
├── sys_monitor.py
├── app_check.py
├── backup.py
├── log_analyzer.py
├── *.log (generated log files)


✅ Summary
Successfully containerized and deployed Wisecow on Kubernetes

Implemented automation scripts for monitoring, backups, and health checks

Secured workloads using KubeArmor zero-trust runtime policies

Delivered a CI/CD pipeline for automated build and deployment

This demonstrates strong skills in DevOps, automation, Kubernetes, and cloud-native security.
