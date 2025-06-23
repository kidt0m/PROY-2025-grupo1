 c # PROY-2025-GRUPO1
Video del mikumpanion: https://youtu.be/bkeT-Qbxxj0
Repositorio del grupo 1 para el proyecto del ramo *Proyecto Inicial* – 2025.

## 👥 Integrantes del grupo

| Nombre y Apellido | Usuario GitHub     | Correo USM               | Rol          |
| ----------------- | --------------     | ------------------------ | ------------ |
| Thomas Filippi    | @kidt0m            | tfilippi@usm.cl          | 202530027-3  |
| Tomás Riquelme    | @Tomi3005          | triquelme@usm.cl         | 202530034-6  |
| Vicente Salgado   | @whodatboin        | vsalgadof@usm.cl         | 202530022-2  |
| Valentina Agüero  | @valechiquita      | vaguero@usm.cl           | 202430031-8  |
| Josué Rojas       | @jjxdress          | jrojasgo@usm.cl          | 202530028-1  |


## 📝 Descripción breve del proyecto

 Mikumpanion es una asistente virtual con text-to-speech, speech-to-text (para hablarle) y capacidades QOL secundarias

---

## 🎯 Objetivos

- Objetivo general:
  - *Crear un asistente virtual que sea capaz de hablar y escuchar.*
- Objetivos específicos:
  - *Integrar Speech-to-text para inputear texto via mic al chatbot* 
  - *Integrar Text-to-speech para darle voz al Mikumpanion*
  - *Darle acceso a internet al chatbot*
  - *Añadir salida y entrada de audio*
  - *Añadir botones al diseño final para manejo simple*
  - *Integrar Calendario y reloj*
  - *Crear una interfaz visual medio decente*
---

## 🧩 Alcance del proyecto

> Contestar preguntas simples, y resolver problemas matemáticos con voz de Miku.

---

## 🛠️ Tecnologías y herramientas utilizadas

- Lenguaje(s) de programación:
  - Micro python
  - python 1.11
- Microcontroladores
  - Raspberry Pi Pico W 2
- Sensores
  - Botón (pulsador)
  - Microfono (PC)
- Actuadores
  - Pantalla OLED 9E6045A0
  - Parlante (bluetooth)
- Librerías
  - utime
  - json
  - network
  - urequests
  - framebuf
  - ssd1306 (SSD1306_I2C)
  - machine
  - whisper
  - sounddevice
  - numpy
  - scipy
  - requests
  - TTS
  - soundfile

## 🗂️ Estructura del repositorio

```
/PROY-2025-GRUPOX
│
├── docs/               # Documentación general y reportes
├── src/                # Código fuente del proyecto
├── tests/              # Casos de prueba
├── assets/             # Imágenes, diagramas, etc.
└── README.md           # Este archivo
```

---

## INSTRUCCIONES DE USO!!

DESDE EL PC (EJECUCION CORRECTA DE PROGRAMAS PERTINENTES)

Descargar aplicaciones necesarias
Python 3.11 (IMPORTANTISIMO QUE SEA 3.11 PARA EVITAR PROBLEMAS DE COMPATIBILIDAD)
Oogabooga (O Text-generation-webui) https://github.com/oobabooga/text-generation-webui/releases
RVC WEB-UI https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI

Descargar archivos para que las aplicaciones descargadas funcionen

Oogabooga - Oogabooga necesita un LLM para poder generar respuestas, el LLM es a eleccion, pero durante el desarrollo se usó mistral 7b-instruct (Descargable aqui: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)
Poner el LLM descargado en text-generation-webui-main\user_data\models

RVC WEB-UI - Para hacer funcionar el RVC necesitas un voicemodel .pth y .index, nosotros usamos un voicemodel de Hatsune Miku descargado desde weights.com (descargable aqui https://www.weights.com/es/models/clwyirbzw007z10ujjnx3g8ff)

El .rar vendra con 2 archivos, poner el .pth en RVC1006Nvidia\assets\weights y el .index en RVC1006Nvidia\logs

En la carpeta de Oogabooga y RVC WEB-UI ejecutar ''pip install -r requirements.txt'' para descargar las librerias correspondientes, Luego ejecutar ''pip install openai-whisper sounddevice numpy scipy requests TTS soundfile'' para descargar librerias necesarias para el pipeline

Una vez tenemos todo instalado, ejecutar oogabooga con --api --listen y aplicar el LLM que descargaste, una vez tenemos oogabooga funcionando, ejecutar RVC-WEBUI.

Cuando tenemos ambos procesos abiertos, ejecutar pipeline.py para ejecutar la pipeline Whisper -> Oogabooga -> coquiTTS -> RVC

enjoy!


DESDE LA RASPBERRY

Descargar los archivos en src y subirlos a la memoria de la raspberry pi pico 2w
Conectar el ssd1306
Conectar el botón
Cambiar el script de internet para tu conexion
run main.py

enjoy!
---

## 📅 Cronograma de trabajo


[Carta Gantt][https://google.com](https://usmcl-my.sharepoint.com/:x:/r/personal/triquelme_usm_cl/_layouts/15/doc2.aspx?sourcedoc=%7B2A9A3214-9615-4D01-91DF-5A3443D31ACC%7D&file=Carta%20gantt.xlsx&action=default&mobileredirect=true&DefaultItemOpen=1&wdOrigin=APPHOME-WEB.DIRECT%2CAPPHOME-WEB.JUMPBACKIN&wdPreviousSession=3a335a0c-f018-47e1-a44e-cdf08c6902ff&wdPreviousSessionSrc=AppHomeWeb&ct=1744400917492)

---

## 📚 Bibliografía

 -[Image2cpp](https://javl.github.io/image2cpp/) (Image generator for oled screen)
 -[Raspberry Pi Pico 2w pinout](https://datasheets.raspberrypi.com/picow/pico-2-w-pinout.pdf)
 -[Oled screen code-help](https://electronoobs.com/eng_arduino_tut138.php)
 -[Oled screen library](https://docs.arduino.cc/libraries/adafruit-ssd1306/)
 -[AI chat for help](https://chat.deepseek.com/) (Deepseek)
 -[Second AI chat for help](https://chatgpt.com/?model=auto) (Chat gpt)
 -[Oogabooga (Chatbot)](https://docs.arduino.cc/libraries/adafruit-ssd1306/)
 -[Coqui-ai](https://github.com/coqui-ai/TTS)
 -[RVC-Webui]([https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/](https://github.com/oobabooga/text-generation-webui))
   
---

## 📌 Notas adicionales

> *Espacio para dejar cualquier comentario útil, como pendientes, acuerdos del grupo, consideraciones especiales, etc.*

---

## Limitaciones
