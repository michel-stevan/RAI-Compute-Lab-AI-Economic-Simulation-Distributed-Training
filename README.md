# RAI Compute Lab

AI Economic Simulation & Distributed Training Sandbox

## Overview
RAI Compute Lab is a lightweight AI sandbox that demonstrates:

- Agent-based economic simulation
- Neural network training (PyTorch)
- Inference API (FastAPI)
- Designed for distributed compute integration (RAI Testnet-ready)

This repository serves as a proof-of-work prototype for AI + compute experimentation.

---

## Tech Stack
- Python
- FastAPI
- PyTorch
- NumPy
- Docker

---

## Quick Start (Local)

### 1. Clone
```bash
git clone https://github.com/YOUR_USERNAME/rai-compute-lab.git
cd rai-compute-lab
```

### 2. Build & Run (Docker Recommended)
```bash
docker-compose up --build
```

API runs at:
http://localhost:8000

Swagger docs:
http://localhost:8000/docs

---

## API Example

POST `/predict`

```json
{
  "inflation": 0.05,
  "shock": 1
}
```

---

## Roadmap
- [ ] Integrate RAI testnet compute
- [ ] Distributed training mode
- [ ] Dashboard visualization
- [ ] Multi-agent reinforcement learning
- [ ] Compute benchmarking report

---

## Vision
Exploring decentralized AI infrastructure for large-scale economic simulation and model training.

---

## License
MIT
