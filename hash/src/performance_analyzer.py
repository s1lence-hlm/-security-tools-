import time
import hashlib
from .hash_calculator import HashCalculator

class PerformanceAnalyzer:
    def __init__(self):
        self.calculator = HashCalculator()
    
    def benchmark_algorithms(self, input_data, iterations=1000):
        """Benchmark de rendimiento para todos los algoritmos"""
        results = {}
        
        for algo_name in self.calculator.algorithms.keys():
            try:
                total_time = 0
                
                # Calcular tiempo para 'iterations' iteraciones
                for _ in range(iterations):
                    start_time = time.time()
                    self.calculator.calculate_hash(input_data, algo_name)
                    end_time = time.time()
                    total_time += (end_time - start_time)
                
                avg_time = (total_time / iterations) * 1000  # Convertir a ms
                hashes_per_second = iterations / total_time if total_time > 0 else 0
                
                results[algo_name] = {
                    'average_time_ms': avg_time,
                    'hashes_per_second': hashes_per_second,
                    'iterations': iterations
                }
                
            except Exception as e:
                results[algo_name] = {
                    'error': str(e),
                    'average_time_ms': 0,
                    'hashes_per_second': 0
                }
        
        return results
    
    def display_results(self, results):
        """Mostrar resultados del benchmark"""
        print("\n" + "="*60)
        print("⚡ BENCHMARK RESULTS")
        print("="*60)
        
        sorted_results = sorted(
            [(algo, data) for algo, data in results.items() if 'error' not in data],
            key=lambda x: x[1]['average_time_ms']
        )
        
        for algo, data in sorted_results:
            if 'error' not in data:
                print(f"{algo:>12}: {data['average_time_ms']:8.4f} ms/op | "
                      f"{data['hashes_per_second']:8.0f} ops/sec")
        
        # Mostrar algoritmos con error
        error_algorithms = [algo for algo, data in results.items() if 'error' in data]
        if error_algorithms:
            print("\n⚠️  Algoritmos con errores:")
            for algo in error_algorithms:
                print(f"  • {algo}: {results[algo]['error']}")