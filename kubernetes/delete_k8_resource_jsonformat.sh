#!/bin/bash
name_space=$1
thereshold=$2

for i in $name_space
do
  deployment_name=$(kubectl get deployments -n $i -o json | jq -r '.items[] | select((now - (.metadata.creationTimestamp | fromdateiso8601) | . / 60) > '"${thereshold}"') | .metadata.name');

  service_name=$(kubectl get service -n $i -o json | jq -r '.items[] | select((now - (.metadata.creationTimestamp | fromdateiso8601) | . / 60) > '"${thereshold}"') | .metadata.name');

  for j in ${deployment_name}
    do
    echo "kubectl delete deployment $j -n $i"
    #kubectl delete deployment $j -n $i 
  done 
  for j in ${service_name}
    do
    echo "kubectl delete service $j -n $i"
    #kubectl delete service $j -n $i
  done
#kubectl get delete ns
done




