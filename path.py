import numpy as np
import pandas as pd
import time
import math
import random

# --- SETTINGS ---
FILE_NAME = 'coordinates.csv'
TIME_LIMIT = 100            # Execution time in seconds
INITIAL_TEMPERATURE = 50.0  # Starting temperature for the exploration phase
FINAL_TEMPERATURE = 0.01    # Temperature at the final second of the algorithm
# ---------------

def load_data(filename):
    try:
        df = pd.read_csv(filename, sep=r'[\s,]+', engine='python', header=None)
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        df = df.dropna()
        
        ids = df.iloc[:, 0].astype(int).values
        x_coords = df.iloc[:, -2].values
        y_coords = df.iloc[:, -1].values
        return ids, x_coords, y_coords
    except Exception as e:
        print(f"Data reading error: {e}")
        return None, None, None

def calc_matrix(x, y):
    n = len(x)
    mat = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            d = math.hypot(x[i]-x[j], y[i]-y[j])
            mat[i][j] = d
            mat[j][i] = d
    return mat

def nearest_neighbor(mat):
    n = len(mat)
    unv = set(range(1, n))
    tour = [0]
    curr = 0
    while unv:
        nxt = min(unv, key=lambda c: mat[curr][c])
        tour.append(nxt)
        unv.remove(nxt)
        curr = nxt
    return tour

def calc_cost(tour, mat):
    n = len(tour)
    return sum(mat[tour[i]][tour[(i+1)%n]] for i in range(n))

def simulated_annealing(mat):
    print("Generating initial route (Nearest Neighbor)...")
    current_tour = nearest_neighbor(mat)
    current_cost = calc_cost(current_tour, mat)
    
    best_tour = current_tour.copy()
    best_cost = current_cost
    
    start_t = time.time()
    n = len(current_tour)
    iteration = 0
    temp = INITIAL_TEMPERATURE
    
    print(f"Initial Cost: {best_cost:.2f} km")
    print(f"Dynamic Cooling SA started, will run for exactly {TIME_LIMIT} seconds...\n")
    
    while True:
        # To avoid slowing down the loop, time and temperature are calculated 
        # only once every 10,000 iterations rather than at every step.
        if iteration % 10000 == 0:
            elapsed_time = time.time() - start_t
            if elapsed_time >= TIME_LIMIT:
                break
                
            # Time-Based Exponential Cooling
            # Temperature smoothly drops from INITIAL to FINAL as time goes from 0% to 100%
            progress = elapsed_time / TIME_LIMIT
            temp = INITIAL_TEMPERATURE * math.pow(FINAL_TEMPERATURE / INITIAL_TEMPERATURE, progress)
            
            # Prints to the screen every 500k steps to show live progress
            if iteration % 500000 == 0:
                print(f"[{elapsed_time:5.1f}s] Temperature: {temp:7.2f} | Best Cost: {best_cost:.2f} km")

        i, j = random.randint(0, n-1), random.randint(0, n-1)
        if i > j:
            i, j = j, i
            
        if j - i <= 1 or (i == 0 and j == n - 1):
            iteration += 1
            continue
            
        A, B = current_tour[i - 1], current_tour[i]
        C, D = current_tour[j], current_tour[(j + 1) % n]
        
        d_old = mat[A][B] + mat[C][D]
        d_new = mat[A][C] + mat[B][D]
        delta = d_new - d_old
        
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_tour[i:j+1] = reversed(current_tour[i:j+1])
            current_cost += delta
            
            if current_cost < best_cost:
                best_cost = current_cost
                best_tour = current_tour.copy()
                
        iteration += 1

    print(f"\nTime's up! Total Iterations: {iteration:,}")
    return best_tour, best_cost

if __name__ == '__main__':
    random.seed(42)
    
    ids, x_coords, y_coords = load_data(FILE_NAME)
    
    if ids is not None:
        print(f"Total of {len(ids)} cities loaded.")
        dist_mat = calc_matrix(x_coords, y_coords)
        
        best_tour, final_cost = simulated_annealing(dist_mat)
        
        print("\n" + "="*50)
        print(f"SHORTEST ROUTE DISTANCE (Pure SA): {final_cost:.2f} km")
        print("CITY SEQUENCE (ID):")
        
        route_ids = [str(ids[i]) for i in best_tour]
        route_ids.append(str(ids[best_tour[0]]))
        
        print(" -> ".join(route_ids))
        print("="*50 + "\n")