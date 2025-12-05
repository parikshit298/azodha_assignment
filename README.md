# azodha_assignment
This repository is created for python application assignment.
<img width="788" height="755" alt="image" src="https://github.com/user-attachments/assets/1f3a1508-e15b-419b-9232-61608d032ff5" />

User → ALB/Ingress: External traffic hits an Application Load Balancer (or Ingress controller in EKS). ALB terminates TLS and forwards to the Kubernetes Service.

Service → Deployment: Kubernetes Service routes traffic to Pods of deployment myapp. Pods run the container parikshit298/azodha:latest.

Jenkins (CI/CD): Pulls repo from GitHub, builds Docker image, pushes to Docker Hub, then runs kubectl set image deployment/myapp myapp=... (or kubectl rollout restart) to trigger rolling update.

CloudWatch:

Node metrics: CloudWatch Agent or CloudWatch EC2 integration collects CPU, memory, disk, network for EC2 worker nodes.


Credentials:

Jenkins needs Docker Hub credentials (username/password) to push images.

Jenkins needs kubeconfig or IAM-authenticated access to update EKS deployment.

Kubernetes nodes should have IAM role for CloudWatch metrics/log push (if using AWS integrations).
