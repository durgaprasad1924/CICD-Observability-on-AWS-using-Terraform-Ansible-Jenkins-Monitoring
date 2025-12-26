FROM python:3.9-slim
WORKDIR /app
COPY /home/ec2-user/CICD-Observability-on-AWS-using-Terraform-Ansible-Jenkins-Monitoring/app/app.py .
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]

