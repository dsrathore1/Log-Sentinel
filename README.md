# LogSentinel

**Event-driven log monitoring and anomaly detection on AWS**

---

## Overview

LogSentinel is a cloud-native system designed to simulate real-world infrastructure log pipelines. It ingests logs from compute instances, stores them in cloud storage, and prepares them for event-driven processing and analytics.

The project focuses on demonstrating core cloud engineering principles such as event-driven architecture, distributed logging, and scalable infrastructure design using AWS services.

---

## Architecture Summary

The system begins with log generation on compute instances and flows through cloud storage, where events are triggered for downstream processing.

**Current Flow (Phase 1):**

EC2 (log generation) → S3 (centralized storage)

This forms the foundation for an event-driven pipeline that will later incorporate serverless processing and Kubernetes-based analytics.

---

## Key Components

* **Compute Layer**
  Log generation is simulated on a virtual machine using **Amazon EC2**.
  This represents application servers in a production environment.

* **Storage Layer**
  Logs are stored in **Amazon S3**, acting as a durable and scalable ingestion layer.

* **Log Simulation**
  A custom script continuously generates logs with varying severity levels (INFO, WARNING, ERROR), mimicking real application behavior.

---

## Features Implemented (Phase 1)

* Continuous log generation on compute instance
* Automated log uploads to cloud storage
* Centralized log aggregation model
* Foundation for event-driven processing

---

## Engineering Decisions

* **S3 as ingestion layer**
  Chosen for durability, scalability, and native event integration with downstream services.

* **EC2 for log simulation**
  Provides realistic control over log generation, closely resembling production workloads.

* **Batch upload approach**
  Periodic uploads reduce overhead and simulate real-world log shipping patterns.

---

## Current Limitations

* No real-time processing yet
* No log parsing or filtering
* No observability or alerting
* No containerized services

These limitations are intentional and will be addressed in upcoming phases.

---

## Next Steps

* Integrate event-driven processing using **AWS Lambda**
* Implement log parsing and error extraction
* Deploy analytics services on **Amazon EKS**
* Containerize services and store images in **Amazon ECR**
* Introduce monitoring and alerting

---

## Learning Outcomes

This phase focuses on:

* Designing a log ingestion pipeline
* Understanding cloud storage as a system boundary
* Simulating real infrastructure behavior
* Building the foundation for event-driven systems

---

## Status

Phase 1 Completed — Log ingestion pipeline established and operational.
