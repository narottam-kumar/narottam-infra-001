# narottam-infra-001

I can't directly provide file downloads, but I can show you how to save the `README.md` file on your local system.

### 📥 To Save the README.md File

#### ✅ Option 1: Manually Create the File

1. Open a text editor like **Notepad**, **VS Code**, or **Notepad++**.
2. Copy the content below.
3. Save the file as `README.md` in your project folder.

---

**📄 Copy and paste this:**

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
python app.py
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
scp app.py <your-username>@<your-vm-public-ip>:~/
```

Or to copy the whole repo:

```bash
scp -r ./narottam-infra-001 <your-username>@<your-vm-public-ip>:~/
```

### 5️⃣ Run the Flask App on the VM

```bash
python3 app.py
```

The app will be available at:
📍 `http://<your-vm-public-ip>:5000`

### 6️⃣ Access from Browser

Open the URL in your browser using the public IP of the VM.

---

## ✅ Notes

* Make sure port `5000` is open in both:

  * Azure NSG (firewall)
  * Any local VM firewall (use `sudo ufw allow 5000` if UFW is enabled)

* To keep the app running after logout, use:

  * `screen` or `tmux`
  * Or consider using a process manager like `nohup` or `pm2`

---

## 📦 Files in This Project

* `app.py` – Main Python Flask app.
* `README.md` – Step-by-step guide.
* HTML is embedded directly inside the Python file using `render_template_string`.

---

## ❤️ Dedication

This app is a tribute with love and gratitude to
**Ashish Sir** & **Aman Sir** — our mentors, guides, and true inspirations. 🙏

---

> Let’s keep the spirit alive – with unity, respect, and growth 🚀
> – Team B17

```

---

Let me know if you'd like a downloadable `.zip` version with this README included.
```
