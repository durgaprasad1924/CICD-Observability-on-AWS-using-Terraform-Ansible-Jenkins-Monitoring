This project demonstrates a production-style end-to-end DevOps pipeline on AWS.
It covers infrastructure provisioning, configuration management, CI/CD automation, containerization, and monitoring using industry-standard tools.

The goal is to automate build → deploy → monitor workflows with minimal manual intervention.

Architecture Overview
Terraform → AWS Infrastructure (VPC + EC2)
Ansible   → Jenkins, Docker, Monitoring Setup
GitHub    → Source Code Management
Jenkins   → CI/CD Pipeline
Docker    → Application Containerization
Prometheus & Grafana → Monitoring & Observability

┌──────────────┐
│   Developer  │
│ (Git Commit) │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   GitHub     │
│ Source Code  │
└──────┬───────┘
       │  (Webhook / Poll SCM)
       ▼
┌──────────────┐
│   Jenkins    │
│  CI/CD Tool  │
└──────┬───────┘
       │
       │ Build & Deploy
       ▼
┌──────────────┐
│   Docker     │
│ Build Image  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Docker       │
│ Container    │
│ (Flask App)  │
└──────┬───────┘
       │
       ▼
┌───────────────────────────────┐
│        AWS EC2 Instance       │
│                               │
│  ┌──────────┐  ┌───────────┐ │
│  │ Jenkins  │  │  Docker   │ │
│  └──────────┘  └───────────┘ │
│                               │
│  ┌──────────┐  ┌───────────┐ │
│  │Prometheus│  │  Grafana  │ │
│  └──────────┘  └───────────┘ │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│   Monitoring & Observability  │
│  Metrics → Prometheus         │
│  Dashboards → Grafana         │
└───────────────────────────────┘
