#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Robust Scheduler for Job Automation System
Handles automated execution at 9:00 AM and 7:00 PM daily
Includes error handling, logging, and recovery mechanisms
"""

import schedule
import time
import logging
import sys
import os
import threading
import signal
from datetime import datetime, timedelta
import subprocess
import traceback
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scheduler.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class RobustScheduler:
    """Robust scheduler for job automation system"""
    
    def __init__(self):
        """Initialize the scheduler"""
        self.running = True
        self.last_execution = None
        self.execution_count = 0
        self.max_retries = 3
        self.retry_delay = 300  # 5 minutes
        
        # Register signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
        
        logger.info("Robust scheduler initialized")
    
    def signal_handler(self, signum, frame):
        """Handle shutdown signals"""
        logger.info(f"Received signal {signum}, shutting down gracefully...")
        self.running = False
    
    def run_automation_with_retry(self):
        """Run automation with retry mechanism"""
        for attempt in range(1, self.max_retries + 1):
            try:
                logger.info(f"Starting automation attempt {attempt}/{self.max_retries}")
                
                # Run the automation script
                result = self.execute_automation()
                
                if result:
                    logger.info("Automation completed successfully")
                    self.last_execution = datetime.now()
                    self.execution_count += 1
                    return True
                else:
                    logger.warning(f"Automation failed on attempt {attempt}")
                    
            except Exception as e:
                logger.error(f"Exception on attempt {attempt}: {e}")
                logger.error(traceback.format_exc())
            
            # Wait before retry (except on last attempt)
            if attempt < self.max_retries:
                logger.info(f"Waiting {self.retry_delay} seconds before retry...")
                time.sleep(self.retry_delay)
        
        logger.error(f"All {self.max_retries} attempts failed")
        return False
    
    def execute_automation(self):
        """Execute the automation script"""
        try:
            # Path to the automation script
            script_path = os.path.join(os.path.dirname(__file__), 'final_automation.py')
            
            if not os.path.exists(script_path):
                logger.error(f"Automation script not found: {script_path}")
                return False
            
            # Execute the script
            logger.info(f"Executing: {script_path}")
            
            # Use subprocess to run the automation
            process = subprocess.Popen(
                [sys.executable, script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8'
            )
            
            stdout, stderr = process.communicate(timeout=1800)  # 30 minutes timeout
            
            if process.returncode == 0:
                logger.info("Automation script executed successfully")
                if stdout:
                    logger.info(f"Script output: {stdout}")
                return True
            else:
                logger.error(f"Automation script failed with return code {process.returncode}")
                if stderr:
                    logger.error(f"Error output: {stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            logger.error("Automation script timed out")
            process.kill()
            return False
        except Exception as e:
            logger.error(f"Error executing automation: {e}")
            return False
    
    def check_system_health(self):
        """Check system health and resources"""
        try:
            # Check disk space
            import shutil
            total, used, free = shutil.disk_usage('.')
            free_gb = free // (1024**3)
            
            if free_gb < 1:  # Less than 1 GB free
                logger.warning(f"Low disk space: {free_gb} GB free")
                return False
            
            # Check if required files exist
            required_files = ['final_automation.py', 'config.json']
            for file in required_files:
                if not os.path.exists(file):
                    logger.error(f"Required file missing: {file}")
                    return False
            
            return True
            
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return False
    
    def scheduled_job(self):
        """The job to run on schedule"""
        try:
            logger.info("=" * 50)
            logger.info("SCHEDULED JOB EXECUTION STARTED")
            logger.info(f"Execution time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            logger.info("=" * 50)
            
            # Check system health
            if not self.check_system_health():
                logger.error("System health check failed, skipping execution")
                return
            
            # Run automation with retry
            success = self.run_automation_with_retry()
            
            if success:
                logger.info("Scheduled job completed successfully")
            else:
                logger.error("Scheduled job failed after all retries")
            
            logger.info("=" * 50)
            logger.info("SCHEDULED JOB EXECUTION COMPLETED")
            logger.info("=" * 50)
            
        except Exception as e:
            logger.error(f"Error in scheduled job: {e}")
            logger.error(traceback.format_exc())
    
    def setup_schedule(self):
        """Set up the schedule for automation"""
        try:
            # Schedule for 9:00 AM daily
            schedule.every().day.at("09:00").do(self.scheduled_job)
            logger.info("Scheduled daily automation at 09:00")
            
            # Schedule for 7:00 PM daily
            schedule.every().day.at("19:00").do(self.scheduled_job)
            logger.info("Scheduled daily automation at 19:00")
            
            # Optional: Schedule for testing (every 2 hours during development)
            # schedule.every(2).hours.do(self.scheduled_job)
            # logger.info("Scheduled automation every 2 hours (testing)")
            
        except Exception as e:
            logger.error(f"Error setting up schedule: {e}")
            raise
    
    def run_scheduler(self):
        """Run the scheduler main loop"""
        try:
            logger.info("Starting robust scheduler...")
            logger.info(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Set up schedule
            self.setup_schedule()
            
            # Show next scheduled runs
            next_runs = schedule.jobs
            logger.info("Scheduled jobs:")
            for job in next_runs:
                logger.info(f"  - {job}")
            
            # Main scheduler loop
            while self.running:
                try:
                    schedule.run_pending()
                    time.sleep(60)  # Check every minute
                    
                    # Log status every hour
                    if datetime.now().minute == 0:
                        logger.info(f"Scheduler running - Next execution: {schedule.next_run()}")
                        logger.info(f"Total executions: {self.execution_count}")
                        if self.last_execution:
                            logger.info(f"Last execution: {self.last_execution.strftime('%Y-%m-%d %H:%M:%S')}")
                    
                except Exception as e:
                    logger.error(f"Error in scheduler loop: {e}")
                    time.sleep(60)  # Wait before continuing
            
            logger.info("Scheduler stopped")
            
        except Exception as e:
            logger.error(f"Critical error in scheduler: {e}")
            logger.error(traceback.format_exc())
    
    def test_automation(self):
        """Test the automation system"""
        try:
            logger.info("Testing automation system...")
            
            # Check system health
            if not self.check_system_health():
                logger.error("System health check failed")
                return False
            
            # Run automation once
            success = self.run_automation_with_retry()
            
            if success:
                logger.info("Automation test passed")
                return True
            else:
                logger.error("Automation test failed")
                return False
                
        except Exception as e:
            logger.error(f"Error testing automation: {e}")
            return False

def main():
    """Main function"""
    try:
        # Create scheduler instance
        scheduler = RobustScheduler()
        
        # Check command line arguments
        if len(sys.argv) > 1:
            if sys.argv[1] == "test":
                # Test mode
                logger.info("Running in test mode")
                success = scheduler.test_automation()
                sys.exit(0 if success else 1)
            elif sys.argv[1] == "run-once":
                # Run once
                logger.info("Running automation once")
                success = scheduler.run_automation_with_retry()
                sys.exit(0 if success else 1)
        
        # Normal scheduler mode
        logger.info("Starting in scheduler mode")
        scheduler.run_scheduler()
        
    except KeyboardInterrupt:
        logger.info("Scheduler interrupted by user")
    except Exception as e:
        logger.error(f"Critical error in main: {e}")
        logger.error(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()
