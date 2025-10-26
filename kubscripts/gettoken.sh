kubectl get secret <sa-name>-token -n <namespace> -o jsonpath='{.data.token}' | base64 -d
