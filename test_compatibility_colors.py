#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script to demonstrate the color-coded compatibility system
"""

import os
import sys
from datetime import datetime
from simple_automation import JobAutomationSystem

def main():
    """Test the color-coded compatibility system"""
    
    # Create test jobs with different compatibility levels
    test_jobs = [
        {
            "title": "Junior Data Entry Clerk",
            "company": "Basic Company",
            "location": "Madrid, España",
            "url": "https://www.infojobs.net/madrid/data-entry-clerk/of-low-compatibility",
            "description": "Buscamos una persona para entrada de datos básica. Conocimientos de Excel requeridos. No se requiere experiencia previa en análisis de datos.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs"
        },
        {
            "title": "Business Intelligence Analyst",
            "company": "Tech Solutions Madrid",
            "location": "Madrid, España",
            "url": "https://www.infojobs.net/madrid/business-intelligence-analyst/of-medium-compatibility",
            "description": "Buscamos un Business Intelligence Analyst con experiencia en SQL, Power BI y análisis de datos. Conocimientos en Python y dashboard creation son valorados. Experiencia en data analytics necesaria.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs"
        },
        {
            "title": "Senior Data Scientist - Business Intelligence Expert",
            "company": "Premium Analytics Corp",
            "location": "Barcelona, España",
            "url": "https://www.infojobs.net/barcelona/senior-data-scientist-bi-expert/of-high-compatibility",
            "description": "Buscamos un Senior Data Scientist especializado en Business Intelligence con experiencia avanzada en Python, SQL, Power BI, Tableau, machine learning, ETL, data warehousing, Azure, AWS, Spark, analytics, dashboard development, data modeling, y big data. Experiencia en data governance y stakeholder management esencial.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs"
        }
    ]
    
    # Initialize automation system
    automation = JobAutomationSystem()
    automation.cvs_generated = [
        'CV_Test_1.docx', 'CV_Test_2.docx', 'CV_Test_3.docx',
        'Cover_Letter_1.docx', 'Cover_Letter_2.docx', 'Cover_Letter_3.docx'
    ]
    
    # Calculate compatibility for each job and show colors
    print("🎨 SISTEMA DE COLORES DE COMPATIBILIDAD")
    print("=" * 50)
    
    for i, job in enumerate(test_jobs, 1):
        compatibility = automation.calculate_compatibility(job)
        compatibility_class = automation.get_compatibility_class(compatibility)
        
        if compatibility_class == "compatibility-low":
            color_name = "GRIS"
            color_desc = "Compatibilidad Baja"
        elif compatibility_class == "compatibility-medium":
            color_name = "NARANJA"
            color_desc = "Compatibilidad Media"
        else:
            color_name = "VERDE"
            color_desc = "Compatibilidad Alta"
        
        print(f"\n{i}. {job['title']}")
        print(f"   Empresa: {job['company']}")
        print(f"   Compatibilidad: {compatibility}%")
        print(f"   Color: {color_name} ({color_desc})")
        print(f"   Clase CSS: {compatibility_class}")
    
    print("\n" + "=" * 50)
    print("RANGOS DE COLORES:")
    print("• 30-60%: 🔘 GRIS (Compatibilidad Baja)")
    print("• 61-90%: 🟠 NARANJA (Compatibilidad Media)")
    print("• 91-95%: 🟢 VERDE (Compatibilidad Alta)")
    print("=" * 50)
    
    # Generate HTML email with color-coded compatibility
    html_content = automation.create_html_email_body(test_jobs)
    
    # Save HTML to file for preview
    output_file = f"compatibility_colors_preview_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\n✅ Vista previa HTML guardada en: {output_file}")
    print("📧 Abre este archivo en tu navegador para ver los colores de compatibilidad")
    print("🎨 Verás los badges de compatibilidad en diferentes colores según el porcentaje")
    
    # Try to open the file automatically
    try:
        os.system(f'start {output_file}')
        print("🌐 Archivo abierto automáticamente en el navegador")
    except:
        print(f"💡 Abre manualmente {output_file} en tu navegador para ver los colores")

if __name__ == "__main__":
    main()
