# 🚀 Sistema de Automatización de Búsqueda de Empleo con IA

## 📋 Descripción

Sistema avanzado de automatización para búsqueda de empleo especializado en **Business Intelligence** y **Big Data**. Genera CVs personalizados automáticamente y envía emails profesionales con **sistema de colores de compatibilidad** dinámico.

## ✨ Características Principales

### 🎨 Sistema de Colores de Compatibilidad
- **🔘 GRIS (30-60%)**: Compatibilidad Baja
- **🟠 NARANJA (61-90%)**: Compatibilidad Media  
- **🟢 VERDE (91-95%)**: Compatibilidad Alta

### 🔍 Búsqueda Inteligente
- ✅ APIs reales de InfoJobs, Tecnoempleo
- ✅ Filtrado por keywords especializadas en BI/Big Data
- ✅ Solo empleos reales, sin simulaciones
- ✅ URLs válidas y verificadas

### 📄 Generación Automática
- ✅ CVs personalizados por empresa y puesto
- ✅ Cartas de presentación adaptadas
- ✅ Formato profesional en Word (.docx)
- ✅ Compresión automática en ZIP

### 📧 Email Profesional
- ✅ Diseño HTML responsive con gradientes
- ✅ Badges de compatibilidad con colores dinámicos
- ✅ Resumen ejecutivo de ofertas
- ✅ Cards individuales por empleo
- ✅ Sección de skills y experiencia
- ✅ Archivos adjuntos automáticos
- **Error Handling**: Comprehensive error handling with retry mechanisms
- **Logging**: Detailed logging for monitoring and debugging
- **No Simulations**: Only real job opportunities from actual sources

## Requirements
- Python 3.8+
- Windows OS (tested on Windows 10/11)
- Gmail account with App Password enabled
- Internet connection

## Setup Instructions

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Email Settings
1. Copy `.env.template` to `.env`
2. Edit `.env` file with your Gmail credentials:
   ```
   SMTP_PASSWORD=your_gmail_app_password
   SENDER_EMAIL=your_email@gmail.com
   ```

### 3. Configure Personal Information
Edit `config.json` with your personal details:
- Update `personal_info` section with your details
- Modify `job_search` keywords if needed
- Set correct email configuration

### 4. Test the System
```bash
python test_system.py
```

### 5. Run Manual Test
```bash
python robust_scheduler.py test
```

### 6. Start Automation
```bash
# Option 1: Use batch file (Windows)
start_automation.bat

# Option 2: Run Python directly
python robust_scheduler.py
```

## File Structure
```
├── final_automation.py      # Main automation system
├── robust_scheduler.py      # Scheduler for automated execution
├── config.json             # Configuration file
├── requirements.txt        # Python dependencies
├── .env.template          # Environment variables template
├── .env                   # Your actual environment variables
├── test_system.py         # System testing script
├── start_automation.bat   # Windows startup script
├── job_applications/      # Generated CVs and reports
├── scheduler.log          # Scheduler logs
└── job_search_automation.log  # Main system logs
```

## Usage

### Automatic Mode
The system runs automatically at:
- **9:00 AM**: Morning job search
- **7:00 PM**: Evening job search

### Manual Mode
```bash
# Run once
python robust_scheduler.py run-once

# Test mode
python robust_scheduler.py test

# Direct automation
python final_automation.py
```

## Job Sources
The system searches the following real sources:
- InfoJobs RSS feeds
- TecnoEmpleo RSS feeds
- LinkedIn (API integration planned)
- Indeed (API integration planned)

## Specialization
The system is specialized in:
- **Business Intelligence**
- **Big Data**
- **Data Analysis**
- **Power BI**
- **Python/SQL**
- **Tableau**
- **Data Science**
- **Analytics**

## Email Reports
Daily email reports include:
- Job opportunities found
- Generated CVs and cover letters
- Job summaries with URLs
- ZIP file with all documents

## Logging
- `scheduler.log`: Scheduler activity and errors
- `job_search_automation.log`: Main system logs
- `test_automation.log`: Test results

## Troubleshooting

### Common Issues
1. **Email not sending**: Check Gmail App Password configuration
2. **No jobs found**: Verify internet connection and RSS feeds
3. **Import errors**: Run `pip install -r requirements.txt`
4. **Encoding issues**: Ensure UTF-8 encoding in all files

### Email Configuration
1. Enable 2-factor authentication in Gmail
2. Generate App Password: Google Account → Security → App passwords
3. Use App Password (not regular password) in `.env` file

### System Health
Run the test script to check system health:
```bash
python test_system.py
```

## Automation Setup for Windows

### Method 1: Windows Task Scheduler
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger for system startup
4. Set action to run `start_automation.bat`

### Method 2: Windows Service
Create a Windows service for the scheduler (advanced users)

## Monitoring
- Check logs regularly for errors
- Monitor email delivery
- Verify job applications folder for generated files

## Security
- Store credentials in `.env` file (not in config.json)
- Use Gmail App Passwords (not regular passwords)
- Keep logs secure and rotate them regularly

## Updates
The system is designed to be maintenance-free, but you can:
- Update keywords in `config.json`
- Add new job sources in `final_automation.py`
- Modify email templates
- Adjust scheduling times

## Support
For issues:
1. Check logs for error messages
2. Run test script to identify problems
3. Verify configuration files
4. Ensure internet connectivity

## Version
Final Version - Production Ready
- Eliminates all simulations
- Uses only real job sources
- Robust error handling
- Autonomous operation
- UTF-8 encoding support
