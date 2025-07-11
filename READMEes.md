# Nominator+ 📊

Un sistema integral de gestión de empleados desarrollado con Python y Tkinter, diseñado para manejar registros de empleados, bajas, informes y gestión de nóminas.

## 🚀 Características

- **Gestión de Empleados**: Agregar, eliminar y gestionar registros de empleados
- **Procesamiento de Bajas**: Manejar bajas de empleados con documentación adecuada
- **Generación de Informes**: Generar varios informes de empleados
- **Gestión de Nóminas**: Gestionar información de nóminas de empleados
- **Validación de Documentos**: Validar documentos de identificación españoles (NIF, NIE, NAF, IBAN)

## 📋 Requisitos

- Python 3.7+
- tkinter (generalmente incluido con Python)
- sqlite3 (incluido con Python)
- Archivo de imagen requerido: `Face.png` (logo de la aplicación)

## 🛠️ Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/5alvh/Nominator-plus.git
cd nominator-plus
```

2. Asegúrate de tener Python 3.7+ instalado:
```bash
python --version
```

3. Coloca el archivo de imagen `Face.png` en el directorio raíz del proyecto

4. Ejecuta la aplicación:
```bash
python main.py
```

## 📁 Estructura del Proyecto

```
nominator-plus/
├── main.py                 # Punto de entrada principal de la aplicación
├── App.py                  # Clase principal de la GUI
├── funcionesPy.py          # Utilidades de validación
├── AltasFich.py           # Módulo de registro de empleados
├── BajasFic.py            # Módulo de bajas de empleados
├── InformesFic.py         # Módulo de generación de informes
├── NominasFich.py         # Módulo de gestión de nóminas
├── Face.png               # Logo de la aplicación
├── empleados.db           # Base de datos SQLite (se crea automáticamente)
└── README.md              # Este archivo
```

## 🎯 Uso

### Iniciar la Aplicación

Ejecuta la aplicación principal:
```bash
python main.py
```

La ventana principal mostrará cuatro módulos principales:

1. **ALTAS** - Registro de Empleados
2. **BAJAS** - Bajas de Empleados
3. **INFORMES** - Informes
4. **NÓMINAS** - Nóminas

### Bajas de Empleados

El módulo de bajas permite:
- Eliminar empleados de la base de datos activa
- Registrar fecha de baja
- Mantener registros de bajas en una tabla separada

**Uso:**
1. Ingresa el código del empleado
2. Ingresa la fecha de baja (formato: dd-mm-yyyy)
3. Haz clic en "Confirmar" para procesar

### Validación de Documentos

La aplicación incluye validación integral para documentos de identificación españoles:

- **NIF (Número de Identificación Fiscal)**: DNI español
- **NIE (Número de Identidad de Extranjero)**: ID de residente extranjero
- **NAF (Número de Afiliación Fiscal)**: Número de afiliación fiscal
- **IBAN**: Número de cuenta bancaria internacional

## 🗄️ Esquema de Base de Datos

La aplicación usa SQLite con las siguientes tablas:

### tabla empleados
- `id`: Clave primaria
- `nombre`: Nombre del empleado
- `nif`: Identificación nacional
- `genero`: Género
- Campos adicionales definidos en AltasFich.py

### tabla bajas
- `id`: ID del empleado
- `nombre`: Nombre del empleado
- `nif`: Identificación nacional
- `fecha_baja`: Fecha de baja
- `genero`: Género

## 🔧 Configuración

### Configuración de la GUI
- Tamaño de ventana: 500x500 píxeles
- Ventana principal no redimensionable
- Diseño basado en rejilla con columnas responsivas

### Configuración de Base de Datos
- Archivo de base de datos: `empleados.db`
- Se crea automáticamente en la primera ejecución
- Las tablas se crean automáticamente si no existen

## 🎨 Personalización

### Estilo
La aplicación usa un esquema de color amarillo consistente (`#FFFF99`) para los botones. Puedes modificar el estilo en el método `crearApp()` en `App.py`.

### Agregar Nuevos Módulos
Para agregar nueva funcionalidad:
1. Crea un nuevo archivo Python (ej., `NuevoModulo.py`)
2. Impórtalo en `App.py`
3. Agrega un nuevo botón en el método `crearApp()`
4. Crea un método de lanzamiento siguiendo el patrón existente

## 🐛 Manejo de Errores

La aplicación incluye manejo de errores para:
- Archivos de imagen faltantes
- Problemas de conexión a base de datos
- Formatos de fecha inválidos
- Errores de validación de documentos

## 📝 Reglas de Validación

### Formato de Fecha
- Formato: dd-mm-yyyy
- Patrón regex: `^\d{2}-\d{2}-\d{4}$`

### Validación NIF
- Formato: 8 dígitos + 1 letra
- Validación de suma de control usando algoritmo oficial

### Validación NIE
- Formato: [XYZ] + 7 dígitos + 1 letra
- Validación de suma de control con sustitución de letras

### Validación NAF
- Formato: A/B/C (números separados por barras)
- Validación módulo 97

### Validación IBAN
- IBAN español de 24 caracteres
- Validación algoritmo MOD-97

## 🤝 Contribuir

1. Haz fork del repositorio
2. Crea una rama de característica (`git checkout -b feature/CaracteristicaIncreible`)
3. Confirma tus cambios (`git commit -m 'Agregar alguna CaracteristicaIncreible'`)
4. Sube a la rama (`git push origin feature/CaracteristicaIncreible`)
5. Abre un Pull Request

## 👥 Autores

- Salah Eddine Khouadri - Trabajo inicial - [MyGithub](https://github.com/5alvh)

## 🙏 Agradecimientos

- Desarrollado con tkinter de Python para soporte GUI multiplataforma
- Usa SQLite para gestión de base de datos ligera
- Implementa estándares de validación de documentos españoles

## 🔮 Mejoras Futuras

- [ ] Agregar gestión de fotos de empleados
- [ ] Implementar funcionalidad de backup/restauración
- [ ] Agregar características de exportación a Excel/PDF
- [ ] Implementar autenticación de usuario
- [ ] Agregar búsqueda avanzada y filtrado
- [ ] Soporte multiidioma

---

Para más información o soporte, por favor abre un issue en GitHub.
