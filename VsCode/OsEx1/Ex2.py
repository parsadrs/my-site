import signal
import time
import sys
import os
import threading

class InterruptDemo:
    def __init__(self):
        self.sigint_count = 0
        self.sigtstp_count = 0
        self.running = True
        self.waiting_for_sigtstp = False
        self.sigtstp_received = False
        self.sigtstp_lock = threading.Lock()
        
    def sigint_handler(self, signum, frame):
        if self.waiting_for_sigtstp:
            print("Already waiting for SIGTSTP, ignoring new SIGINT")
            return
            
        self.sigint_count += 1
        print(f"\n{'-'*50}")
        print("SIGINT Interrupt Routine Activated")
        print(f"SIGINT Interrupt Number: {self.sigint_count}")
        print("Activated Time: " + time.strftime("%H:%M:%S"))
        print(f"{'-'*50}")
        
        print("Processing in first phase...")
        time.sleep(1)
        
        print("Waiting for SIGTSTP (Ctrl+Z) to continue...")
        self.waiting_for_sigtstp = True
        self.sigtstp_received = False
        
        # Wait for SIGTSTP (Ctrl+Z)
        wait_start = time.time()
        while self.waiting_for_sigtstp:  
            time.sleep(0.1)
            
        if self.sigtstp_received:
            print("SIGTSTP received, continuing SIGINT processing...")
            print("Processing in second phase...")
            time.sleep(1)
            print("SIGINT interrupt processing completed")
            
        print("Returning control to main program...")
        print(f"{'-'*50}\n")
        self.waiting_for_sigtstp = False
        
    def sigtstp_handler(self, signum, frame):
        """Interrupt service routine for Ctrl+Z (SIGTSTP)"""
        if not self.waiting_for_sigtstp:
            # If not waiting for SIGTSTP, handle it as standalone interrupt
            self.sigtstp_count += 1
            print(f"\n{'='*50}")
            print("SIGTSTP Interrupt Routine Activated!")
            print(f"SIGTSTP Interrupt Number: {self.sigtstp_count}")
            print("Time: " + time.strftime("%H:%M:%S"))
            print("Program control transferred to SIGTSTP ISR")
            print(f"{'='*50}")
            
            print("Processing in SIGTSTP interrupt routine...")
            time.sleep(2)
            
            print("SIGTSTP interrupt processing completed")
            print("Returning control to main program...")
            print(f"{'='*50}\n")
        else:
            # If waiting for SIGTSTP as part of SIGINT sequence
            print("\nSIGTSTP received! Continuing SIGINT processing...")
            self.sigtstp_received = True
            self.waiting_for_sigtstp = False
        
    def main_program(self):
        """Main program loop"""
        # Register interrupt handlers
        signal.signal(signal.SIGINT, self.sigint_handler)
        signal.signal(signal.SIGTSTP, self.sigtstp_handler)
        
        print("Main program started")
        print("Program is displaying sequential numbers...")
        print("Available interrupts:")
        print("   • Ctrl+C - Trigger SIGINT interrupt (waits for Ctrl+Z)")
        print("   • Ctrl+Z - Trigger SIGTSTP interrupt")
        print("   • Ctrl+\\ - Exit program")
        print("Workflow: Ctrl+C → waits for Ctrl+Z → continues Ctrl+C → returns to main")
        print("-" * 70)
        
        counter = 0
        try:
            while self.running:
                print(f"Main program - Current number: {counter}", end="\r")
                sys.stdout.flush()
                counter += 1
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n\nProgram terminated successfully!")
            print(f"Interrupt Statistics:")
            print(f"   • SIGINT interrupts (Ctrl+C): {self.sigint_count}")
            print(f"   • SIGTSTP interrupts (Ctrl+Z): {self.sigtstp_count}")
def main():
    demo = InterruptDemo()
    demo.main_program()
if __name__ == "__main__":
    main()