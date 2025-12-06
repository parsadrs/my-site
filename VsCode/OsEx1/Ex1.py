import signal
import time
import sys

class InterruptDemo:
    def __init__(self):
        self.interrupt_count = 0
        self.running = True
        
    def interrupt_handler(self, signum, frame):
        """
        Interrupt Service Routine - This function is called when SIGINT (Ctrl+C) is detected
        """
        self.interrupt_count += 1
        print(f"\n{'='*50}")
        print("INTERRUPT ROUTINE ACTIVATED!")
        print(f"Interrupt Number: {self.interrupt_count}")
        print("Time: " + time.strftime("%H:%M:%S"))
        print("Program control transferred to ISR")
        print(f"{'='*50}")
        
        # Simulate some processing in the interrupt routine
        print("Processing in interrupt routine...")
        time.sleep(5)  # Simulate some work being done in the ISR
        
        print("Interrupt processing completed")
        print("Returning control to main program...")
        print(f"{'='*50}\n")
        
    def main_program(self):
        """
        Main program loop - This represents the normal program execution
        """
        # Register our function as the handler for SIGINT (Ctrl+C)
        signal.signal(signal.SIGINT, self.interrupt_handler)
        
        print("Main program started")
        print("Program is displaying sequential numbers...")
        print("Press Ctrl+C to trigger an interrupt")
        print("Press Ctrl+\\ to exit the program")
        print("-" * 40)
        
        counter = 0
        try:
            # Main program loop - runs continuously
            while self.running:
                # Display current number (using \r to overwrite the same line)
                print(f"Main program - Current number: {counter}", end="\r")
                sys.stdout.flush()  # Ensure output is displayed immediately
                counter += 1
                time.sleep(1)  # Short delay to make the display readable
                
        except KeyboardInterrupt:
            # This will catch Ctrl+\ or other termination signals
            print("\n\nProgram terminated successfully!")
            print(f"Total interrupts processed: {self.interrupt_count}")

def main():
    # Create an instance of our interrupt demo class
    demo = InterruptDemo()
    # Start the main program
    demo.main_program()

if __name__ == "__main__":
    main()