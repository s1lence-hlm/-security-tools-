from .hash_calculator import HashCalculator
from .hash_identifier import HashIdentifier

class HashComparator:
    def __init__(self):
        self.calculator = HashCalculator()
        self.identifier = HashIdentifier()
    
    def verify_file_integrity(self, file_path, expected_hash):
        """Verificar integridad de archivo"""
        # Primero identificar el algoritmo
        possibilities = self.identifier.identify(expected_hash)
        
        if not possibilities:
            return {
                'match': False,
                'algorithm': None,
                'calculated_hash': None,
                'error': 'No se pudo identificar el algoritmo del hash proporcionado'
            }
        
        # Usar el algoritmo más probable
        most_likely_algorithm = possibilities[0][0]
        
        try:
            calculated_hash = self.calculator.calculate_hash(file_path, most_likely_algorithm)
            
            return {
                'match': calculated_hash.lower() == expected_hash.lower(),
                'algorithm': most_likely_algorithm,
                'calculated_hash': calculated_hash,
                'expected_hash': expected_hash
            }
        except Exception as e:
            return {
                'match': False,
                'algorithm': most_likely_algorithm,
                'calculated_hash': None,
                'error': str(e)
            }
    
    def compare_hashes(self, hash1, hash2):
        """Comparar dos hashes directamente"""
        return hash1.lower() == hash2.lower()
    
    def find_collisions(self, data_list, algorithm='MD5'):
        """Buscar colisiones en una lista de datos"""
        hashes = {}
        collisions = []
        
        for data in data_list:
            hash_value = self.calculator.calculate_hash(data, algorithm)
            
            if hash_value in hashes:
                collisions.append({
                    'hash': hash_value,
                    'data1': hashes[hash_value],
                    'data2': data
                })
            else:
                hashes[hash_value] = data
        
        return collisions