#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for the job automation system
Verifies all components work correctly
"""

import os
import sys
import json
import logging
from datetime import datetime
import traceback

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('test_automation.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def test_imports():
    """Test if all required modules can be imported"""
    try:
        logger.info("Testing imports...")
        
        import requests
        import feedparser
        from docx import Document
        import pandas as pd
        from dotenv import load_dotenv
        import schedule
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        
        logger.info("All imports successful")
        return True
        
    except ImportError as e:
        logger.error(f"Import error: {e}")
        return False

def test_configuration():
    """Test configuration file"""
    try:
        logger.info("Testing configuration...")
        
        if not os.path.exists('config.json'):
            logger.error("config.json not found")
            return False
        
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        required_sections = ['personal_info', 'job_search', 'email_config']
        for section in required_sections:
            if section not in config:
                logger.error(f"Missing section in config: {section}")
                return False
        
        logger.info("Configuration test passed")
        return True
        
    except Exception as e:
        logger.error(f"Configuration test failed: {e}")
        return False

def test_automation_system():
    """Test the automation system"""
    try:
        logger.info("Testing automation system...")
        
        # Import the automation system
        from final_automation import JobAutomationSystem
        
        # Initialize system
        automation = JobAutomationSystem()
        
        # Test job search
        logger.info("Testing job search...")
        jobs = automation.search_jobs_real_sources()
        
        if not jobs:
            logger.warning("No jobs found (this might be normal)")
        else:
            logger.info(f"Found {len(jobs)} jobs")
        
        # Test directory creation
        test_dir = os.path.join('test_output', datetime.now().strftime('%Y-%m-%d'))
        os.makedirs(test_dir, exist_ok=True)
        
        # Test CV generation if jobs found
        if jobs:
            logger.info("Testing CV generation...")
            cv_path = automation.generate_cv_for_job(jobs[0], test_dir)
            if cv_path and os.path.exists(cv_path):
                logger.info("CV generation test passed")
            else:
                logger.warning("CV generation test failed")
        
        logger.info("Automation system test completed")
        return True
        
    except Exception as e:
        logger.error(f"Automation system test failed: {e}")
        logger.error(traceback.format_exc())
        return False

def test_email_configuration():
    """Test email configuration"""
    try:
        logger.info("Testing email configuration...")
        
        from dotenv import load_dotenv
        load_dotenv()
        
        # Check if email credentials are configured
        smtp_password = os.getenv('SMTP_PASSWORD')
        if not smtp_password or smtp_password == 'your_gmail_app_password_here':
            logger.warning("Email password not configured properly")
            return False
        
        # Test SMTP connection (without sending)
        import smtplib
        
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        email_config = config['email_config']
        
        server = smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port'])
        server.starttls()
        server.login(email_config['sender_email'], smtp_password)
        server.quit()
        
        logger.info("Email configuration test passed")
        return True
        
    except Exception as e:
        logger.error(f"Email configuration test failed: {e}")
        return False

def test_scheduler():
    """Test the scheduler"""
    try:
        logger.info("Testing scheduler...")
        
        from robust_scheduler import RobustScheduler
        
        # Initialize scheduler
        scheduler = RobustScheduler()
        
        # Test health check
        if not scheduler.check_system_health():
            logger.error("System health check failed")
            return False
        
        logger.info("Scheduler test passed")
        return True
        
    except Exception as e:
        logger.error(f"Scheduler test failed: {e}")
        return False

def run_all_tests():
    """Run all tests"""
    logger.info("=" * 60)
    logger.info("STARTING COMPREHENSIVE SYSTEM TEST")
    logger.info(f"Test time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 60)
    
    tests = [
        ("Imports", test_imports),
        ("Configuration", test_configuration),
        ("Automation System", test_automation_system),
        ("Email Configuration", test_email_configuration),
        ("Scheduler", test_scheduler)
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        logger.info(f"\nRunning test: {test_name}")
        logger.info("-" * 30)
        
        try:
            result = test_func()
            results[test_name] = result
            
            if result:
                logger.info(f"✓ {test_name} PASSED")
            else:
                logger.error(f"✗ {test_name} FAILED")
                
        except Exception as e:
            logger.error(f"✗ {test_name} ERROR: {e}")
            results[test_name] = False
    
    # Summary
    logger.info("\n" + "=" * 60)
    logger.info("TEST SUMMARY")
    logger.info("=" * 60)
    
    passed = sum(1 for result in results.values() if result)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✓ PASSED" if result else "✗ FAILED"
        logger.info(f"{test_name}: {status}")
    
    logger.info(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        logger.info("🎉 ALL TESTS PASSED - System is ready for production!")
        return True
    else:
        logger.error("❌ SOME TESTS FAILED - Please fix issues before production")
        return False

def main():
    """Main function"""
    try:
        success = run_all_tests()
        sys.exit(0 if success else 1)
        
    except Exception as e:
        logger.error(f"Critical error in test: {e}")
        logger.error(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()
