
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Now import your module
try:
    from graphs_bonkfairy import sp
    print("Successfully imported sp module!")
except ImportError as e:
    print(f"Import error: {e}")
    print("Trying direct import...")
    # Try importing directly from the file
    import importlib.util
    spec = importlib.util.spec_from_file_location("sp", "src/graphs_bonkfairy/sp.py")
    sp_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sp_module)
    sp = sp_module

if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print(f'Use: {sys.argv[0]} graph_file')
        print("Creating a test graph instead...")
        
        # Create a simple test graph
        graph = {
            0: {1: 4, 7: 8},
            1: {0: 4, 2: 8, 7: 11},
            2: {1: 8, 3: 7, 8: 2, 5: 4},
            3: {2: 7, 4: 9, 5: 14},
            4: {3: 9, 5: 10},
            5: {2: 4, 3: 14, 4: 10, 6: 2},
            6: {5: 2, 7: 1, 8: 6},
            7: {0: 8, 1: 11, 6: 1, 8: 7},
            8: {2: 2, 6: 6, 7: 7}
        }
    else:
        graph = {}
        with open(sys.argv[1], 'rt') as f:
            f.readline() # skip first line
            for line in f:
                line = line.strip()
                s, d, w = line.split()
                s = int(s)
                d = int(d)
                w = int(w)
                if s not in graph:
                    graph[s] = {}
                graph[s][d] = w
    
    s = 0
    dist, path = sp.dijkstra(graph, s)
    print(f'Shortest distances from {s}:')
    print(dist)