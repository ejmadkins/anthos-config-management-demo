import subprocess
import argparse

# get the cluster names
def get_cluster_names():
    process = subprocess.Popen(['kubectl', 'config', 'get-clusters'], stdout=subprocess.PIPE)
    stdout = process.communicate()[0]
    cluster_names = [y for y in (x.strip() for x in stdout.splitlines()) if y]
    cluster_names.pop(0)
    return cluster_names

# apply config management object
def execute_command(cluster_names, command):
    for cluster in cluster_names:
        subprocess.call("kubectl config use-context {}".format(cluster), shell=True)
        subprocess.call("{}".format(command), shell=True)

# get the command from the user
def get_command():
    parser = argparse.ArgumentParser(description='Gets a kubectl command from a user')
    parser.add_argument('-c', "--command", help="enter a kubectl command", type=str, required=True, default=True)
    args = parser.parse_args()
    return(args.command)


if __name__ == "__main__":
    execute_command(get_cluster_names(), get_command())