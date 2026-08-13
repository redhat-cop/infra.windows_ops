Build EE manually, push to quay.io

```
ansible-builder build
# podman build -f context/Containerfile -t ansible-execution-env:latest context
podman tag ansible-execution-env:latest quay.io/redhat-cop/apd-ee-25-windows:latest
podman push quay.io/redhat-cop/apd-ee-25-windows:latest
```
