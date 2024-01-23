#!/bin/bash
name_space=$1
DELETE_THRESHOLD_MINUTES=$2

echo "NameSpace = $name_space"
echo "DELETE_THRESHOLD_MINUTES = $DELETE_THRESHOLD_MINUTES"

for NAMESPACE in $name_space
do

  # Get deployments and filter by namespace and label, then extract creation timestamps
  DEPLOYMENTS=$(kubectl get deployments -n $NAMESPACE -o go-template --template='{{range .items}}{{.metadata.name}}|{{.metadata.creationTimestamp}}{{"\n"}}{{end}}')

  while IFS= read -r LINE; do
    # Split the line into deployment name and creation timestamp
    IFS="|" read -r DEPLOYMENT_NAME CREATION_TIMESTAMP <<< "$LINE"
    echo "DEPLOYMENT_NAME : $DEPLOYMENT_NAME and CREATION_TIMESTAMP : $CREATION_TIMESTAMP"
    # Calculate age of deployment in minutes
    deployment_creation_epoch=$(date -u -j -f "%Y-%m-%dT%H:%M:%SZ" "$CREATION_TIMESTAMP" +%s)
    current_epoc=$(date -u +%s)
    echo "deployment_creation_epoch : $deployment_creation_epoch"
    echo "current_epoc : $current_epoc"  
    diff=$((current_epoc - deployment_creation_epoch))  
    diff_min=$((diff / 60))
    AGE_MINUTES=${diff_min}
    #AGE_MINUTES=$(((current_epoc - deployment_creation_epoch)) / 60)
    #AGE_MINUTES=$(( ($(date +%s) - $(date -d "$CREATION_TIMESTAMP" +%s)) / 60 ))
    echo "AGE_MINUTES = ${AGE_MINUTES}"
    # Check if deployment is older than the threshold
    if [[ $AGE_MINUTES -gt $DELETE_THRESHOLD_MINUTES ]]; then
      echo "Deleting deployment $DEPLOYMENT_NAME (created $AGE_MINUTES minutes ago)"
      echo "kubectl delete deployment $DEPLOYMENT_NAME -n $NAMESPACE"
    else
      echo "Skipping deployment $DEPLOYMENT_NAME (created $AGE_MINUTES minutes ago)"
    fi
  done <<< "$DEPLOYMENTS"
done








