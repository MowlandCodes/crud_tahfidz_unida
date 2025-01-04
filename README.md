<html>
<h1 style="text-align: center;">🕌 Tahfidz Dashboard System 🕌</h1>

## Tech Stack
[![Static Badge](https://img.shields.io/badge/django-framework-green?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com) [![Static Badge](https://img.shields.io/badge/python-language-yellow?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
---


Project ini saya buat secara sederhana untuk memudahkan user terkhusus Mahasiswa dalam mengelola data tahfidz. Saya memilih menggunakan Django sebagai framework karena memungkinkan saya untuk mengelola data dengan mudah dan cepat.

<br>

## Requirements 📃

Sebelum menggunakan aplikasi ini, pastikan anda telah menginstall dan memasukkan semua requirements, atau kalian bisa menggunakan perintah berikut ini:

#### Linux (Ubuntu)

```bash
sudo apt update && sudo apt upgrade -y && sudo apt install python3 python3-pip -y && pip3 install -r requirements.txt
```

#### Windows

Untuk pengguna Windows, diharapkan untuk menginstall [Python](https://python.org/downloads) , pip dan Git di komputer Anda terlebih dahulu. Pastikan untuk menggunakan Python 3.9 atau versi terbaru. Setelah menginstall, Anda dapat menjalankan perintah berikut:

```powershell
winget install --id Git.Git -e --source winget # Untuk menginstall Git

python --version # Untuk mengecek versi Python

pip install -r requirements.txt # Untuk menginstall semua requirements
```

#### Pre-deploy
Jika anda ingin melakukan deploy pada local environment, pastikan untuk melakukan perintah berikut ini:
```bash
# Pengguna Windows
python manage.py makemigrations
python manage.py migrate

# Pengguna Linux
python3 manage.py makemigrations
python3 manage.py migrate
```
<br>

## Local Deployment 🚀
Untuk melakukan deploy pada local environment, anda dapat menjalankan perintah berikut:

```bash
python manage.py runserver # untuk windows

python3 manage.py runserver # untuk linux
```

> NB : Jika terdapat masalah pada saat deploy, pastikan untuk menjalankan perintah diatas terlebih dahulu.


## Social Media 🌐
Kalian Bisa mengakses saya melalui beberapa media sosial berikut: <br><br>
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/mowland__) [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=inspire&logoColor=white)](https://linkedin.com/in/m-faridh-maulana-a3532a287) [![Medium](https://img.shields.io/badge/Medium-12100E?logo=medium&logoColor=white)](https://medium.com/@mowland-codes) 

</html>
