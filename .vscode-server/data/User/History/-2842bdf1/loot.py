from cluster_creation import ClusterCreation

if __name__ == "__main__":
    # Instantiate ClusterCreation
    cluster_creator = ClusterCreation()

    # Define cluster name (you might fetch this from somewhere else)
    cluster_name = "my_cluster"

    # Call create_cluster method
    result = cluster_creator.create_cluster(cluster_name)

    # Print the result (you might handle it differently in your actual application)
    print(result)
