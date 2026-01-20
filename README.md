# Fullstack Flask JWT App

Aplicación **full-stack** que demuestra un flujo completo de **autenticación y autorización** usando **Flask**, **JWT** y un **frontend en JavaScript**.

Este proyecto fue creado como parte de mi portafolio para mostrar habilidades reales de **backend** y **full-stack**, incluyendo diseño de APIs seguras, control de roles y una arquitectura limpia.

---

## Funcionalidades

- API REST desarrollada con Flask
- Autenticación con JWT (access tokens)
- Autorización basada en roles (admin / user)
- Endpoints protegidos
- Operaciones CRUD sobre items
- ORM con SQLAlchemy
- Separación clara entre backend y frontend
- Frontend en JavaScript que consume la API

---

##  Tecnologías Utilizadas

### Backend
- Python
- Flask
- Flask-JWT-Extended
- SQLAlchemy
- SQLite (entorno de desarrollo)

### Frontend
- JavaScript 
- HTML / CSS
- Fetch API

---

## Flujo de Autenticación

1. El usuario inicia sesión con email y contraseña
2. El backend valida las credenciales
3. Se genera un token JWT
4. El frontend guarda el token
5. El token se envía en el header `Authorization` como Bearer Token
6. Los endpoints protegidos validan el token y el rol del usuario

---

## Endpoints de la API

| Método | Endpoint | Descripción | Autenticación | Rol |
|------|---------|------------|---------------|-----|
| POST | `/login` | Login de usuario | ❌ | — |
| GET | `/api/items` | Listar items | ✅ | User |
| POST | `/api/items` | Crear item | ✅ | Admin |
| DELETE | `/api/items/<id>` | Eliminar item | ✅ | Admin |

---
