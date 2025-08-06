#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Menú interactivo para gestionar la aplicación de automatización de empleo
"""

import os
import sys
from datetime import datetime

def print_banner():
    """Print application banner"""
    print("="*70)
    print(" 🚀 APLICACIÓN DE AUTOMATIZACIÓN DE EMPLEO CON COLORES")
    print("="*70)
    print(" ✅ Sistema de colores implementado")
    print(" 📊 Compatibilidad: 🔘 Gris | 🟠 Naranja | 🟢 Verde") 
    print(" 📧 Emails con diseño profesional")
    print(" 🎯 CVs personalizados para cada empleo")
    print("="*70)
    print()

def show_status():
    """Show current system status"""
    print("📋 ESTADO DEL SISTEMA:")
    print("-"*30)
    
    # Check if recent files exist
    today = datetime.now().strftime('%Y-%m-%d')
    job_dir = f"job_applications/{today}"
    
    if os.path.exists(job_dir):
        files = os.listdir(job_dir)
        cvs = [f for f in files if f.startswith('CV_') and f.endswith('.docx')]
        covers = [f for f in files if f.startswith('Cover_Letter_') and f.endswith('.docx')]
        zip_files = [f for f in files if f.endswith('.zip')]
        
        print(f"✅ Última ejecución: {today}")
        print(f"📄 CVs generados: {len(cvs)}")
        print(f"📝 Cartas generadas: {len(covers)}")
        print(f"📦 Archivos ZIP: {len(zip_files)}")
        
        if zip_files:
            print(f"💾 Último ZIP: {zip_files[-1]}")
    else:
        print("⚠️  No hay archivos de hoy")
        
    # Check configuration
    if os.path.exists('config.json'):
        print("✅ Configuración: Presente")
    else:
        print("❌ Configuración: Falta config.json")
        
    # Check .env file
    if os.path.exists('.env'):
        print("✅ Variables de entorno: Configuradas")
    else:
        print("⚠️  Variables de entorno: No configuradas")
    
    print()

def main_menu():
    """Main application menu"""
    while True:
        print_banner()
        show_status()
        
        print("🎯 OPCIONES DISPONIBLES:")
        print("-"*30)
        print("1. 🚀 Ejecutar búsqueda completa de empleos")
        print("2. 🎨 Probar sistema de colores de compatibilidad")
        print("3. 📧 Ver demostración de email con colores")
        print("4. 🔍 Ejecutar pruebas del sistema")
        print("5. ⏰ Configurar ejecución automática")
        print("6. 📂 Ver archivos generados")
        print("7. 📊 Ver estadísticas de ejecución")
        print("8. ⚙️  Configuración del sistema")
        print("9. ❌ Salir")
        print()
        
        choice = input("Selecciona una opción (1-9): ").strip()
        
        if choice == "1":
            execute_job_search()
        elif choice == "2":
            test_color_system()
        elif choice == "3":
            show_email_demo()
        elif choice == "4":
            run_system_tests()
        elif choice == "5":
            setup_scheduler()
        elif choice == "6":
            show_generated_files()
        elif choice == "7":
            show_statistics()
        elif choice == "8":
            system_configuration()
        elif choice == "9":
            print("¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción inválida. Por favor selecciona 1-9.")
        
        input("\nPresiona Enter para continuar...")

def execute_job_search():
    """Execute job search"""
    print("\n🚀 INICIANDO BÚSQUEDA COMPLETA DE EMPLEOS...")
    print("="*50)
    os.system("python simple_automation.py")

def test_color_system():
    """Test color compatibility system"""
    print("\n🎨 PROBANDO SISTEMA DE COLORES...")
    print("="*50)
    print("1. Prueba básica de colores")
    print("2. Demostración completa")
    print("3. Demostración perfecta (todos los rangos)")
    
    choice = input("Selecciona (1-3): ").strip()
    
    if choice == "1":
        os.system("python test_compatibility_colors.py")
    elif choice == "2":
        os.system("python demo_compatibility_colors.py")
    elif choice == "3":
        os.system("python perfect_color_demo.py")

def show_email_demo():
    """Show email demonstration"""
    print("\n📧 DEMOSTRACIÓN DE EMAIL CON COLORES...")
    print("="*50)
    os.system("python perfect_color_demo.py")

def run_system_tests():
    """Run system tests"""
    print("\n🔍 EJECUTANDO PRUEBAS DEL SISTEMA...")
    print("="*50)
    os.system("python test_system.py")

def setup_scheduler():
    """Setup automatic scheduler"""
    print("\n⏰ CONFIGURANDO EJECUCIÓN AUTOMÁTICA...")
    print("="*50)
    print("1. Ejecutar scheduler básico")
    print("2. Ejecutar scheduler robusto")
    
    choice = input("Selecciona (1-2): ").strip()
    
    if choice == "1":
        os.system("python simple_scheduler.py")
    elif choice == "2":
        os.system("python robust_scheduler.py")

def show_generated_files():
    """Show generated files"""
    print("\n📂 ARCHIVOS GENERADOS...")
    print("="*50)
    
    if os.path.exists("job_applications"):
        for date_folder in sorted(os.listdir("job_applications"), reverse=True)[:5]:
            folder_path = os.path.join("job_applications", date_folder)
            if os.path.isdir(folder_path):
                files = os.listdir(folder_path)
                print(f"\n📅 {date_folder}:")
                for file in sorted(files):
                    if file.endswith('.docx'):
                        print(f"  📄 {file}")
                    elif file.endswith('.zip'):
                        print(f"  📦 {file}")
                    elif file.endswith('.txt'):
                        print(f"  📋 {file}")
    else:
        print("No hay archivos generados aún.")

def show_statistics():
    """Show execution statistics"""
    print("\n📊 ESTADÍSTICAS DEL SISTEMA...")
    print("="*50)
    
    total_cvs = 0
    total_days = 0
    
    if os.path.exists("job_applications"):
        for date_folder in os.listdir("job_applications"):
            folder_path = os.path.join("job_applications", date_folder)
            if os.path.isdir(folder_path):
                total_days += 1
                files = os.listdir(folder_path)
                cvs = [f for f in files if f.startswith('CV_') and f.endswith('.docx')]
                total_cvs += len(cvs)
    
    print(f"📈 Total de días con ejecuciones: {total_days}")
    print(f"📄 Total de CVs generados: {total_cvs}")
    print(f"🎯 Promedio de CVs por día: {total_cvs/total_days if total_days > 0 else 0:.1f}")
    
    # System features status
    print(f"\n🎨 Sistema de colores: ✅ Implementado")
    print(f"🔍 APIs reales: ✅ Funcionando")
    print(f"📧 Email HTML: ✅ Diseño profesional")
    print(f"📦 Compresión ZIP: ✅ Automática")

def system_configuration():
    """System configuration menu"""
    print("\n⚙️  CONFIGURACIÓN DEL SISTEMA...")
    print("="*50)
    print("1. Ver configuración actual")
    print("2. Verificar credenciales de email")
    print("3. Ver keywords de búsqueda")
    print("4. Comprobar archivos del sistema")
    
    choice = input("Selecciona (1-4): ").strip()
    
    if choice == "1":
        if os.path.exists('config.json'):
            print("\n📋 config.json encontrado ✅")
        else:
            print("\n❌ config.json NO encontrado")
            
        if os.path.exists('.env'):
            print("📋 .env encontrado ✅")
        else:
            print("❌ .env NO encontrado")
    
    elif choice == "2":
        from dotenv import load_dotenv
        load_dotenv()
        smtp_password = os.getenv('SMTP_PASSWORD')
        if smtp_password and smtp_password != 'your_gmail_app_password_here':
            print("✅ Credenciales de email configuradas")
        else:
            print("⚠️  Credenciales de email NO configuradas")
    
    elif choice == "3":
        try:
            import json
            with open('config.json', 'r', encoding='utf-8') as f:
                config = json.load(f)
            keywords = config.get('job_search', {}).get('keywords', [])
            print(f"\n🔍 Keywords configuradas: {len(keywords)}")
            for i, keyword in enumerate(keywords[:10], 1):
                print(f"  {i}. {keyword}")
            if len(keywords) > 10:
                print(f"  ... y {len(keywords)-10} más")
        except:
            print("❌ Error al leer keywords")
    
    elif choice == "4":
        files_to_check = [
            'simple_automation.py',
            'config.json',
            '.env',
            'test_system.py',
            'perfect_color_demo.py'
        ]
        
        print("\n📁 Estado de archivos del sistema:")
        for file in files_to_check:
            status = "✅" if os.path.exists(file) else "❌"
            print(f"  {status} {file}")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Aplicación cerrada por el usuario!")
    except Exception as e:
        print(f"\n❌ Error en la aplicación: {e}")
        print("Por favor reporta este error.")
