#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script to send a sample email with the new beautiful HTML design
NOTE: You need to configure your Gmail credentials in .env file
"""

import os
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from simple_automation import JobAutomationSystem
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def send_test_email():
    """Send a test email with the new HTML design"""
    
    # Email configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = os.getenv('SENDER_EMAIL', 'vladimir.jcr@gmail.com')
    sender_password = os.getenv('SMTP_PASSWORD')
    recipient_email = sender_email  # Send to yourself
    
    if not sender_password or sender_password == 'your_gmail_app_password_here':
        print("⚠️  Email password not configured!")
        print("📧 To test the email:")
        print("1. Enable 2-factor authentication in Gmail")
        print("2. Generate App Password in Google Account settings")
        print("3. Update SMTP_PASSWORD in .env file")
        print("4. Run this script again")
        return False
    
    # Create test data
    test_jobs = [
        {
            "title": "Senior Data Analyst - Business Intelligence",
            "company": "Banco Santander",
            "location": "Madrid, España",
            "url": "https://www.infojobs.net/madrid/data-analyst-business-intelligence/of-i4b6a7c8d9e0f1g2h3i4j5k6l7m8n9o0",
            "description": "Buscamos un Senior Data Analyst con experiencia en Business Intelligence para unirse a nuestro equipo en Madrid. Experiencia requerida en Python, SQL, Power BI y análisis de datos financieros. Responsabilidades incluyen desarrollo de dashboards, análisis de KPIs y colaboración con equipos multidisciplinarios para la toma de decisiones estratégicas.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs"
        },
        {
            "title": "Business Intelligence Developer",
            "company": "Telefónica",
            "location": "Barcelona, España", 
            "url": "https://www.infojobs.net/barcelona/senior-business-intelligence-developer/of-j5k6l7m8n9o0p1q2r3s4t5u6v7w8x9y0",
            "description": "Oportunidad para BI Developer con experiencia en Tableau, SQL Server, y desarrollo de dashboards. Conocimientos en ETL y data warehousing necesarios. Trabajarás en proyectos de transformación digital y modernización de sistemas de reportes, implementando soluciones de Business Intelligence de última generación.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs"
        },
        {
            "title": "Data Scientist - Machine Learning",
            "company": "BBVA",
            "location": "Madrid, España",
            "url": "https://www.infojobs.net/madrid/data-scientist-machine-learning/of-l7m8n9o0p1q2r3s4t5u6v7w8x9y0z1a2",
            "description": "Data Scientist para equipo de innovación en BBVA. Experiencia en Python, scikit-learn, TensorFlow y modelos predictivos. Sector financiero. Desarrollarás algoritmos de machine learning para detección de fraudes, análisis de riesgo crediticio y personalización de productos financieros.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs"
        }
    ]
    
    try:
        # Initialize automation system
        automation = JobAutomationSystem()
        automation.cvs_generated = [
            'CV_Banco_Santander_Data_Analyst.docx',
            'CV_Telefonica_BI_Developer.docx', 
            'CV_BBVA_Data_Scientist.docx',
            'Cover_Letter_Banco_Santander.docx',
            'Cover_Letter_Telefonica.docx',
            'Cover_Letter_BBVA.docx'
        ]
        
        # Create message
        msg = MIMEMultipart('alternative')
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = Header("🔍 Reporte Diario de Búsqueda de Empleo - DEMO", 'utf-8')
        
        # Create HTML content
        html_content = automation.create_html_email_body(test_jobs)
        
        # Create plain text version
        plain_text = f"""
🔍 Reporte Diario de Búsqueda de Empleo - DEMO
Fecha: {datetime.now().strftime('%Y-%m-%d')}

📊 RESUMEN EJECUTIVO:
- Ofertas Encontradas: {len(test_jobs)}
- CVs Generados: {len(automation.cvs_generated)}
- Especialización: Business Intelligence & Big Data

🎯 OFERTAS DE EMPLEO:
"""
        
        for i, job in enumerate(test_jobs, 1):
            plain_text += f"""
{i}. {job['title']} en {job['company']}
   📍 {job['location']}
   🔗 {job['url']}
   📝 {job['description'][:150]}...
   
"""
        
        plain_text += """
🚀 PRÓXIMOS PASOS:
1. Revisar CVs y cartas de presentación adjuntas
2. Aplicar a las posiciones seleccionadas  
3. Hacer seguimiento de las aplicaciones

Saludos cordiales,
Sistema de Automatización de Búsqueda de Empleo
"""
        
        # Attach both versions
        msg.attach(MIMEText(plain_text, 'plain', 'utf-8'))
        msg.attach(MIMEText(html_content, 'html', 'utf-8'))
        
        # Send email
        print("📧 Sending test email...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        print("✅ Test email sent successfully!")
        print(f"📩 Check your inbox: {recipient_email}")
        print("🎨 The email should have the beautiful gradient design like the image")
        
        return True
        
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

def main():
    """Main function"""
    print("🎨 Testing Beautiful HTML Email Design")
    print("=" * 40)
    
    success = send_test_email()
    
    if success:
        print("\n🎉 Email test completed successfully!")
        print("📧 Check your Gmail inbox for the beautiful email report")
    else:
        print("\n⚠️  Email test failed")
        print("🔧 Please configure your Gmail credentials and try again")

if __name__ == "__main__":
    main()
