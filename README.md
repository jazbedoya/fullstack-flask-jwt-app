# Fullstack Flask JWT App

Aplicación **full-stack** que combina un **backend en Flask** y un **frontend en React**, con autenticación segura mediante **JWT** y consumo de una **API externa de productos de ropa deportiva**.

El proyecto fue desarrollado como parte de mi portafolio para demostrar habilidades reales de **backend**, **frontend** y **arquitectura full-stack**.

---

##  Funcionalidades Principales

- API REST desarrollada con Flask
- Autenticación con JWT (Bearer Token)
- Control de acceso por roles (admin / user)
- Endpoints protegidos
- CRUD de items internos
- Consumo de API externa de ropa deportiva
- Backend actúa como intermediario seguro
- Frontend en React consumiendo la API

---

## Tecnologías Utilizadas

### Backend
- Python
- Flask
- Flask-JWT-Extended
- SQLAlchemy
- Flask-CORS
- SQLite (entorno de desarrollo)

### Frontend
- React
- JavaScript (ES6+)
- Fetch API
- HTML / CSS

---

##  Flujo de Autenticación

1. El usuario inicia sesión con email y contraseña
2. El backend valida las credenciales
3. Se genera un **JWT**
4. El frontend guarda el token
5. El token se envía en el header:
