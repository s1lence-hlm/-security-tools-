import hashlib
import os
from .utils.file_utils import FileUtils

class HashCalculator:
    def __init__(self):
        self.algorithms = {
            'MD5': hashlib.md5,
            'SHA1': hashlib.sha1,
            'SHA224': hashlib.sha224,
            'SHA256': hashlib.sha256,
            'SHA384': hashlib.sha384,
            'SHA512': hashlib.sha512,
            'SHA3-224': hashlib.sha3_224,
            'SHA3-256': hashlib.sha3_256,
            'SHA3-384': hashlib.sha3_384,
            'SHA3-512': hashlib.sha3_512,
            'BLAKE2b': hashlib.blake2b,
            'BLAKE2s': hashlib.blake2s
        }
    
    def calculate_hash(self, data, algorithm):
        """Calcular hash para datos dados"""
        if algorithm.upper() not in self.algorithms:
            raise ValueError(f"Algoritmo no soportado: {algorithm}")
        
        hash_func = self.algorithms[algorithm.upper()]
        
        if isinstance(data, str):
            if os.path.exists(data):
                # Es un archivo
                return self._calculate_file_hash(data, hash_func)
            else:
                # Es texto
                return self._calculate_string_hash(data, hash_func)
        else:
            raise ValueError("Tipo de dato no soportado")
    
    def _calculate_string_hash(self, text, hash_func):
        """Calcular hash de un string"""
        return hash_func(text.encode('utf-8')).hexdigest()
    
    def _calculate_file_hash(self, file_path, hash_func, buffer_size=65536):
        """Calcular hash de un archivo"""
        hash_obj = hash_func()
        
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(buffer_size)
                if not data:
                    break
                hash_obj.update(data)
        
        return hash_obj.hexdigest()
    
    def calculate_all_hashes(self, input_data, specific_algorithm=None):
        """Calcular todos los hashes disponibles"""
        results = {}
        algorithms_to_use = [specific_algorithm] if specific_algorithm else self.algorithms.keys()
        
        for algo_name in algorithms_to_use:
            if algo_name in self.algorithms:
                try:
                    hash_value = self.calculate_hash(input_data, algo_name)
                    results[algo_name] = hash_value
                except Exception as e:
                    results[algo_name] = f"Error: {e}"
        
        return results
    
    def get_available_algorithms(self):
        """Obtener algoritmos disponibles categorizados"""
        return {
            "MD": ["MD5"],
            "SHA-2": ["SHA224", "SHA256", "SHA384", "SHA512"],
            "SHA-3": ["SHA3-224", "SHA3-256", "SHA3-384", "SHA3-512"],
            "BLAKE2": ["BLAKE2b", "BLAKE2s"]
        }
    
    def save_to_file(self, results, filename):
        """Guardar resultados en archivo"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Hash Analysis Results\n")
            f.write("=" * 50 + "\n")
            for algo, hash_value in results.items():
                f.write(f"{algo:>12}: {hash_value}\n")