# AI Safety Guardrails

This repository contains guardrails for AI systems:
- **Kyverno policies** for Kubernetes security and compliance
- **Pydantic validators** for robust Python data validation in AI pipelines
- **S3 lock config** for infrastructure state management

## Directory Structure
```
├── kyverno/          # Kubernetes policies
├── pydantic/         # Python validation models
├── infra/            # Infrastructure configurations
└── README.md
```

## Components
- **Kyverno**: Policy-as-code for cluster security
- **Pydantic**: Type-safe data models for AI inputs/outputs
- **S3 Lock**: Prevent concurrent modifications to state files