# Git Flow Example API

Repositorio informativo que muestra cómo aplicar **GitFlow**, **versionado SemVer**, y **empaquetar un proyecto Python con FastAPI en Docker**.  
Cada release genera un **tag** y una **imagen Docker** en GitHub Container Registry, demostrando un flujo completo replicable en proyectos reales.

---

## 🔹 Tecnologías utilizadas

- Python 3.11 2
- [FastAPI](https://fastapi.tiangolo.com/)  
- Docker / Docker Compose  
- GitFlow + SemVer  
- GitHub Actions (CI/CD y publicación de imágenes)

---

## 🚀 Levantar el servidor

Primero, asegúrate de tener Docker instalado en tu máquina. Luego ejecuta:

```bash
docker run -d -p 8000:8000 --name gitflow-api ghcr.io/medranoq/git-flow-example
```

## 📡 Endpoints disponibles

| Endpoint       | Descripción                                           | Ejemplo de petición                       |
|----------------|------------------------------------------------------|------------------------------------------|
| `/`            | Mensaje "Hello World" y versión de la API           | `curl http://localhost:8000/`           |
| `/hello/{name}`| Saluda a un usuario por nombre y devuelve la versión| `curl http://localhost:8000/hello/Medrano` |
| `/version`     | Devuelve la versión actual de la API                | `curl http://localhost:8000/version`    |


Mismos que peudes encontrar en http://localhost:8000/docs