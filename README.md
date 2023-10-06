# README

```bash
multipass launch \
    --cloud-init ~/git/telco/telco-hacks/cloud-init/charm-dev-juju-3.1.yaml \
    --memory 8G \
    --cpus 2 \
    --disk 80G \
    --mount ~/git/telco/:/home/ubuntu/telco \
    --timeout 1200 \
    --name fiveg \
    22.04
```
