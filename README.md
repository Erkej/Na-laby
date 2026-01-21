# Na-laby

Repozytorium zawierające projekt **ROS 2** w Pythonie, przygotowany na potrzeby zajęć laboratoryjnych.  
Projekt oparty jest o pakiet `projetk_ros`, który demonstruje podstawowe mechanizmy działania ROS 2.

---

## 📌 Opis projektu

Projekt stanowi workspace ROS 2 zawierający pakiet napisany w Pythonie (`rclpy`).  
Celem projektu jest zapoznanie się z podstawami systemu ROS 2, w szczególności:
- tworzeniem węzłów (nodes),
- publikowaniem i subskrybowaniem wiadomości,
- komunikacją poprzez topiki,
- uruchamianiem aplikacji ROS 2 z poziomu terminala.

---

## ▶️ Uruchomienie paczki
Uruchomienie paczki następuje automatycznie za pomocą dockerfile'a. Wystarczy jedynie wpisać komendę:
docker run -it --rm --net=host --privileged --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" -v "$(pwd):/src" camera_subscriber bash

---

## 📁 Struktura repozytorium

