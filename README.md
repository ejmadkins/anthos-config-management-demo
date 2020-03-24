# Anthos Config Management Demo
This is a short demo of Anthos Config Management.  It covers configuring following:
* Kubernetes Objects on Multiple Clusters
* Cluster Selectors
* Namespace Selectors
* Namespace labels and Pod Security using the Policy Controller

```
config-and-policy
├── cluster
│   ├── constraint-namespace-cost-centre.yaml
│   ├── constraint-privilege-escalation.yaml
│   ├── pod-reader-clusterrole.yaml
│   └── pod-reader-clusterrolebinding.yaml
├── clusterregistry
│   ├── cluster-lon-dev.yaml
│   ├── cluster-lon-prod.yaml
│   └── selector-prod.yaml
├── namespaces
│   ├── audit
│   │   └── namespace.yaml
│   ├── istio-system
│   │   └── namespace.yaml
│   └── t-rex-app
│       ├── deployment.yaml
│       ├── ingress.yaml
│       ├── namespace.yaml
│       ├── node-port.yaml
│       └── privileged-nginx.yaml
└── system
    ├── README.md
    └── repo.yaml
```

## Prereqs
This demo assumes that the following prereqs are met:
* [Nomos](https://cloud.google.com/anthos-config-management/docs/how-to/nomos-command) is installed

## Anthos Config Management Setup
Follow these steps to get ACM on your clusters.

Create the GKE clusters:
```
for cluster in lon-prod lon-dev; do
gcloud container clusters create ${cluster} \
--zone europe-west2-a
done
```
Configure your Git repository and [Grant the Operator read-only access to Git](https://cloud.google.com/anthos-config-management/docs/how-to/installing#git-creds-secret)

Execute acm_cluster_setup.py file to configure the operator: 
```
python acm-setup/acm_cluster_setup.py
```
## Kubernetes Objects on Multiple Clusters
Verify that the objects configured in the git repo are deployed into the cluster.

## Cluster Selectors
Check out the labels attached to clusters and the ClusterSelector:
```
bat config-and-policy/clusterregistry/cluster-lon-prod.yaml && bat config-and-policy/clusterregistry/cluster-lon-dev.yaml
```

For production clusters we need to ensure that the audit team have their own namespace where they can deploy their workloads.
Verify the audit namespace annotation:
```
bat config-and-policy/namespaces/audit/namespace.yaml
```

The audit namespace should only be present on the lon-prod cluster, we can check this by verifying the namespaces on each cluster:

```
python command_runner.py -c "kubectl get ns"
```

## Namespace Selectors

## Namespace labels using the Policy Controller
The `istio-system` namespace should be deployed across all clusters, there is a namespace label constraint in place that mandates a cost centre label much be defined to each namespace.

Verify that the namespace has not been deployed to clusters:
```
python command_runner.py -c "kubectl get ns"
```

Edit the istio-system-namespace.yaml file and uncomment the last two lines
```
vi config-and-policy/namespaces/istio-system-namespace.yaml
```

Check again to make sure that the namespace is now present:
```
python command_runner.py -c "kubectl get ns"
```

## Pod security using the Policy Controller
The NGINX pod needs to be deployed in the t-rex-app namespace.

The NGINX container has been configured as a privilged container, due to the constraint in place to deny privileged containers from running the pod is not deployed.

Change the NGINX container privileged to false.