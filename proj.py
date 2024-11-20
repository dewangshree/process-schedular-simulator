import os
from collections import deque

class Process:
    def __init__(self, pid, arrival, burst):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.remaining = burst
        self.completion = self.waiting = self.turnaround = 0

def fcfs(processes):
    processes.sort(key=lambda p: p.arrival)
    time_elapsed = 0
    print("\nGantt Chart:")
    for p in processes:
        time_elapsed = max(time_elapsed, p.arrival)
        print(f"[{time_elapsed} -> P{p.pid}] ", end="")
        time_elapsed += p.burst
        p.completion = time_elapsed
    calculate_metrics(processes)

def round_robin(processes, quantum):
    queue = deque(processes)
    time_elapsed = 0
    print("\nGantt Chart:")
    while queue:
        p = queue.popleft()
        time_elapsed = max(time_elapsed, p.arrival)
        print(f"[{time_elapsed} -> P{p.pid}] ", end="")
        if p.remaining <= quantum:
            time_elapsed += p.remaining
            p.remaining = 0
            p.completion = time_elapsed
        else:
            time_elapsed += quantum
            p.remaining -= quantum
            queue.append(p)
    calculate_metrics(processes)

def calculate_metrics(processes):
    print("\n\nProcess Completion:")
    for p in processes:
        p.turnaround = p.completion - p.arrival
        p.waiting = p.turnaround - p.burst
        print(f"P{p.pid}: CT={p.completion}, TAT={p.turnaround}, WT={p.waiting}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    n = int(input("Enter number of processes: "))
    processes = [Process(i + 1, int(input(f"Arrival time P{i+1}: ")), int(input(f"Burst time P{i+1}: "))) for i in range(n)]
    algo = int(input("\n1. FCFS\n2. Round Robin\nChoose algorithm: "))
    if algo == 1:
        fcfs(processes)
    elif algo == 2:
        round_robin(processes, int(input("Enter time quantum: ")))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
