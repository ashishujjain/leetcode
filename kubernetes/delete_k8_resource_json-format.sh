#!/bin/bash
NameSpace=$1
DELETE_THRESHOLD_MINUTES=$2
k8_objects="deployments services"
echo "NameSpace = $NameSpace"
echo "DELETE_THRESHOLD_MINUTES = $DELETE_THRESHOLD_MINUTES"

echo ""
echo ""

clean_up () {
  #set -x
  input=$1
  while IFS= read -r LINE; do
    # Split the line into NAMESPACE DEPLOYMENT_NAME and CREATION_TIMESTAMP
    IFS="|" read -r NAMESPACE DEPLOYMENT_NAME CREATION_TIMESTAMP <<< "$LINE"
    echo "NAMESPACE : ${NAMESPACE} and DEPLOYMENT_NAME : $DEPLOYMENT_NAME and CREATION_TIMESTAMP : $CREATION_TIMESTAMP"
    echo ""
    
    # Calculate age of deployment in minutes
    
    deployment_creation_epoch=$(date -u -j -f "%Y-%m-%dT%H:%M:%SZ" "$CREATION_TIMESTAMP" +%s)
    current_epoc=$(date -u +%s)
    echo "deployment_creation_epoch in UTC format in seconds : $deployment_creation_epoch"
    echo "current_epoc in UTC format in seconds : $current_epoc"  
    diff=$((current_epoc - deployment_creation_epoch)) 
    echo "difference between current_epoc and deployment_creation_epoch in UTC format in seconds : $diff"  
    diff_min=$((diff / 60))
    AGE_MINUTES=${diff_min}
    AGE_MINUTES1=$(( (current_epoc - deployment_creation_epoch) / 60))
    echo "AGE_MINUTES = ${AGE_MINUTES}"
    echo "AGE_MINUTES1 = ${AGE_MINUTES1}"
    AGE_MINUTES2=$(( ($(date -u +%s) - $(date -u -j -f "%Y-%m-%dT%H:%M:%SZ" "$CREATION_TIMESTAMP" +%s)) / 60 ))
    echo "AGE_MINUTES2 = ${AGE_MINUTES2}"
    # Check if deployment is older than the threshold
    if [[ $AGE_MINUTES -gt $DELETE_THRESHOLD_MINUTES ]]; then
      echo "Deleting deployment $DEPLOYMENT_NAME (created $AGE_MINUTES minutes ago)"
      echo "kubectl delete deployment $DEPLOYMENT_NAME -n $NAMESPACE"
    else
      echo "Skipping deployment $DEPLOYMENT_NAME (created $AGE_MINUTES minutes ago)"
    fi
    echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
  done <<< "$input"
}

for NAMESPACE in $NameSpace
do
  for object in ${k8_objects}
  do
    # Get deployments and filter by namespace and label, then extract creation timestamps
    #DEPLOYMENTS=$(kubectl get deployments -n $NAMESPACE -o go-template --template='{{range .items}}{{.metadata.name}}|{{.metadata.creationTimestamp}}{{"\n"}}{{end}}')

    object_variable=$(kubectl get $object -n $NAMESPACE -o jsonpath='{range .items[*]}{.metadata.namespace}|{.metadata.name}|{.metadata.creationTimestamp}{"\n"}{end}')
    clean_up "$object_variable"
  done
  echo ""
  echo "-------------------------------------------------------"
done





