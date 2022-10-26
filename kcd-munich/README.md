# Color Demo

This demo was shown at KCD Munich. It consists of some workloads (`manifest` directory) a backend and a frontend app.

Build the apps locally and swap them with Gefyra into a Kubernetes cluster which has been provisioned with the given workloads from the manifest directory.

## Try this demo

**Prerequisites:**
1. A Kubernetes cluster and a valid connection to it.
2. An [installed](https://gefyra.dev/installation/) version of Gefyra
3. Installed CLIs: `kubectl` and `docker`

### Prepare the cluster
Just apply the `demo.yaml` from the `manifests` directory to your cluster. If you wish to adapt the namespace feel free to do so, just keep in mind
that you need to tell `gefyra` about the namespace later.

**Attention** - make sure you're actually connected to the right cluster.

```bash
kubectl apply -f manifests/demo.yaml
```

### Prepare the images
To give `gefyra` some application to work with we need to build the images.

**Backend**

```bash
cd backend/
docker build -t color-backend .
```

**Frontend**

```bash
cd frontend/
docker build -t color-frontend .
```

### Install Gefyra cluster side

First we need to make sure Gefyra is installed and all cluster side components are running:

```bash
gefyra up
gefyra status
```

In some cases you may need to provide the `--endpoint` flag to point Gefyra to the correct cluster:

```bash
gefyra up --endpoint=11.11.11.11:31820
```

`31820` is the default NodePort Gefyra runs on.


### Run container with Gefyra

To connect a local container with the cluster we run it with Gefyra. Imagine this to be
`docker run` on steriods. At takes care of the connection under the hood. First we run our frontend 
image:

```bash
gefyra run -I color-frontend -N frontend --env-from pod/frontend -p 5003:5003 --rm
```

What happens here?
 - `-I color-frontend` selects the image we just built
 - `-N frontend` gives our local container a name
 - `--env-from pod/frontend` copies the environment variables from the pod `frontend` to our local container
 - `-p 5003:5003` exposes port 5003 of our container to localhost 5003
 - `--rm` removes the container as soon as it exits

Done! The container now runs within the default namespace of the cluster. To run it within a different namespace try the following:

```bash
gefyra run -I color-frontend -N frontend --env-from pod/frontend -p 5003:5003 --rm -n my-namespace
```

`-n my-namespace` makes sure your container is connected to the correct namespace.

**Use Case** - `gefyra run` allows your local container to connect to a K8s cluster and the resources within. Let's assume your container
needs to connect to a database. In case the database is accessible within the cluster your container now has access to it.

**Rule of thumb** - Use `gefyra run` when you want to connect your local container to other services within a K8s cluster.


### Bridge a workload with Gefyra

TODO


