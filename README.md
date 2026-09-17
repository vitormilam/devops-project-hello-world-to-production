# Part 1 - What we will learn:

- Version Control
- Containers
- CI - Automation: Github Actions
- IaC : Terraform
- Monitor : Prometheus / Grafana
- CD : ArgoCD

# Part 2 - How to Set Up our enviroment.

How to host our Virtual Machines:
- Azure Virtual Machines
- AWS EC2
- Github Codespace <-- We are gonna use this

- We are gonna create a Codespace and connect to our project.
- Inside our codespace, we are gonna install the tools below:
    - Docker
    - Git
    - Kubectl
    - Helm
    - python (+3.12)
    - pip
    - aws cli
    - terraform

- If they are already installed, just check the version.

# Parte 3 - 

# Part 4 - Containerization with Docker

What do we need?
- Code
- Requirements.txt  
- DockerFile (Manual to build our image)

Docker commands
- docker build -t hello-world . 
- docker run -p 8000:5000 --name hello-world-container hello-world
- 8000 is local portal and 5000 is container port.

# Part 5 - Push Image to DockerHub

1. Create Account
2. Create repo in DockerHub
    - vitormilam/hello-world
    - Image name has to be equal to the name in dockerhub.
    - So, our image name should be vitormilam/hello-world, not only hello-world.
3. Create PAT (Personal Access Token) for login
    - Account Settings -> Personal Access Tokens. -> Generate New Token.
4. Login in the terminal
5. Image with same repo name
    - To change the docker image name, use this command: docker tag hello-world vitormilam/hello-world
6. Docker push
    - docker push vitormilam/hello-world:latest

# Part 6 - CI with GitHub Actions

- I had to create this structure: .github / workflows / ci.yaml (code for building and pushing docker images automatizally using GitHub Actions).
- Also, i had to create a PAT (Personal Access Token) only for this and add in the code.
- Since our username and password aren't in the code because of security, it won't run in Actions tab.
- We should do this using the safer version.
- Go to github repository settings -> Secrets and Variables -> Actions -> New repository secret.
- We have to type exactly we typed in the code:
    NAME: DOCKERHUB_USERNAME / SECRET: USERNAME
    NAME: DOCKERHUB_TOKEN / SECRET: PASSWORD

- Now the code should work in the Actions Tab.

# Part 7 - Terraform to create Kubernetes on AWS

- To do this, we need Terraform and aws cli installed in our VM/machine.
- For this project i have created a IAM user.
- After creating the user, i have created a access key so we can configure our AWS CLI.

Commands:
- aws configure

- In this project, we are gonna use Terraform EKS module that is available for free in Terraform website.
- We are gonna use EKS Managed Groud code.
- Bu first, to create a EKS, we a need a VPC. EKS goes inside a VPC.

- Search terms: terraform module EKS
- Search terms: terraform module VPC

Commands:
- terraform init = Initialize terraform.
- terraform plan = It gives a list of resources that it will create for us.
- terraform apply -auto-approved = 

- After this, it will take while to set up EKS, for example, between 15 and 20 minutes.
- To check if it worked, you can to your aws account and open EKS, in Clusters tab.

- Now that we have created our Cluster, we have to initialize it.

Commands:
- aws eks update-kubeconfig --name my-cluster
- kubectl get nodes
- If we want to destroy our cluster, run terraform destroy -y


# Part 8 - Deploy Application in EKS

- We created a image that when executed it becomes a container.
- We will wrap this container inside a pod, the smallest object in kubernetes.
- After this is done, we will have 3 pods and we will use a Replica Set because if one pod or more fail, another will be created imediatly to replace it.
- All this we will wrap up again and call this a DEPLOYMENT.
- IMAGE -> CONTAINER -> POD -> DEPLOYMENT 

- To create any resources in Kubernetes, we use a YAML cofniguration file.
- So we create a deployment.yaml file to create all this things above (container, pods, replica set, deployment).

Commands:
- kubectl apply -f ./deployment.yaml
- kubectl get all
- kubectl port-forward svc/hello-world-service 8080:(hello-world-service port)


# Part 9 - Observability: Prometheus & Grafana

- Basically Prometheus get the metrics of Application/EKS.

But how do we install Prometheus ?
- We use Helm to install Prometheus.
- It's a packet manager for kubernetes, like PIP for python.
- So HELM is a packet manager that we use to install 3rd party software inside Kubernetes

So we run this commands in our command line:
- helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
- heml repo update
- helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring --create-namespace

After creating, we can through if it worked:
- kubectl get ns
- kubectl get all -n monitoring

- After does this, can we track our metrics with Prometheus ?
R: No, first we need to have a endpoint, like /endpoint Since we don't have it, we need to create it.

So we need to install some libraries, in requirements.txt, we need to paste it:
- prometheus-client==0.21.0
- prometheus-flask-exporter==0.23.2

So, our requirements.txt will look like this:
flask
prometheus-client==0.21.0
prometheus-flask-exporter==0.23.2

After this, we go to app.py so we can call the libraries and create our endpoint:
- from prometheus_flask_exporter import PrometheusMetrics
- metrics = PrometheusMetrics(app)  # <-- enables / metrics

So, our app.py will look like this:


## Importing flask & Prometheus 
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # <-- enables / metrics

CODE:
## Endpoint
@app.route("/")
def hello():
    return "Hello World"

@app.route("/new")
def new():
    return "It's a new world, a new day."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


Run commands:
- kubectl get svc
- kubectl port-forward svc/hello-world-service 8000:80


- Now we need to tell prometheus which port it has to go so it can collect the metrics.
- For this, we need to create servicemonitor.yaml with the right configuration and labels that match our service configuration in deployment.yaml

Commands:
- kubectl apply -f ./servicemonitor.yaml
- kubectl get all -n monitoring

- To see prometheus URL, we connect to service/prometheus-kube-prometheus-prometheus port
- kubectl port-forward -n monitoring svc/prometheus-kube-prometheus-prometheu port:port

To see this metric in nice dashboard, we need grafana.
Grafana is a dashboard tool and we can have the source as Prometheus to see Prometheus matrics.
When we installed prometheus, grafana already came pre-installed, you can see these in services, like, service/prometheus-grafana 
When we ran:
- helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
- heml repo update
- helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring --create-namespace

At the beginning, you can see: 
Get Grafana admin user password by running:
    kubectl get secret --namespace monitoring get secrets prometheus-grafana -0 jsonpath="{.items[0].data.admin-password}" base64 --decode ; echo

Now we can exexute the command above to get the password.

Now we run again command:
kubectl port-forward -n monitoring svc/prometheus-grafana port:port

- After this, it will forward to Grafana and ask for the username and password that we talked above.
    - username: admin
    - password: 

In Grafana, go to Dashboards, clink in the arrow besides the + symbol -> Import Dashboard 
- In Find and import dashboards for common applications at grafana.com/dashboards, we can fill with code 3662 and press Load.
(This code represents a specific dashboard that grafana provides on their own website)
- In prometheus sections, click on it and select the default one and click on Import.


# Part 10 - CD with ArgoCD and Extending the CI for further automation
