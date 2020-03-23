# Anthos Config Management Demo
This is a short demo of Anthos Config Management.  It covers configuring following:
* Kubernetes Objects on Multiple Clusters
* Cluster Selectors
* Namespace Selectors
* Namespace labels and Pod Security using the Policy Controller

## Prereqs
This demo assumes that the following prereqs are met:
* Nomos is installed

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

## Namespace labels and Pod Security using the Policy Controller