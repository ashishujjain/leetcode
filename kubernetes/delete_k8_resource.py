#https://github.com/kubernetes-client/python

import datetime
from kubernetes import client, config

def delete_old_deployments_services(apps_api_instance, core_api_instance, namespace, threshold_sec):
    # Get Deployments
    deployments = apps_api_instance.list_namespaced_deployment(namespace)
    for deployment in deployments.items:
        creation_timestamp = deployment.metadata.creation_timestamp
        print (f"creation_timestamp for the deployments {deployment.metadata.name} in the namespace {namespace} is {creation_timestamp}")
        if is_old(creation_timestamp, threshold_sec):
            print(f"Deleting Deployment: {deployment.metadata.name}")
            apps_api_instance.delete_namespaced_deployment(deployment.metadata.name, namespace)

    # Get Services
    services = core_api_instance.list_namespaced_service(namespace)
    for service in services.items:
        creation_timestamp = service.metadata.creation_timestamp
        print (f"creation_timestamp for service {service.metadata.name} in the namespace {namespace} is {creation_timestamp}")
        if is_old(creation_timestamp, threshold_sec):
            print(f"Deleting Service: {service.metadata.name}")
            core_api_instance.delete_namespaced_service(service.metadata.name, namespace)

def is_old(creation_timestamp, threshold_sec):
    now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    time_difference = now - creation_timestamp
    return time_difference.total_seconds() > threshold_sec  # 15 minutes in seconds

def main():
    config.load_kube_config()  # Assumes kubeconfig is set up properly

    apps_v1 = client.AppsV1Api()
    core_v1 = client.CoreV1Api()
    
    # Specify the namespaces you want to check
    namespaces = ["test", "test1", "test2"]
    DELETE_THRESHOLD_SECONDS=300 #15 min
    for namespace in namespaces:
        delete_old_deployments_services(apps_v1, core_v1, namespace, DELETE_THRESHOLD_SECONDS)

if __name__ == "__main__":
    main()
