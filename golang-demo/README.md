# Gefyra Golang Hot Reload Example App


Start the Cluster and install the workloads:
```
cd golang-demo
deck get deck.yaml
```

Once everything is up and running, you can visit http://gefyra-golang.127.0.0.1.nip.io:8080/ to verify.

Enter Gefyra:
```
cd app
docker build .  -t gefyra-golang-example

gefyra up
gefyra run -i gefyra-golang-example -N gefyra-golang-example -n golang-demo -c air -v $(pwd):/app
gefyra bridge -N gefyra-golang-example --container-name gefyra-golang-demo --deployment gefyra-golang-demo --port 3333:3333 -n golang-example
```

Once the bridge is established, try changing the code in main.go and reloading the page to see your changes reflected without rebuilding/restarting the container.

## Note
We install https://github.com/cosmtrek/air during the Docker build. In a production environment, you'd want to define a Docker build target or use a different Dockerfile altogether.