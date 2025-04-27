import argparse
import random

def read_file_input(file_path):
        with open(file_path, 'r') as file:
                lines = [line.strip() for line in file.readlines()]
        return [[char for char in line if not char.isspace()] for line in lines]

def generate_random_map(rows, cols):
        return [[random.choice(['0', 'X']) for _ in range(cols)] for _ in range(rows)]

def apply_rules(current_state, num_neighbors):
        if num_neighbors <= 1:
                return '0'  # Rule 1: Lonely cells die
        elif num_neighbors == 2:
                return current_state  # Rule 2: Stable cells remain unchanged
        elif num_neighbors == 3:
                return 'X'  # Rule 3: New cell is born or remains
        else:
                return '0'  # Rule 4: Overcrowded cells die

def detect_neighboring_X(map_data):
    neighboring_X = []
    rows = len(map_data)
    cols = len(map_data[0])

    # Create a new map for the next generation
    next_generation_map = [[cell for cell in row] for row in map_data]

    for i in range(rows):
        for j in range(cols):
            neighbors = []
            # Check neighboring cells
            for x in range(max(0, i-1), min(rows, i+2)):
                for y in range(max(0, j-1), min(cols, j+2)):
                    if (x, y) != (i, j) and map_data[x][y] == 'X':
                        neighbors.append((x, y))

            # Apply rules to update the new map for the next generation
            num_neighbors = len(neighbors)
            new_state = apply_rules(map_data[i][j], num_neighbors)
            next_generation_map[i][j] = new_state

            if new_state == 'X':
                neighboring_X.append((i, j, neighbors))

    return neighboring_X, next_generation_map



def main():
        print("Artificial Life Simulation of Game of Life")
        print("Each cell with one or no neighbors dies, as if by loneliness.")
        print("Each cell with four or more neighbors dies, as if by overpopulation.")
        print("Each cell with two or three neighbors survives.")
        print("Each cell with three neighbors becomes populated.")
        print("Each cell that ages over 10 generations dies.\n")
        num_generations = int(input("How many generations would you like to simulate? "))
    
        # Parse command-line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument("--file", "-f", type=str, help="Input file path")
        args = parser.parse_args()

        if args.file:
                # Handle file input
                map_data = read_file_input(args.file)
        else:
                # Generate a random 20x20 map
                map_data = generate_random_map(20, 20)

        # Print the initial map
        print("\n\nInitial Colony Prior to Evolution:")
        print("************************************************")
        for row in map_data:
                print(' '.join(row))

        # Detect neighboring X's and apply rules for next generation
        for generation in range(1, num_generations + 1):
                neighboring_X, map_data = detect_neighboring_X(map_data)
                print(f"\nHow Colony Has Evolved After {generation} Generation(s)")
                print("************************************************")
                for row in map_data:
                        print(' '.join(row))
                print("************************************************")

if __name__ == "__main__":
        main()

