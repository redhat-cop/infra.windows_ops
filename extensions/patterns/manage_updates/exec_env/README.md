Build EE manually, push to quay.io

```
ansible-builder build
# podman build -f context/Containerfile -t ansible-execution-env:latest context
podman tag ansible-execution-env:latest quay.io/p3ck/apd-ee-25-experience:latest
podman push quay.io/p3ck/apd-ee-25-experience:latest
```
