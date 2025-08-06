#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Versión mejorada del cálculo de compatibilidad para mejor distribución de colores
"""

import re
import random
from datetime import datetime
from simple_automation import JobAutomationSystem

class ImprovedCompatibilityCalculator:
    """Calculador de compatibilidad mejorado para mejor distribución"""
    
    def __init__(self, config):
        self.config = config
        self.my_skills = config['job_search']['keywords']
        
        # Categorizar skills por importancia
        self.high_value_skills = [
            'python', 'sql', 'power bi', 'tableau', 'business intelligence',
            'data analyst', 'data science', 'analytics', 'big data',
            'machine learning', 'azure', 'aws'
        ]
        
        self.medium_value_skills = [
            'etl', 'data warehouse', 'databricks', 'spark', 'pandas',
            'numpy', 'visualization', 'qlik sense', 'looker', 'snowflake',
            'reporting', 'dashboard', 'statistics'
        ]
        
        self.bonus_keywords = [
            'senior', 'lead', 'specialist', 'expert', 'advanced',
            'years experience', 'bi', 'data', 'analysis', 'analytics'
        ]
    
    def calculate_improved_compatibility(self, job):
        """Calculate improved compatibility with better distribution"""
        job_text = f"{job['title']} {job.get('description', '')}".lower()
        
        # Initialize scoring
        compatibility_score = 0
        
        # 1. High-value skills matching (40% of total score)
        high_value_matches = sum(1 for skill in self.high_value_skills if skill in job_text)
        high_value_score = (high_value_matches / len(self.high_value_skills)) * 40
        compatibility_score += high_value_score
        
        # 2. Medium-value skills matching (30% of total score)
        medium_value_matches = sum(1 for skill in self.medium_value_skills if skill in job_text)
        medium_value_score = (medium_value_matches / len(self.medium_value_skills)) * 30
        compatibility_score += medium_value_score
        
        # 3. Title relevance (20% of total score)
        title_score = 0
        if any(keyword in job['title'].lower() for keyword in ['data', 'business intelligence', 'bi', 'analyst', 'analytics']):
            title_score = 20
        elif any(keyword in job['title'].lower() for keyword in ['python', 'sql', 'developer']):
            title_score = 15
        elif any(keyword in job['title'].lower() for keyword in ['science', 'scientist', 'engineer']):
            title_score = 10
        compatibility_score += title_score
        
        # 4. Bonus keywords (10% of total score)
        bonus_matches = sum(1 for keyword in self.bonus_keywords if keyword in job_text)
        bonus_score = min(bonus_matches * 2, 10)  # Max 10 points
        compatibility_score += bonus_score
        
        # 5. Experience level adjustment
        if 'senior' in job_text or 'lead' in job_text:
            compatibility_score += 5
        elif 'junior' in job_text:
            compatibility_score -= 5
        
        # 6. Company/industry bonus
        if any(word in job_text for word in ['tech', 'technology', 'data', 'analytics', 'intelligence']):
            compatibility_score += 5
        
        # Ensure realistic distribution
        compatibility_score = max(30, min(95, compatibility_score))
        
        # Add slight randomization for variety (±3%)
        variation = random.randint(-3, 3)
        final_score = max(30, min(95, int(compatibility_score + variation)))
        
        return final_score

def test_improved_compatibility():
    """Test the improved compatibility calculator"""
    
    # Initialize systems
    automation = JobAutomationSystem()
    with open('config.json', 'r', encoding='utf-8') as f:
        import json
        config = json.load(f)
    
    improved_calc = ImprovedCompatibilityCalculator(config)
    
    # Test jobs designed to hit different compatibility ranges
    test_jobs = [
        # Low compatibility jobs (should be 30-60% - GRIS)
        {
            "title": "Cashier",
            "description": "Cashier position for retail store. Basic math skills required.",
            "company": "Retail Store"
        },
        {
            "title": "Administrative Assistant",
            "description": "Administrative assistant with basic computer skills. Filing and data entry.",
            "company": "Office Corp"
        },
        {
            "title": "Customer Service Representative",
            "description": "Customer service with basic computer knowledge and communication skills.",
            "company": "Service Plus"
        },
        
        # Medium compatibility jobs (should be 61-90% - NARANJA)
        {
            "title": "Business Analyst",
            "description": "Business analyst with experience in SQL, data analysis, and reporting. Excel and basic python knowledge preferred.",
            "company": "Tech Solutions"
        },
        {
            "title": "Data Analyst",
            "description": "Data analyst position requiring SQL, Python, and data visualization skills. Experience with tableau or power bi preferred.",
            "company": "Analytics Corp"
        },
        {
            "title": "Junior Data Scientist",
            "description": "Junior data scientist with python, sql, machine learning, and statistics knowledge. Business intelligence experience a plus.",
            "company": "Data Insights"
        },
        
        # High compatibility jobs (should be 91-95% - VERDE)
        {
            "title": "Senior Business Intelligence Developer",
            "description": "Senior BI developer with advanced python, sql, power bi, tableau, etl, data warehouse, azure, and business intelligence expertise. Machine learning and big data experience required.",
            "company": "Data Excellence"
        },
        {
            "title": "Lead Data Scientist - BI Specialist",
            "description": "Lead data scientist specializing in business intelligence with expert-level python, sql, power bi, tableau, machine learning, azure, aws, spark, databricks, analytics, and big data technologies.",
            "company": "Premium Analytics"
        },
        {
            "title": "Senior Data Analyst - Business Intelligence Expert",
            "description": "Senior data analyst with business intelligence expertise. Advanced python, sql, power bi, tableau, etl, data warehouse, machine learning, azure, spark, analytics, reporting, dashboard, and big data skills required.",
            "company": "BI Masters"
        }
    ]
    
    print("🔄 PROBANDO CALCULADOR DE COMPATIBILIDAD MEJORADO")
    print("="*60)
    
    # Test both calculators
    results = []
    
    for job in test_jobs:
        original_score = automation.calculate_compatibility(job)
        improved_score = improved_calc.calculate_improved_compatibility(job)
        
        original_class = automation.get_compatibility_class(original_score)
        improved_class = automation.get_compatibility_class(improved_score)
        
        color_map = {
            "compatibility-low": "🔘 GRIS",
            "compatibility-medium": "🟠 NARANJA", 
            "compatibility-high": "🟢 VERDE"
        }
        
        results.append({
            'job': job,
            'original_score': original_score,
            'improved_score': improved_score,
            'original_color': color_map[original_class],
            'improved_color': color_map[improved_class]
        })
    
    # Display results
    print("\n📊 COMPARACIÓN DE RESULTADOS:")
    print("-"*60)
    
    for result in results:
        print(f"\n🏢 {result['job']['title']}")
        print(f"   Original: {result['original_score']}% ({result['original_color']})")
        print(f"   Mejorado: {result['improved_score']}% ({result['improved_color']})")
        
        if result['original_color'] != result['improved_color']:
            print(f"   ⚡ CAMBIO DE COLOR: {result['original_color']} → {result['improved_color']}")
    
    # Generate distribution summary
    print("\n📈 DISTRIBUCIÓN DE COLORES:")
    print("-"*60)
    
    original_colors = {'🔘 GRIS': 0, '🟠 NARANJA': 0, '🟢 VERDE': 0}
    improved_colors = {'🔘 GRIS': 0, '🟠 NARANJA': 0, '🟢 VERDE': 0}
    
    for result in results:
        original_colors[result['original_color']] += 1
        improved_colors[result['improved_color']] += 1
    
    print("Original:")
    for color, count in original_colors.items():
        print(f"  {color}: {count} trabajos")
    
    print("\nMejorado:")
    for color, count in improved_colors.items():
        print(f"  {color}: {count} trabajos")
    
    # Generate sample email with improved scores
    print("\n📧 GENERANDO EMAIL CON COMPATIBILIDAD MEJORADA...")
    
    # Update jobs with improved scores
    for i, job in enumerate(test_jobs):
        improved_score = improved_calc.calculate_improved_compatibility(job)
        job['compatibility_override'] = improved_score
        job['url'] = f"https://www.infojobs.net/job-{i+1}/demo"
        job['location'] = "Madrid, España"
        job['posted_date'] = datetime.now().isoformat()
        job['source'] = "infojobs"
    
    # Generate HTML email
    automation.cvs_generated = ['Demo_CV_1.docx', 'Demo_CV_2.docx', 'Demo_Cover_Letter.docx']
    html_content = automation.create_html_email_body(test_jobs)
    
    # Save HTML file
    output_file = f"improved_compatibility_demo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Email de demostración guardado: {output_file}")
    
    # Try to open automatically
    try:
        import os
        os.system(f'start {output_file}')
        print("🌐 Archivo abierto automáticamente en el navegador")
    except:
        print(f"💡 Abre manualmente {output_file} en tu navegador")
    
    return output_file

if __name__ == "__main__":
    test_improved_compatibility()
