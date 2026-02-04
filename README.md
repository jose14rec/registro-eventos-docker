# Registro de Eventos – Servicio Distribuido Dockerizado

Proyecto final de la asignatura Computación Distribuida.  
Implementa un servicio distribuido simple para registrar eventos utilizando Docker, Docker Compose, Flask y PostgreSQL.

---

## Caso seleccionado
Servicio distribuido de registro de eventos.

---

## Arquitectura

El sistema está compuesto por tres elementos principales:

- Cliente: Postman (consumo de la API)
- Backend: API REST desarrollada con Flask y ejecutada en un contenedor Docker
- Base de datos: PostgreSQL desplegada en un contenedor Docker
- Orquestación: Docker Compose
- Comunicación: HTTP mediante APIs REST

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio:

git clone https://github.com/jose14rec/registro-eventos-docker.git  
cd registro-eventos-docker  

2. Construir y levantar los servicios:

docker compose up --build

---

## Endpoints

### POST /events
http://localhost:5000/events

Ejemplo de cuerpo JSON:

{
  "tipo": "Sistema",
  "descripcion": "Inicio",
  "fecha": "2026-01-28"
}

---

### GET /events
http://localhost:5000/events

---

## Archivos principales

- app.py: backend del sistema
- Dockerfile: configuración de la imagen del backend
- docker-compose.yml: orquestación de los contenedores
- requirements.txt: dependencias del proyecto

---

## Autor

José Alejandro Recalde  
Proyecto académico – Computación Distribuida
