import subprocess

# get the cluster names
def get_cluster_names():
    process = subprocess.Popen(['kubectl', 'config', 'get-clusters'], stdout=subprocess.PIPE)
    stdout = process.communicate()[0]
    cluster_names = [y for y in (x.strip() for x in stdout.splitlines()) if y]
    cluster_names.pop(0)
    return cluster_names

# apply config management object
def set_cluster_name(cluster_names):
    for cluster in cluster_names:
        config_management="""
        apiVersion: configmanagement.gke.io/v1
        kind: ConfigManagement
        metadata:
          name: config-management
          namespace: config-management-system
        spec:
          clusterName: {}
        git:
            syncRepo: git@github.com:ejmadkins/anthos-config-management-demo.git
            syncBranch: master
            secretType: ssh
            policyDir: "config-and-policy"
        configConnector:
            enabled: true
        policyController:
            enabled: true""".format(cluster)
        subprocess.call("kubectl config use-context {}".format(cluster), shell=True)
        subprocess.call("kubectl apply -f - <<EOF{}\nEOF".format(config_management), shell=True)

if __name__ == "__main__":
    set_cluster_name(get_cluster_names())