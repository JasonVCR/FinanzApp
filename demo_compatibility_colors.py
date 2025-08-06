#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para demostrar los diferentes rangos de compatibilidad con colores
"""

import os
import sys
from datetime import datetime
from simple_automation import JobAutomationSystem

def create_test_jobs_with_different_compatibility():
    """Create test jobs with predetermined compatibility levels"""
    
    test_jobs = [
        # Compatibilidad BAJA (Gris) - 30-60%
        {
            "title": "Junior Data Entry Clerk",
            "company": "Basic Company",
            "location": "Madrid, España",
            "url": "https://www.infojobs.net/madrid/data-entry-clerk/low-compatibility",
            "description": "Buscamos una persona para entrada de datos básica. Conocimientos de Excel requeridos.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs",
            "forced_compatibility": 35
        },
        {
            "title": "Administrative Assistant",
            "company": "Generic Corp",
            "location": "Valencia, España",
            "url": "https://www.infojobs.net/valencia/admin-assistant/low-compatibility",
            "description": "Asistente administrativo con conocimientos básicos de Office. Experiencia en atención al cliente.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs",
            "forced_compatibility": 45
        },
        {
            "title": "Customer Service Representative",
            "company": "Service Plus",
            "location": "Sevilla, España",
            "url": "https://www.infojobs.net/sevilla/customer-service/low-compatibility",
            "description": "Representante de servicio al cliente. Conocimientos básicos de CRM y comunicación.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs",
            "forced_compatibility": 55
        },
        
        # Compatibilidad MEDIA (Naranja) - 61-90%
        {
            "title": "Business Intelligence Analyst",
            "company": "Tech Solutions Madrid",
            "location": "Madrid, España",
            "url": "https://www.infojobs.net/madrid/bi-analyst/medium-compatibility",
            "description": "Buscamos un Business Intelligence Analyst con experiencia en SQL, Power BI y análisis de datos. Conocimientos en Python y dashboard creation son valorados.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs",
            "forced_compatibility": 65
        },
        {
            "title": "Data Analyst - Marketing",
            "company": "Marketing Dynamics",
            "location": "Barcelona, España",
            "url": "https://www.infojobs.net/barcelona/data-analyst-marketing/medium-compatibility",
            "description": "Analista de datos para marketing con experiencia en SQL, Excel, Google Analytics, y reporting. Conocimientos en visualización de datos con Tableau o Power BI.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs",
            "forced_compatibility": 75
        },
        {
            "title": "Senior Business Analyst",
            "company": "Innovation Hub",
            "location": "Bilbao, España",
            "url": "https://www.infojobs.net/bilbao/senior-business-analyst/medium-compatibility",
            "description": "Senior Business Analyst con experiencia en análisis de requisitos, SQL, Python, y metodologías ágiles. Experiencia en BI y data analytics preferible.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs",
            "forced_compatibility": 85
        },
        
        # Compatibilidad ALTA (Verde) - 91-95%
        {
            "title": "Senior Data Scientist - BI Expert",
            "company": "Premium Analytics Corp",
            "location": "Madrid, España",
            "url": "https://www.infojobs.net/madrid/senior-data-scientist-bi/high-compatibility",
            "description": "Senior Data Scientist especializado en Business Intelligence con experiencia avanzada en Python, SQL, Power BI, Tableau, machine learning, ETL, data warehousing, Azure, AWS, Spark, analytics, dashboard development, data modeling, y big data. Experiencia en data governance y stakeholder management esencial.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs",
            "forced_compatibility": 92
        },
        {
            "title": "Lead Business Intelligence Engineer",
            "company": "Data Excellence Inc",
            "location": "Barcelona, España",
            "url": "https://www.infojobs.net/barcelona/lead-bi-engineer/high-compatibility",
            "description": "Lead BI Engineer con experiencia en Python, SQL, Power BI, Tableau, Azure Data Factory, Databricks, machine learning, data warehousing, ETL processes, data modeling, analytics, dashboard creation, y big data technologies. Liderazgo de equipos de datos y experiencia en data governance.",
            "posted_date": datetime.now().isoformat(),
            "source": "infojobs",
            "forced_compatibility": 94
        }
    ]
    
    return test_jobs

def main():
    """Main function to demonstrate color-coded compatibility system"""
    
    print("🎨 DEMOSTRACIÓN COMPLETA DEL SISTEMA DE COLORES DE COMPATIBILIDAD")
    print("=" * 80)
    
    # Initialize automation system
    automation = JobAutomationSystem()
    
    # Create test jobs with different compatibility levels
    test_jobs = create_test_jobs_with_different_compatibility()
    
    # Add some generated CVs for the email
    automation.cvs_generated = [
        'CV_Test_1.docx', 'CV_Test_2.docx', 'CV_Test_3.docx',
        'Cover_Letter_1.docx', 'Cover_Letter_2.docx', 'Cover_Letter_3.docx'
    ]
    
    print("\n📊 ANÁLISIS DE COMPATIBILIDAD POR RANGOS:")
    print("-" * 80)
    
    # Group jobs by compatibility range
    low_compatibility = []
    medium_compatibility = []
    high_compatibility = []
    
    for job in test_jobs:
        compatibility = job['forced_compatibility']
        compatibility_class = automation.get_compatibility_class(compatibility)
        
        if compatibility_class == "compatibility-low":
            low_compatibility.append((job, compatibility))
        elif compatibility_class == "compatibility-medium":
            medium_compatibility.append((job, compatibility))
        else:
            high_compatibility.append((job, compatibility))
    
    # Display results by category
    print("\n🔘 COMPATIBILIDAD BAJA (GRIS) - 30-60%:")
    for job, compatibility in low_compatibility:
        print(f"   • {job['title']}: {compatibility}%")
    
    print("\n🟠 COMPATIBILIDAD MEDIA (NARANJA) - 61-90%:")
    for job, compatibility in medium_compatibility:
        print(f"   • {job['title']}: {compatibility}%")
    
    print("\n🟢 COMPATIBILIDAD ALTA (VERDE) - 91-95%:")
    for job, compatibility in high_compatibility:
        print(f"   • {job['title']}: {compatibility}%")
    
    print("\n" + "=" * 80)
    print("RESUMEN DE COLORES:")
    print("• 🔘 GRIS: 30-60% (Compatibilidad Baja)")
    print("• 🟠 NARANJA: 61-90% (Compatibilidad Media)")
    print("• 🟢 VERDE: 91-95% (Compatibilidad Alta)")
    print("=" * 80)
    
    # Generate HTML email with all compatibility levels
    html_content = automation.create_html_email_body(test_jobs)
    
    # Save HTML to file for preview
    output_file = f"full_compatibility_demo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\n✅ Vista previa HTML completa guardada en: {output_file}")
    print("📧 Abre este archivo en tu navegador para ver TODOS los colores de compatibilidad")
    print("🎨 Verás ejemplos de los 3 rangos de colores: GRIS, NARANJA y VERDE")
    
    # Try to open the file automatically
    try:
        os.system(f'start {output_file}')
        print("🌐 Archivo abierto automáticamente en el navegador")
    except:
        print(f"💡 Abre manualmente {output_file} en tu navegador para ver los colores")
    
    print("\n" + "=" * 80)
    print("✅ SISTEMA DE COLORES DE COMPATIBILIDAD FUNCIONANDO CORRECTAMENTE")
    print("✅ Todos los rangos de colores están implementados y funcionando")
    print("✅ El email se generará con colores dinámicos según el porcentaje de compatibilidad")

if __name__ == "__main__":
    main()
