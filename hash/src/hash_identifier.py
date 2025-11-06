import re

class HashIdentifier:
    def __init__(self):
        # Patrones de hash con sus longitudes y ejemplos
        self.hash_patterns = {
            'MD5': {
                'length': 32,
                'pattern': r'^[a-fA-F0-9]{32}$',
                'examples': ['5d41402abc4b2a76b9719d911017c592']
            },
            'SHA1': {
                'length': 40,
                'pattern': r'^[a-fA-F0-9]{40}$',
                'examples': ['aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d']
            },
            'SHA256': {
                'length': 64,
                'pattern': r'^[a-fA-F0-9]{64}$',
                'examples': ['2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824']
            },
            'SHA512': {
                'length': 128,
                'pattern': r'^[a-fA-F0-9]{128}$',
                'examples': ['9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043']
            },
            'BLAKE2b': {
                'length': 128,
                'pattern': r'^[a-fA-F0-9]{128}$',
                'examples': []
            },
            'BLAKE2s': {
                'length': 64,
                'pattern': r'^[a-fA-F0-9]{64}$',
                'examples': []
            }
        }
    
    def identify(self, hash_string):
        """Identificar el tipo de hash"""
        hash_string = hash_string.strip()
        possibilities = []
        
        for algo_name, algo_info in self.hash_patterns.items():
            confidence = self._calculate_confidence(hash_string, algo_info)
            if confidence > 0:
                possibilities.append((algo_name, confidence))
        
        # Ordenar por confianza
        possibilities.sort(key=lambda x: x[1], reverse=True)
        return possibilities
    
    def _calculate_confidence(self, hash_string, algo_info):
        """Calcular confianza de identificación"""
        confidence = 0
        
        # Verificar longitud
        if len(hash_string) == algo_info['length']:
            confidence += 60
        
        # Verificar patrón hexadecimal
        if re.match(algo_info['pattern'], hash_string):
            confidence += 40
        
        return confidence
    
    def get_hash_info(self, algorithm):
        """Obtener información detallada de un algoritmo"""
        if algorithm in self.hash_patterns:
            info = self.hash_patterns[algorithm].copy()
            info['security_status'] = self._get_security_status(algorithm)
            return info
        return None
    
    def _get_security_status(self, algorithm):
        """Estado de seguridad del algoritmo"""
        security_status = {
            'MD5': 'INSECURE - Solo para checksums',
            'SHA1': 'WEAK - No usar para seguridad',
            'SHA256': 'SECURE - Recomendado',
            'SHA512': 'SECURE - Alta seguridad',
            'BLAKE2b': 'SECURE - Moderno y rápido',
            'BLAKE2s': 'SECURE - Para entornos limitados'
        }
        return security_status.get(algorithm, 'Desconocido')