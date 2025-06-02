
````markdown
# 🙏 Tribute App – Flask Web Assignment

This is a heartfelt web application developed using **Python Flask** to pay tribute to Ashish Sir and Aman Sir for their guidance, mentorship, and incredible support.

Unlike our previous assignments involving `HTML` and `Nginx`, this task involves building and running a **Flask-based Python web app** locally and on a **Linux VM hosted in Azure**.

---

## 🛠️ Project Setup Instructions

### ✅ Clone the Repository

```bash
git clone https://github.com/narottam-kumar/narottam-infra-001.git
cd narottam-infra-001
````

---

## 🧪 Run the App Locally on Windows

### 1️⃣ Install Python (if not installed)

Download and install Python from:
🔗 [https://www.python.org/downloads/](https://www.python.org/downloads/)

Ensure Python and pip are added to the system PATH.

### 2️⃣ Install Flask

Open Command Prompt or PowerShell and run:

```bash
pip install flask
```

### 3️⃣ Run the Flask App

```bash
python Tribute.py
```

The app will start running at:
📍 `http://localhost:5000`
Open this URL in your browser to view the tribute.

---

## ☁️ Deploy to Azure Linux VM

### 1️⃣ Create a Linux VM on Azure

* Use Ubuntu.
* Allow **port 5000** in Network Security Group (NSG) during creation.

### 2️⃣ SSH into Your VM

```bash
ssh <your-username>@<your-vm-public-ip>
```

### 3️⃣ Install Python, pip, Flask on VM

```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install flask
```

### 4️⃣ Transfer the Flask App to the VM

From your local machine, use `scp`:

```bash
scp Tribute.py <your-username>@<your-vm-public-ip>:~/
```

Or to copy the whole repo:

```bash
scp -r ./narottam-infra-001 <your-username>@<your-vm-public-ip>:~/
```

### 5️⃣ Run the Flask App on the VM

```bash
python3 Tribute.py
```

The app will be available at:
📍 `http://<your-vm-public-ip>:5000`

### 6️⃣ Access from Browser

Open the URL in your browser using the public IP of the VM.

---

## 🐳 Docker – Containerize and Run the Tribute App

This section guides you through containerizing the Flask app using Docker, running it locally, and deploying it on your Azure Linux VM.

### 1️⃣ Install Docker

* **Windows:**
  Download Docker Desktop from [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop) and install.

* **Azure Linux VM:**
  SSH into your VM and run:

```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
```

*Optional:* Add your user to the docker group to run docker without `sudo`:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

---

### 2️⃣ Create a Dockerfile

In your project directory (`narottam-infra-001`), create a file named `Dockerfile` with the following content:

```dockerfile
# Use official Python runtime as a parent image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install --no-cache-dir flask

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set environment variable for Flask app
ENV FLASK_APP=Tribute.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
```

---

### 3️⃣ Build the Docker Image (Locally)

In your terminal or PowerShell, inside your project folder, run:

```bash
docker build -t tribute-app .
```

This will build the Docker image and tag it as `tribute-app`.

---

### 4️⃣ Run the Docker Container (Locally)

Run the container and map port 5000 of the container to port 5000 on your local machine:

```bash
docker run -d -p 5000:5000 tribute-app
```

Now open your browser and navigate to:

```
http://localhost:5000
```

You should see the tribute app running inside the Docker container.

---

### 5️⃣ Push Docker Image to Docker Hub (Optional)

If you want to run the app via Docker on Azure VM without transferring files, push your image to Docker Hub:

* Log in to Docker Hub:

```bash
docker login
```

* Tag your image with your Docker Hub username:

```bash
docker tag tribute-app yourdockerhubusername/tribute-app:latest
```

* Push the image:

```bash
docker push yourdockerhubusername/tribute-app:latest
```

---

### 6️⃣ Run Docker Container on Azure Linux VM

#### Option A: Pull from Docker Hub

On your Azure VM, pull the image:

```bash
docker pull yourdockerhubusername/tribute-app:latest
```

Run the container:

```bash
docker run -d -p 5000:5000 yourdockerhubusername/tribute-app:latest
```

#### Option B: Build Directly on VM

Transfer your project files (including the Dockerfile) to your VM using `scp`:

```bash
scp -r ./narottam-infra-001 <your-username>@<your-vm-public-ip>:~/
```

SSH into VM and build:

```bash
cd narottam-infra-001
docker build -t tribute-app .
docker run -d -p 5000:5000 tribute-app
```

---

### 7️⃣ Access the App on Azure VM

Open a browser and navigate to:

```
http://<your-vm-public-ip>:5000
```

You should see the tribute app running inside Docker on your Azure VM.

---

## ✅ Notes

* Make sure port `5000` is open in both:

  * Azure NSG (firewall)
  * Local VM firewall (`sudo ufw allow 5000` if UFW is enabled)
* To stop the Docker container, use:

```bash
docker ps
docker stop <container_id>
```

* To keep the container running after logout, consider running it with `-d` (detached mode) as shown above.

---

## 📦 Files in This Project

* `Tribute.py` – Main Python Flask app.
* `Dockerfile` – Docker configuration for containerizing the app.
* `README.md` – Step-by-step guide.
* HTML embedded inside the Python file using `render_template_string`.

---

## ❤️ Dedication

This app is a tribute with love and gratitude to
**Ashish Sir** & **Aman Sir** — our mentors, guides, and true inspirations. 🙏

---


🐳 Docker – Containerize and Run the Tribute App
This section guides you through containerizing the Flask app using Docker, running it locally, and deploying it on your Azure Linux VM.

1️⃣ Install Docker
Windows:
Download Docker Desktop from https://www.docker.com/products/docker-desktop and install.

Azure Linux VM:
SSH into your VM and run:

bash
Copy
Edit
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
Optional: Add your user to the docker group to run docker without sudo:

bash
Copy
Edit
sudo usermod -aG docker $USER
newgrp docker
2️⃣ Create a Dockerfile
In your project directory (narottam-infra-001), create a file named Dockerfile with the following content:

dockerfile
Copy
Edit
# Use official Python runtime as a parent image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install --no-cache-dir flask

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set environment variable for Flask app
ENV FLASK_APP=Tribute.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
3️⃣ Build the Docker Image (Locally)
In your terminal or PowerShell, inside your project folder, run:

bash
Copy
Edit
docker build -t tribute-app .
This will build the Docker image and tag it as tribute-app.

4️⃣ Run the Docker Container (Locally)
Run the container and map port 5000 of the container to port 5000 on your local machine:

bash
Copy
Edit
docker run -d -p 5000:5000 tribute-app
Now open your browser and navigate to:

arduino
Copy
Edit
http://localhost:5000
You should see the tribute app running inside the Docker container.


> Let’s keep the spirit alive – with unity, respect, and growth 🚀
> – Narottam (B17)

```
