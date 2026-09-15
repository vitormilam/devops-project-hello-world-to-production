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