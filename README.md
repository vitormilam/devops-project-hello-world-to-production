# 🚀 The Simplest End-to-End DevOps Project | Hello World to Production

This project demonstrates a simple **end-to-end DevOps workflow**, starting with a basic Python application and progressing through containers, CI, Infrastructure as Code, Kubernetes, monitoring, and Continuous Deployment.

The main goal of this project is to understand how an application can go from **local source code to a deployed and observable application**.

Some of the main technologies used in this project are:

* Git & GitHub
* Python & Flask
* Docker
* DockerHub
* GitHub Actions
* Terraform
* Kubernetes
* Amazon EKS
* Helm
* Prometheus
* Grafana
* ArgoCD

---

# Part 1 - What We Will Learn

Throughout this project, we will learn about several important DevOps concepts.

### Version Control

We use **Git and GitHub** to store and manage our source code.

Version control allows us to track changes made to the project and keep our code organized.

### Containers

We use **Docker** to package our Flask application and its dependencies into a container.

This allows the application to run in a consistent environment.

### Continuous Integration (CI)

We use **GitHub Actions** to automate the process of building our Docker image and pushing it to DockerHub.

### Infrastructure as Code (IaC)

We use **Terraform** to create our infrastructure on AWS.

In this project, Terraform is used to create the VPC and the Amazon EKS cluster.

### Monitoring

We use **Prometheus and Grafana** to collect and visualize metrics from our application and Kubernetes environment.

### Continuous Deployment (CD)

We use **ArgoCD** to implement a GitOps-style deployment process.

---

# Part 2 - How to Set Up Our Environment

Before starting the project, we need an environment where we can execute our commands and install the necessary tools.

## Where Can We Host Our Virtual Machines?

Some possible options are:

* Azure Virtual Machines
* AWS EC2
* GitHub Codespaces

For this project, **we are going to use GitHub Codespaces**.

We will create a Codespace and connect it to our project repository.

Inside the Codespace, we need the following tools:

* Docker
* Git
* Kubectl
* Helm
* Python (+3.12)
* pip
* AWS CLI
* Terraform

If a tool is already installed, we can simply check its version instead of installing it again.

For example:

```bash
docker --version
git --version
kubectl version --client
helm version
python --version
pip --version
aws --version
terraform --version
```

---

# Part 3 - Our Application: A Simple Hello World Using Flask

For this project, we start with a very simple Python application using **Flask**.

Flask is a Python framework that allows us to create web applications and HTTP endpoints.

Our application will have two endpoints:

```text
/
```

and

```text
/new
```

The first endpoint returns:

```text
Hello World
```

The second endpoint returns:

```text
It's a new world, a new day.
```

At this stage, the application is very simple.

The important part is not the complexity of the application itself, but what we will do with it throughout the project.

We will take this simple Flask application and progressively:

```text
Python Application
        ↓
Docker Container
        ↓
DockerHub
        ↓
GitHub Actions
        ↓
Amazon EKS
        ↓
Prometheus
        ↓
Grafana
        ↓
ArgoCD
```

This allows us to understand how different DevOps tools work together in a complete workflow.

Our application will eventually also expose a `/metrics` endpoint so that Prometheus can collect metrics from it.

---

# Part 4 - Containerization with Docker

Now that we have our Flask application, we need to package it into a Docker image.

## What Do We Need?

To create our Docker image, we need:

* Application code
* `requirements.txt`
* `Dockerfile`

The `requirements.txt` file contains the Python dependencies required by our application.

The `Dockerfile` contains the instructions Docker uses to build our image.

## Build the Docker Image

We can build our image using:

```bash
docker build -t hello-world .
```

The `-t` option allows us to give our image a name.

In this case:

```text
hello-world
```

## Run the Container

After building the image, we can run it with:

```bash
docker run -p 8000:5000 --name hello-world-container hello-world
```

The port configuration is:

```text
8000:5000
```

The first port is the **local port**:

```text
8000
```

The second port is the **container port**:

```text
5000
```

Our Flask application runs on port `5000` inside the container.

Docker maps that port to port `8000` on our local environment.

---

# Part 5 - Push Image to DockerHub

After creating our Docker image, we can push it to DockerHub.

## 1. Create a DockerHub Account

First, we need to create an account on DockerHub.

## 2. Create a Repository

Create a repository with the following name:

```text
vitormilam/hello-world
```

Our Docker image needs to use the same repository name.

Instead of:

```text
hello-world
```

we will use:

```text
vitormilam/hello-world
```

## 3. Create a Personal Access Token

For authentication, we create a **PAT (Personal Access Token)**.

Go to:

```text
Account Settings
→ Personal Access Tokens
→ Generate New Token
```

The token can then be used to authenticate with DockerHub.

## 4. Login Through the Terminal

We can log in to DockerHub through the terminal.

## 5. Tag the Docker Image

Our original image is:

```text
hello-world
```

We can change its name/tag with:

```bash
docker tag hello-world vitormilam/hello-world
```

Now the image has the same repository name as our DockerHub repository.

## 6. Push the Image

Finally, we can push the image to DockerHub:

```bash
docker push vitormilam/hello-world:latest
```

The image is now available in our DockerHub repository.

---

# Part 6 - Continuous Integration (CI) with GitHub Actions

The next step is to automate the process of building and pushing our Docker image.

For this, we use **GitHub Actions**.

We created the following structure:

```text
.github/
└── workflows/
    └── ci.yaml
```

The `ci.yaml` file contains the workflow responsible for building and pushing our Docker image automatically.

Initially, we used a username and password/PAT directly in the workflow.

However, this is not a safe approach because credentials should not be exposed directly in the code.

## Using GitHub Secrets

Instead, we store our credentials using **GitHub repository secrets**.

Go to:

```text
GitHub Repository
→ Settings
→ Secrets and Variables
→ Actions
→ New repository secret
```

We create the following secrets:

```text
NAME: DOCKERHUB_USERNAME
SECRET: USERNAME
```

and:

```text
NAME: DOCKERHUB_TOKEN
SECRET: PASSWORD
```

The names must match the names used inside our GitHub Actions workflow.

After creating the secrets, GitHub Actions can use them without exposing our credentials directly in the code.

We can then check the workflow execution in the:

```text
Actions
```

tab of our GitHub repository.

---

# Part 7 - Terraform to Create Kubernetes on AWS

Now we are going to create our Kubernetes infrastructure on AWS.

For this part, we need:

* Terraform
* AWS CLI
* An AWS account

## AWS CLI Configuration

For this project, I created an **IAM user**.

After creating the user, I created an **access key** so that we could configure the AWS CLI.

We configure the AWS CLI with:

```bash
aws configure
```

## Terraform EKS Module

Instead of manually creating all the AWS resources, we use Terraform modules.

We use the Terraform EKS module available through the Terraform Registry.

Search terms:

```text
terraform module EKS
```

and:

```text
terraform module VPC
```

### Why Do We Need a VPC?

Before creating an EKS cluster, we need a VPC.

Amazon EKS runs inside a VPC.

In this project, Terraform creates our VPC and then uses it for our EKS cluster.

The VPC contains:

```text
VPC
├── Public Subnets
└── Private Subnets
```

The EKS cluster uses the private subnets.

## Terraform Commands

First, initialize Terraform:

```bash
terraform init
```

This initializes the Terraform project and downloads the required providers and modules.

Next, we can see what Terraform plans to create:

```bash
terraform plan
```

After reviewing the plan, we can create the infrastructure:

```bash
terraform apply -auto-approve
```

The creation of the EKS cluster can take some time.

For example, in this project it can take approximately:

```text
15–20 minutes
```

After Terraform finishes, we can check our AWS account.

Open:

```text
AWS Console
→ EKS
→ Clusters
```

Our cluster should appear there.

## Connect kubectl to the EKS Cluster

After creating the cluster, we need to configure `kubectl` to communicate with it.

Run:

```bash
aws eks update-kubeconfig --name my-cluster
```

We can then check the nodes:

```bash
kubectl get nodes
```

If the cluster is no longer needed, we can destroy the infrastructure with:

```bash
terraform destroy -y
```

---

# Part 8 - Deploy Application in EKS

Now that our Kubernetes cluster exists, we can deploy our application.

We already created a Docker image containing our Flask application.

The basic relationship is:

```text
IMAGE
   ↓
CONTAINER
   ↓
POD
   ↓
REPLICASET
   ↓
DEPLOYMENT
```

## What Is a Pod?

A **Pod** is the smallest deployable object in Kubernetes.

Our Docker container runs inside a Pod.

In this project, we configure:

```text
replicas: 2
```

This means Kubernetes will maintain two Pods for our application.

A **ReplicaSet** is responsible for maintaining the desired number of Pods.

If a Pod fails, Kubernetes can create another Pod to replace it.

A **Deployment** manages the application and its ReplicaSet.

## Kubernetes YAML

To create Kubernetes resources, we use YAML configuration files.

For this project, we create:

```text
deployment.yaml
```

The file defines our Deployment, including:

* Number of replicas
* Container
* Docker image
* Container port
* Labels
* Pod configuration

We apply the configuration using:

```bash
kubectl apply -f ./deployment.yaml
```

We can then check the Kubernetes resources with:

```bash
kubectl get all
```

## Kubernetes Service

We also create a Kubernetes Service for our application.

The Service allows us to access the Pods through a stable network endpoint.

Our Service uses:

```text
port: 80
targetPort: 5000
```

This means that the Service receives traffic on port `80` and forwards it to port `5000` inside the application container.

We can access the Service locally using port forwarding:

```bash
kubectl port-forward svc/hello-world-service 8080:80
```

---

# Part 9 - Observability: Prometheus & Grafana

Our application is now running inside Kubernetes.

The next step is to monitor it.

For this project, we use:

* Prometheus
* Grafana

## What Is Prometheus?

**Prometheus** collects metrics from applications and infrastructure.

In our project, Prometheus will collect metrics from our application and Kubernetes environment.

But before Prometheus can collect application metrics, our Flask application needs to expose a metrics endpoint.

---

## Installing Prometheus with Helm

We use **Helm** to install Prometheus.

Helm is a package manager for Kubernetes.

It is similar to how `pip` is used as a package manager for Python.

Therefore:

```text
pip
↓
Python packages

Helm
↓
Kubernetes software/packages
```

We add the Prometheus Community repository:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
```

Then update the repository:

```bash
helm repo update
```

Finally, install the Prometheus stack:

```bash
helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring --create-namespace
```

The installation creates a Kubernetes namespace called:

```text
monitoring
```

We can check if it was created:

```bash
kubectl get ns
```

And check the resources inside it:

```bash
kubectl get all -n monitoring
```

---

## Add Metrics to Our Flask Application

Can Prometheus track our application immediately?

**No.**

Our application needs to expose an endpoint containing metrics.

For this, we add two libraries to `requirements.txt`:

```text
prometheus-client==0.21.0
prometheus-flask-exporter==0.23.2
```

Our complete `requirements.txt` becomes:

```text
flask
prometheus-client==0.21.0
prometheus-flask-exporter==0.23.2
```

Then we modify `app.py`.

We import:

```python
from prometheus_flask_exporter import PrometheusMetrics
```

and initialize the metrics:

```python
metrics = PrometheusMetrics(app)
```

This enables the:

```text
/metrics
```

endpoint.

Our application contains:

```python
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/new")
def new():
    return "It's a new world, a new day."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

Now our application exposes:

```text
/
```

```text
/new
```

and:

```text
/metrics
```

---


## Configure Prometheus with ServiceMonitor

Now we need to tell Prometheus where it should collect our application metrics.

For this, we create:

```text
servicemonitor.yaml
```

The ServiceMonitor contains the configuration required for Prometheus to find our application Service and collect metrics from:

```text
/metrics
```

The ServiceMonitor also uses labels that match the Prometheus configuration.

We apply it with:

```bash
kubectl apply -f ./servicemonitor.yaml
```

We can check the resources in the monitoring namespace:

```bash
kubectl get all -n monitoring
```

---

## Access Prometheus

Prometheus is available through its Kubernetes Service.

We can use port forwarding:

```bash
kubectl port-forward -n monitoring svc/prometheus-kube-prometheus-prometheus 9090:9090
```

This allows us to access the Prometheus interface locally.

---

# Grafana

Prometheus allows us to collect metrics, but we can use **Grafana** to visualize those metrics in dashboards.

Grafana is a dashboard and visualization tool.

When we installed:

```bash
helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring --create-namespace
```

Grafana was also installed as part of the stack.

We can find it among the Kubernetes Services:

```text
service/prometheus-grafana
```

## Get the Grafana Password

During the installation, the command provided to retrieve the Grafana administrator password is:

```bash
kubectl get secret --namespace monitoring get secrets prometheus-grafana -o jsonpath="{.items[0].data.admin-password}" | base64 --decode ; echo
```

The username is:

```text
admin
```

The password is the value returned by the command above.

## Access Grafana

We can forward the Grafana Service to our local environment:

```bash
kubectl port-forward -n monitoring svc/prometheus-grafana <port>:<port>
```

After accessing Grafana, we log in using:

```text
Username: admin
Password: <password retrieved from Kubernetes>
```

## Import a Grafana Dashboard

After logging in:

```text
Dashboards
→ Arrow beside the + symbol
→ Import Dashboard
```

In:

```text
Find and import dashboards for common applications at grafana.com/dashboards
```

we can enter:

```text
3662
```

and click:

```text
Load
```

This code represents a dashboard provided by Grafana.

In the Prometheus section, select the default Prometheus data source and click:

```text
Import
```

We can now use Grafana to visualize the metrics collected by Prometheus.

---

# Part 10 - CD with ArgoCD and Extending the CI for Further Automation

ArgoCD tracks only the changes in the YAML files and changes the production accordingly.

- Through their website, we can get the command to install ArgoCD through the command line.

Which is:
kubectl create namespace argocd
kubectl apply -n argocd --server-side --force-conflicts -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

After installing, how do we expose it ArgoCD UI?
- Through service/argocd-server
- ArgoCD doesn't work with ClusterIP.
- In a production enviroment, we use a Load Balancer so that's what we will use.

Command to fix this:
- kubectl patch svc argocd-server -n argocd -p '{"spec":{"type":"LoadBalancer"}}'

If you use this command now, you can that it's working:
- kubectl get svc -n argocd

Once we login through the EXTERNAL-IP provided, we login.
- The user name is admin.

To find out the password, you use:
- kubectl get secret -n argocd
- kubectl get secret -n argocd argocd-initial-admin-secret -o yaml

The password is coded.

- echo "password" | base64 -d

New we have to create application:
-> Create Application
- Application name: Demo
- Project Name: default
- Sync Policy: Automatic
- Enable auto-sync, prune resources and self heal.
- Repository URL: Your repo link
- Revision: main
- Path: .

Destination:
- Cluster URL: Just select whatever it appears.
- Namespace: default

Click in Create