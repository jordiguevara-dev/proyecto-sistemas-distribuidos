# PC1 - Sistema Distribuido de Inventario (Neptuno)

## 1. Requerimientos de Infraestructura
- **Plataforma:** Google Cloud Platform (GCP).
- **Servidor BD:** Instancia Debian con MariaDB (IP: 104.154.47.132).
- **Servidor Middleware:** Instancia Debian con Java 17 (IP: 34.68.239.254).

## 2. Manual de Despliegue

### Middleware (Java Spring Boot)
1. Compilar el proyecto localmente: `.\mvnw.cmd clean package -DskipTests`.
2. Subir el archivo `middleware-0.0.1-SNAPSHOT.jar` a la instancia de GCP vía SSH.
3. Ejecutar el servidor: `java -jar middleware-0.0.1-SNAPSHOT.jar`.
4. El servidor escuchará en el puerto 8080.

### Cliente (Python)
1. Instalar dependencias: `pip install requests`.
2. Configurar la variable `IP_NUBE` en `cliente.py` con la IP `34.68.239.254`.
3. Ejecutar: `python cliente.py`.

## 3. Lógica de Negocio e Integridad
El sistema garantiza la integridad **ACID** mediante el uso de la anotación `@Transactional` en el middleware de Java, asegurando que el registro de pedidos y la actualización de stock se realicen de forma atómica.
