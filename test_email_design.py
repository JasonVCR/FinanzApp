#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for the new HTML email design
"""

import os
import sys
from datetime import datetime
from simple_automation import JobAutomationSystem

def main():
    """Test the new HTML email design"""
    
    # Create test data similar to what the system would generate
    test_jobs = [
        {
            "title": "Data Analyst - Business Intelligence",
            "company": "Tech Solutions Madrid",
            "location": "Madrid, España",
            "url": "https://www.infojobs.net/madrid/data-analyst-business-intelligence/of-i4b6a7c8d9e0f1g2h3i4j5k6l7m8n9o0",
            "description": "Buscamos un Data Analyst con experiencia en Business Intelligence para unirse a nuestro equipo en Madrid. Experiencia requerida en Python, SQL, Power BI y análisis de datos financieros. Responsabilidades incluyen desarrollo de dashboards interactivos y análisis predictivos para mejorar la toma de decisiones empresariales. Conocimientos en R y Tableau son valorados. Experiencia mínima de 3 años en análisis de datos.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs"
        },
        {
            "title": "Senior Business Intelligence Developer",
            "company": "Telefónica Digital",
            "location": "Barcelona, España",
            "url": "https://www.infojobs.net/barcelona/senior-business-intelligence-developer/of-j5k6l7m8n9o0p1q2r3s4t5u6v7w8x9y0",
            "description": "Oportunidad para Senior BI Developer con experiencia en Tableau, SQL Server, y desarrollo de dashboards. Conocimientos en ETL y data warehousing necesarios. Trabajarás en proyectos de transformación digital y modernización de sistemas de reportes. Experiencia con Python, Azure, y herramientas de visualización. Mínimo 5 años de experiencia en Business Intelligence.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs"
        },
        {
            "title": "Junior Data Scientist - Machine Learning",
            "company": "BBVA Innovation Center",
            "location": "Madrid, España",
            "url": "https://www.infojobs.net/madrid/data-scientist-machine-learning/of-l7m8n9o0p1q2r3s4t5u6v7w8x9y0z1a2",
            "description": "Data Scientist para equipo de innovación en BBVA. Experiencia en Python, scikit-learn, SQL y modelos predictivos. Desarrollarás algoritmos de machine learning para detección de fraudes y análisis de riesgo crediticio. Conocimientos en Spark, Hadoop y AWS son valorados. Experiencia de 1-2 años en data science.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs"
        }
    ]
    
    # Initialize the automation system
    automation = JobAutomationSystem()
    automation.cvs_generated = ['CV_1.docx', 'CV_2.docx', 'CV_3.docx', 'Cover_Letter_1.docx', 'Cover_Letter_2.docx', 'Cover_Letter_3.docx']
    
    # Generate HTML email
    html_content = automation.create_html_email_body(test_jobs)
    
    # Save HTML to file for preview
    output_file = f"email_preview_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ HTML email preview saved to: {output_file}")
    print("📧 Open this file in your browser to see the email design")
    print("🎨 The design matches the gradient style shown in the image")
    
    # Try to open the file automatically
    try:
        os.system(f'start {output_file}')
    except:
        print(f"💡 Manually open {output_file} in your browser to preview the email design")

if __name__ == "__main__":
    main()
