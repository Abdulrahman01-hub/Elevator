import time
from elevator import Elevator

def main():
    elevator = Elevator(total_floors=10, capacity=8)
    for turn in range(20):
        print(f"\n--- Turn {turn + 1} ---")
        print(elevator.status())
        elevator.simulate_turn()
        time.sleep(1)

    print("\nSimulation completed.")

if __name__ == "__main__":
    main()