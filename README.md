What we will learn:

- Version Control
- Containers
- CI - Automation: Github Actions
- IaC : Terraform
- Monitor : Prometheus / Grafana
- CD : ArgoCD

How to host our Virtual Machines:
- AWS EC2
- Github Codespace

We need to install
- Docker
- Git
- Kubectl
- Helm
- python
- pip
- aws cli
- terraform

# Part 4 - Containerization with Docker

What do we need?
- Code
- Requirements.txt  
- DockerFile (Manual to build our image)

Docker commands
- docker build -t hello-world . 
- docker run -p 8000:5000 --name hello-world-container hello-world
- 8000 is local portal and 5000 is container port.