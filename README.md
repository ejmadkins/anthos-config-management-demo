# Anthos Config Management Demo
This is a short demo of Anthos Config Management.  It covers configuring following:
* Kubernetes Objects on Multiple Clusters
* Cluster Selectors
* Namespace labels and Pod Security using the Policy Controller

```
config-and-policy
├── cluster
│   ├── constraint-containers-must-be-limited.yaml
│   ├── constraint-namespace-cost-centre.yaml
│   ├── constraint-privilege-escalation.yaml
│   ├── pod-reader-clusterrole.yaml
│   └── pod-reader-clusterrolebinding.yaml
├── clusterregistry
│   ├── cluster-aws.yaml
│   ├── cluster-gcp.yaml
│   ├── selector-aws.yaml
│   └── selector-gcp.yaml
├── namespaces
│   ├── audit
│   │   └── namespace.yaml
│   └── t-rex-app
│       ├── configmap.yaml
│       ├── deployment.yaml
│       ├── namespace.yaml
│       ├── ops-role.yaml
│       ├── ops-rolebinding.yaml
│       └── service.yaml
└── system
    ├── README.md
    └── repo.yaml
```
