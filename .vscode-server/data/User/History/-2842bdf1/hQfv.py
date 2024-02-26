from cluster_creation import ClusterCreation
from ansible_config import AnsibleConfiguration

if __name__ == "__main__":
    ansible_config = AnsibleConfiguration('cluster_config.yml')
    cluster_creator = ClusterCreation(ansible_config)
    cluster_name = "my_cluster"
    result = cluster_creator.create_cluster(cluster_name)
    print(result)
