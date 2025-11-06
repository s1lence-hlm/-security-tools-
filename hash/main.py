#!/usr/bin/env python3
"""
Hash Analyzer - Herramienta de análisis de hashes criptográficos
"""

import argparse
import sys
from src.hash_calculator import HashCalculator
from src.hash_identifier import HashIdentifier
from src.hash_comparator import HashComparator
from src.performance_analyzer import PerformanceAnalyzer
from src.utils.color_output import ColorOutput

def main():
    parser = argparse.ArgumentParser(description='Hash Analyzer - Analizador de Hashes Criptográficos')
    parser.add_argument('input', help='Texto o ruta de archivo para analizar')
    
    # Modos de operación
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--calculate', action='store_true', help='Calcular hashes')
    group.add_argument('-i', '--identify', help='Identificar tipo de hash')
    group.add_argument('-v', '--verify', nargs=2, help='Verificar hash (archivo hash_esperado)')
    group.add_argument('-b', '--benchmark', action='store_true', help='Benchmark de algoritmos')
    
    # Opciones adicionales
    parser.add_argument('-a', '--algorithm', help='Algoritmo específico a usar')
    parser.add_argument('--list-algorithms', action='store_true', help='Listar algoritmos disponibles')
    parser.add_argument('-o', '--output', help='Archivo de salida')
    
    args = parser.parse_args()
    color = ColorOutput()
    
    try:
        if args.list_algorithms:
            list_algorithms()
        elif args.identify:
            identify_hash(args.identify)
        elif args.verify:
            verify_hash(args.verify[0], args.verify[1])
        elif args.benchmark:
            run_benchmark(args.input)
        else:
            calculate_hashes(args.input, args.algorithm, args.output)
    except Exception as e:
        color.print_error(f"Error: {e}")
        sys.exit(1)

def calculate_hashes(input_data, algorithm=None, output_file=None):
    """Calcular hashes del input"""
    calculator = HashCalculator()
    color = ColorOutput()
    
    color.print_header("🔐 CALCULANDO HASHES")
    color.print_info(f"Input: {input_data}")
    
    results = calculator.calculate_all_hashes(input_data, algorithm)
    
    # Mostrar resultados
    for algo, hash_value in results.items():
        color.print_success(f"{algo:>12}: {hash_value}")
    
    if output_file:
        calculator.save_to_file(results, output_file)
        color.print_info(f"Resultados guardados en: {output_file}")

def identify_hash(hash_string):
    """Identificar tipo de hash"""
    identifier = HashIdentifier()
    color = ColorOutput()
    
    color.print_header("🔍 IDENTIFICANDO HASH")
    color.print_info(f"Hash: {hash_string}")
    
    possibilities = identifier.identify(hash_string)
    
    if possibilities:
        color.print_success("Posibles algoritmos:")
        for algo, confidence in possibilities:
            color.print_info(f"  • {algo} (confianza: {confidence}%)")
    else:
        color.print_warning("No se pudo identificar el algoritmo")

def verify_hash(file_path, expected_hash):
    """Verificar integridad de archivo"""
    comparator = HashComparator()
    color = ColorOutput()
    
    color.print_header("✅ VERIFICANDO INTEGRIDAD")
    color.print_info(f"Archivo: {file_path}")
    color.print_info(f"Hash esperado: {expected_hash}")
    
    result = comparator.verify_file_integrity(file_path, expected_hash)
    
    if result['match']:
        color.print_success("✓ INTEGRIDAD VERIFICADA")
        color.print_info(f"Algoritmo: {result['algorithm']}")
        color.print_info(f"Hash calculado: {result['calculated_hash']}")
    else:
        color.print_error("✗ INTEGRIDAD COMPROMETIDA")
        if result['algorithm']:
            color.print_warning(f"Algoritmo: {result['algorithm']}")
            color.print_warning(f"Hash calculado: {result['calculated_hash']}")

def run_benchmark(input_data):
    """Ejecutar benchmark de rendimiento"""
    analyzer = PerformanceAnalyzer()
    color = ColorOutput()
    
    color.print_header("⚡ BENCHMARK DE ALGORITMOS")
    
    results = analyzer.benchmark_algorithms(input_data)
    analyzer.display_results(results)

def list_algorithms():
    """Listar algoritmos disponibles"""
    calculator = HashCalculator()
    color = ColorOutput()
    
    color.print_header("📚 ALGORITMOS DISPONIBLES")
    
    algorithms = calculator.get_available_algorithms()
    for category, algo_list in algorithms.items():
        color.print_info(f"\n{category}:")
        for algo in algo_list:
            color.print_success(f"  • {algo}")

if __name__ == "__main__":
    main()