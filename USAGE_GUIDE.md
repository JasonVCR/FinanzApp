# 📚 GUÍA RÁPIDA DE USO - Sistema de Automatización de Empleo

## 🚀 Inicio Rápido

### 1. Primera Configuración
```bash
# Clonar repositorio
git clone https://github.com/JasonVCR/FinanzApp.git
cd FinanzApp

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements_automation.txt
```

### 2. Configurar Credenciales
```bash
# Crear archivo .env
echo SMTP_PASSWORD=tu_contraseña_de_aplicacion > .env
```

### 3. Ejecutar por Primera Vez
```bash
# Prueba rápida del sistema
python test_system.py

# Ejecutar búsqueda completa
python simple_automation.py

# Ver demostración de colores
python perfect_color_demo.py
```

## 🎯 Comandos Principales

| Comando | Descripción |
|---------|-------------|
| `python simple_automation.py` | Ejecuta búsqueda completa |
| `python perfect_color_demo.py` | Demuestra sistema de colores |
| `python app_menu.py` | Menú interactivo |
| `python test_system.py` | Pruebas del sistema |
| `python robust_scheduler.py` | Scheduler automático |

## 📧 Configuración de Email

### Gmail (Recomendado)
1. Ir a [Configuración de Google](https://myaccount.google.com/)
2. Activar autenticación de 2 factores
3. Ir a "Contraseñas de aplicaciones"
4. Generar nueva contraseña para "Correo"
5. Usar esa contraseña en el archivo `.env`

### Otros Proveedores
Configurar en `config.json`:
```json
{
  "email_config": {
    "smtp_server": "smtp.tu-proveedor.com",
    "smtp_port": 587,
    "sender_email": "tu@email.com",
    "recipient_email": "destinatario@email.com"
  }
}
```

## 🎨 Sistema de Colores Explicado

### Rangos de Compatibilidad
- **🔘 GRIS (30-60%)**: Trabajos con baja compatibilidad con tu perfil
- **🟠 NARANJA (61-90%)**: Trabajos con compatibilidad media, buenos candidatos
- **🟢 VERDE (91-95%)**: Trabajos altamente compatibles, aplicar prioritariamente

### Factores de Evaluación
1. **Keywords Match**: Coincidencias con tu perfil
2. **Nivel de Experiencia**: Senior/Mid/Junior
3. **Relevancia del Título**: Palabras clave importantes
4. **Industria**: Sector tecnológico/datos
5. **Skills Premium**: Python, SQL, Power BI, etc.

## 📁 Estructura de Archivos Generados

```
job_applications/
├── 2025-08-06/
│   ├── CV_Empresa_Puesto.docx          # CV personalizado
│   ├── Cover_Letter_Empresa_Puesto.docx # Carta personalizada
│   ├── CVs_Generated_2025-08-06.zip    # Todos los docs
│   └── Job_Summary_2025-08-06.txt      # Resumen del día
├── 2025-08-07/
└── logs/
    └── automation.log                   # Logs del sistema
```

## ⏰ Automatización Diaria

### Configurar Scheduler
```bash
python robust_scheduler.py
```

### Windows Task Scheduler
```batch
# Crear tarea diaria a las 9:00 AM
schtasks /create /tn "JobAutomation" /tr "C:\ruta\python simple_automation.py" /sc daily /st 09:00
```

### Linux/Mac Crontab
```bash
# Ejecutar a las 9:00 AM y 7:00 PM diariamente
0 9,19 * * * /usr/bin/python3 /ruta/simple_automation.py
```

## 🔧 Personalización Avanzada

### Modificar Keywords de Búsqueda
Editar `config.json`:
```json
{
  "job_search": {
    "keywords": [
      "tu_skill_1",
      "tu_skill_2",
      "tu_especialidad"
    ]
  }
}
```

### Cambiar Diseño de Email
Modificar función `create_html_email_body()` en `simple_automation.py`:
- Colores: Variables CSS en la función
- Layout: Estructura HTML
- Logos: Agregar imágenes en base64

### Agregar Nuevas Fuentes de Empleo
Agregar URLs RSS en `search_jobs_real_sources()`:
```python
job_sources = [
    "https://nueva-fuente.com/rss/jobs",
    # ... otras fuentes
]
```

## 🛠️ Troubleshooting

### Error: "No module named..."
```bash
pip install -r requirements_automation.txt
```

### Error de Credenciales de Email
1. Verificar contraseña de aplicación
2. Comprobar archivo `.env`
3. Verificar configuración en `config.json`

### No Se Encuentran Empleos
1. Verificar conexión a internet
2. Comprobar URLs RSS en el código
3. Revisar keywords en `config.json`

### Archivos No Se Generan
1. Verificar permisos de escritura
2. Comprobar espacio en disco
3. Revisar logs en `automation.log`

## 📊 Métricas y Monitoreo

### Ver Estadísticas
```bash
python -c "
import os
total_cvs = 0
for folder in os.listdir('job_applications'):
    path = f'job_applications/{folder}'
    if os.path.isdir(path):
        cvs = [f for f in os.listdir(path) if f.startswith('CV_')]
        total_cvs += len(cvs)
        print(f'{folder}: {len(cvs)} CVs')
print(f'Total: {total_cvs} CVs generados')
"
```

### Logs Importantes
- `automation.log`: Log principal del sistema
- `test_automation.log`: Logs de pruebas
- `job_applications/*/Job_Summary_*.txt`: Resúmenes diarios

## 🤝 Contribuir al Proyecto

1. Fork del repositorio
2. Crear rama: `git checkout -b feature/nueva-funcionalidad`
3. Hacer cambios y commit: `git commit -am 'Añadir funcionalidad'`
4. Push: `git push origin feature/nueva-funcionalidad`
5. Crear Pull Request

## 📞 Soporte

- **GitHub Issues**: Para reportar bugs
- **Discussions**: Para sugerencias y dudas
- **Email**: vladimir.jcr@gmail.com (solo para consultas urgentes)

---

**¡Disfruta automatizando tu búsqueda de empleo! 🚀**
