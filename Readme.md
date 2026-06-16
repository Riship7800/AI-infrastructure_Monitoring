# AI Infrastructure Monitoring & Incident Analysis Platform

An AI-powered monitoring platform built using Kubernetes, Prometheus, Grafana, Alertmanager, and Ollama.

## Features

- Real-time infrastructure monitoring
- AI-powered alert analysis
- Root cause suggestions
- Grafana dashboards
- Local LLM deployment using Ollama

## Technologies

- Kubernetes
- Docker
- Prometheus
- Grafana
- Alertmanager
- Ollama
- Python

## Architecture

![Architecture](architecture.png)

## Example AI Analysis

Input Alert:

CPU usage exceeded 90%

AI Response:

The node experienced sustained CPU saturation. Most likely causes include:

- High pod resource consumption
- Infinite loop process
- Resource limits not configured

Recommended Actions:

- Check top consuming pods
- Configure requests and limits
- Scale deployment
