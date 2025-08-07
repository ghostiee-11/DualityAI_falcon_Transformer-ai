# 🛡️ SafeGuard AI

**AI-Powered Emergency Equipment Compliance & Safety Monitoring System**

## 🔍 Overview

**SafeGuard AI** automates the detection and monitoring of emergency equipment (fire extinguishers, oxygen tanks, etc.) using advanced object detection models. Designed for critical environments like hospitals, airports, schools, and public spaces, it ensures real-time compliance monitoring, alerts, and safety audit automation.

Developed as part of a hackathon by **Team Transformer-AI**, the system went through multiple R&D iterations with a strong focus on real-world performance.

---

## 🚨 Problem Statement

Manual safety audits for critical emergency equipment are:

- **Time-consuming**
- **Error-prone**
- **Non-scalable**

This results in **high risk during emergencies** if equipment is missing, blocked, or displaced.

---

## ✅ Solution

SafeGuard AI uses **custom-trained YOLOv8 models** (fused with transformers) to detect and monitor emergency tools in real-time. It:

- Detects equipment presence & occlusion
- Raises instant alerts
- Scores compliance
- Displays live monitoring dashboards
- Provides simulation and voice assistant support

---

## ⚙️ Tech Stack

| Area | Tech |
|------|------|
| Detection | YOLOv8 (with Swin Transformer backbone along with Spatial Attention Modules for Feature Enhancement) |
| Dashboard | Flask / Streamlit |
| Data Processing | OpenCV |
| Synthetic Data | Falcon |
| Alerts | Twilio / SMTP |
| Storage | SQLite / CSV |

---

## 🧪 Development Iterations

### 🔹 Iteration 1 – Baseline YOLOv8n
- **Goal:** Quick setup with minimal config
- **mAP@0.5:** ~80%
- **Outcome:** Established working prototype, struggled with occlusion

### 🔹 Iteration 2 – Data Augmentation + Longer Training
- **Augmentations:** Mosaic, MixUp, Color Jitter, Perspective, Rotation
- **Epochs:** 125
- **mAP@0.5:** ~95%
- **Outcome:** Significantly improved generalization

### 🔹 Iteration 3 – CBAM + FasterNet (Blocked)
- **Tried:** Attention modules, lightweight CNNs, SIoU loss
- **Issue:** Incompatibility with YOLOv8's dynamic shape system
- **Outcome:** Model failed to converge

### 🔹 Iteration 4 – YOLOv8 + Swin Transformer
- **Fusion:** Swin as backbone for YOLOv8
- **Training:** Mixed precision, custom layers
- **mAP@0.5:** **96%**
- **Outcome:** Best results; robust under clutter, low-light, rotation

---

## 🧠 Key Innovations

- ✅ First use of Swin Transformer + YOLOv8 on this domain
- ✅ Custom domain-specific augmentations
- ✅ Performance across real-world challenges (low-light, clutter)
- ✅ Model-ready compliance scoring & location deviation logic

---

## 🌐 Target Environments

- 🏥 Hospitals (ICUs, ERs)
- ✈️ Airports, 🏬 Malls
- 🏫 Schools, 🏢 Offices
- 🏛️ Government Buildings

---

## 🧭 Features

- Real-time object detection
- Occlusion and displacement alerts
- Location-based compliance scoring
- Smart notifications (Email/SMS/WhatsApp)
- Live dashboard with floor plan overlays
- Voice assistant & simulation mode
- Audit reports generation

---

## 🔮 Future Work

- Fix integration of **CBAM + SIoU** with dynamic adapters
- Add **location compliance scoring**
- Extend **simulation** for emergency drills
- Expand synthetic data capabilities

---

## 📢 Bonus Idea

Integrate with **BIM (Building Information Modeling)** systems for floor-aware detection and tracking, and link with **IoT sensors** for proactive fire/emergency readiness.

---

## 👥 Team

**Team Name:** Transformer-AI  
Finalists in BuildwithDelhi 2.0

## The Document of this task is :
https://docs.google.com/document/d/1jntvAiQgfSUsj8yilLnkrQ2Ty4M8j_lEwSrwW5u_McI/edit?usp=sharing

## The drive link for this task containing all the results is:-
https://drive.google.com/drive/u/0/folders/1HyytmSDOv_zWouzJTnRBHLOGW53QsYTp
