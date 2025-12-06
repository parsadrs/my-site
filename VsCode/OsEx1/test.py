import signal
import time
import sys

class InterruptDemo:
    def __init__(self):
        self.interrupt_count = 0
        self.in_interrupt = False
        self.waiting_for_exit = False

    def sigint_handler(self, signum, frame):
        """Handler for Ctrl+C - enter interrupt mode"""
        if self.in_interrupt:
            print("\nAlready in interrupt mode!")
            return
            
        self.interrupt_count += 1
        self.in_interrupt = True

        print(f"\n{'-'*50}")
        print("INTERRUPT ACTIVATED")
        print(f"Interrupt Number: {self.interrupt_count}")
        print("Press Ctrl+Z to return to main program after countdown")
        print(f"{'-'*50}")

        # Wait for Ctrl+Z to exit
        self.waiting_for_exit = True
        print("\nWaiting for Ctrl+Z to exit...")
        
        while self.waiting_for_exit:
            time.sleep(0.1)
        
        # Countdown before returning to main program
        print("\nReturning to main program in:")
        for i in range(3, 0, -1):
            print(f" {i}...", end="\r")
            time.sleep(1)
        print("\nReturned to main program!\n")
        
        self.in_interrupt = False

    def sigtstp_handler(self, signum, frame):
        """Handler for Ctrl+Z - exit interrupt mode"""
        if not self.in_interrupt:
            print(f"\n{'#'*50}")
            print("Ctrl+Z IGNORED!")
            print("You must press Ctrl+C first to enter interrupt mode")
            print(f"{'#'*50}\n")
            return
            
        if self.waiting_for_exit:
            print("\nCtrl+Z detected! Preparing to return to main program...")
            self.waiting_for_exit = False

    def main_program(self):
        # Register signal handlers
        signal.signal(signal.SIGINT, self.sigint_handler)  # Ctrl+C
        signal.signal(signal.SIGTSTP, self.sigtstp_handler)  # Ctrl+Z

        print("Main program started")
        print("Press Ctrl+C to enter interrupt mode")
        print("Press Ctrl+Z to exit interrupt mode (after Ctrl+C)")
        print("-" * 50)

        counter = 0
        try:
            while True:
                print(f"Main program running: {counter}", end="\r")
                counter += 1
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n\nProgram terminated successfully!")
            print(f"Total interrupts processed: {self.interrupt_count}")

def main():
    demo = InterruptDemo()
    demo.main_program()

if __name__ == "__main__":
    main()