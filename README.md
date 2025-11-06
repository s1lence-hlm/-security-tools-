# 🔐 **Hash Analyzer - Documentación Completa de Uso**

*`Clasificación: INFORMACIÓN PÚBLICA - USO LIBRE`*  
*`Versión: 1.0.0`*  
*`Última actualización: ${current_date}`*

## 📋 **TABLA DE CONTENIDOS**

1. [Descripción General](#descripción-general)
2. [Instalación y Configuración](#instalación-y-configuración)
3. [Modos de Operación](#modos-de-operación)
4. [Sintaxis Completa](#sintaxis-completa)
5. [Ejemplos Detallados](#ejemplos-detallados)
6. [Códigos de Salida](#códigos-de-salida)
7. [Formatos de Salida](#formatos-de-salida)
8. [Referencia de Algoritmos](#referencia-de-algoritmos)

---

## 🎯 **DESCRIPCIÓN GENERAL**

### **Propósito**
El **Hash Analyzer** es una herramienta de línea de comandos diseñada para el análisis criptográfico de funciones hash. Proporciona capacidades de cálculo, identificación, verificación y benchmarking de algoritmos hash.

### **Características Principales**
- ✅ Cálculo múltiple de hashes
- 🔍 Identificación automática de algoritmos
- 📊 Benchmark de rendimiento
- 🔒 Verificación de integridad
- 🎨 Salida coloreada y formateada
- 💾 Exportación de resultados

---

## ⚙️ **INSTALACIÓN Y CONFIGURACIÓN**

### **Requisitos del Sistema**
```bash
# Sistema Operativo
✔️ Windows 10/11
✔️ Linux (Ubuntu 18.04+, CentOS 7+)
✔️ macOS 10.14+

# Python
✔️ Python 3.8 o superior
✔️ pip (gestor de paquetes)
```

### **Instalación desde Código Fuente**
```bash
# 1. Clonar repositorio
git clone https://github.com/s1lence-hlm/hash-analyzer.git
cd hash-analyzer

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Instalar en modo desarrollo
pip install -e .

# 4. Verificar instalación
hash-analyzer --version
```

### **Instalación Global**
```bash
# Instalar directamente desde PyPI (cuando esté disponible)
pip install hash-analyzer

# Verificar instalación
hash-analyzer --help
```

---

## 🕹️ **MODOS DE OPERACIÓN**

### **Resumen de Modos**
| **Modo** | **Comando** | **Descripción** |
|----------|-------------|-----------------|
| `Cálculo` | `--calculate` | Calcular hashes de entrada |
| `Identificación` | `--identify` | Identificar algoritmo de hash |
| `Verificación` | `--verify` | Verificar integridad de archivos |
| `Benchmark` | `--benchmark` | Test de rendimiento de algoritmos |
| `Listado` | `--list-algorithms` | Mostrar algoritmos disponibles |

---

## 🛠️ **SINTAXIS COMPLETA**

### **Estructura Base del Comando**
```bash
hash-analyzer [OPCIONES] [ENTRADA]
hash-analyzer [MODO] [ARGUMENTOS] [OPCIONES]
```

### **Parámetros Principales**
| **Parámetro** | **Tipo** | **Requerido** | **Descripción** |
|---------------|----------|---------------|-----------------|
| `ENTRADA` | string | Condicional | Texto o ruta de archivo a procesar |
| `MODO` | flag | Opcional | Modo de operación específico |

### **Opciones de Modo**
| **Opción** | **Forma Larga** | **Argumentos** | **Descripción** |
|------------|-----------------|----------------|-----------------|
| `-c` | `--calculate` | Ninguno | Modo cálculo de hashes |
| `-i` | `--identify` | HASH | Identificar algoritmo |
| `-v` | `--verify` | ARCHIVO HASH | Verificar integridad |
| `-b` | `--benchmark` | Ninguno | Benchmark de algoritmos |
| `-l` | `--list-algorithms` | Ninguno | Listar algoritmos |

### **Opciones Adicionales**
| **Opción** | **Forma Larga** | **Argumentos** | **Descripción** |
|------------|-----------------|----------------|-----------------|
| `-a` | `--algorithm` | ALGORITMO | Algoritmo específico |
| `-o` | `--output` | ARCHIVO | Guardar resultados |
| `--no-color` | `--no-color` | Ninguno | Deshabilitar colores |
| `--version` | `--version` | Ninguno | Mostrar versión |
| `-h` | `--help` | Ninguno | Mostrar ayuda |

---

## 📚 **EJEMPLOS DETALLADOS**

### **1. 🧮 MODO CÁLCULO - Ejemplos Completos**

#### **1.1. Cálculo Básico de Texto**
```bash
# Calcular todos los hashes de un texto
hash-analyzer "texto de prueba" --calculate

# Salida esperada:
🔐 CALCULANDO HASHES
ℹ Input: texto de prueba
✓         MD5: 1a79a4d60de6718e8e5b326e338ae533
✓        SHA1: 7b52009b64fd0a2a49e6d8a939753077792b0554
✓      SHA256: 6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090
✓      SHA512: 4b7b... [truncado]
```

#### **1.2. Cálculo con Algoritmo Específico**
```bash
# Calcular solo SHA256
hash-analyzer "datos sensibles" --algorithm SHA256

# Calcular múltiples algoritmos específicos
hash-analyzer "archivo.txt" -a SHA256 -a SHA512 --calculate
```

#### **1.3. Cálculo de Archivos**
```bash
# Calcular hash de un archivo
hash-analyzer documento.pdf --calculate

# Calcular con algoritmo específico para archivo
hash-analyzer imagen.jpg --algorithm MD5 --calculate
```

#### **1.4. Cálculo con Exportación**
```bash
# Calcular y guardar en archivo
hash-analyzer "texto importante" --calculate --output resultados.txt

# Ver contenido del archivo de salida
cat resultados.txt
```

### **2. 🔍 MODO IDENTIFICACIÓN - Ejemplos Completos**

#### **2.1. Identificación Básica**
```bash
# Identificar algoritmo de hash
hash-analyzer --identify "5d41402abc4b2a76b9719d911017c592"

# Salida esperada:
🔍 IDENTIFICANDO HASH
ℹ Hash: 5d41402abc4b2a76b9719d911017c592
✓ Posibles algoritmos:
  • MD5 (confianza: 100%)
  • CRC32 (confianza: 40%)
```

#### **2.2. Identificación de Hashes Complejos**
```bash
# Hash SHA256
hash-analyzer --identify "6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090"

# Hash SHA512
hash-analyzer --identify "ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff"
```

### **3. ✅ MODO VERIFICACIÓN - Ejemplos Completos**

#### **3.1. Verificación de Integridad Básica**
```bash
# Verificar archivo con hash esperado
hash-analyzer --verify archivo.zip "a1b2c3d4e5f67890123456789012345678901234"

# Salida exitosa:
✅ VERIFICANDO INTEGRIDAD
ℹ Archivo: archivo.zip
ℹ Hash esperado: a1b2c3d4e5f67890123456789012345678901234
✓ INTEGRIDAD VERIFICADA
ℹ Algoritmo: SHA1
ℹ Hash calculado: a1b2c3d4e5f67890123456789012345678901234
```

#### **3.2. Verificación con Hash Incorrecto**
```bash
# Verificación fallida
hash-analyzer --verify script.py "hash_incorrecto_12345"

# Salida de error:
✅ VERIFICANDO INTEGRIDAD
ℹ Archivo: script.py
ℹ Hash esperado: hash_incorrecto_12345
✗ INTEGRIDAD COMPROMETIDA
⚠ Algoritmo: SHA256
⚠ Hash calculado: 6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090
```

### **4. ⚡ MODO BENCHMARK - Ejemplos Completos**

#### **4.1. Benchmark Básico**
```bash
# Benchmark con texto de prueba
hash-analyzer "datos de prueba para benchmark" --benchmark

# Salida esperada:
⚡ BENCHMARK DE ALGORITMOS
======================= ⚡ BENCHMARK RESULTS =======================

✓        MD5:   0.0456 ms/op |   21930 ops/sec
✓       SHA1:   0.0567 ms/op |   17637 ops/sec
✓     SHA256:   0.0789 ms/op |   12674 ops/sec
✓     SHA512:   0.1234 ms/op |    8104 ops/sec
```

#### **4.2. Benchmark con Archivo Grande**
```bash
# Benchmark usando archivo como entrada
hash-analyzer archivo_grande.iso --benchmark
```

### **5. 📚 MODO INFORMATIVO - Ejemplos Completos**

#### **5.1. Listar Algoritmos Disponibles**
```bash
# Mostrar todos los algoritmos soportados
hash-analyzer --list-algorithms

# Salida esperada:
📚 ALGORITMOS DISPONIBLES

MD:
  • MD5

SHA-2:
  • SHA224
  • SHA256
  • SHA384
  • SHA512

SHA-3:
  • SHA3-224
  • SHA3-256
  • SHA3-384
  • SHA3-512

BLAKE2:
  • BLAKE2b
  • BLAKE2s
```

#### **5.2. Mostrar Ayuda Completa**
```bash
# Ayuda general
hash-analyzer --help

# Ayuda específica de modos
hash-analyzer --calculate --help
```

---

## 🎨 **OPCIONES AVANZADAS**

### **Salida Sin Colores**
```bash
# Para scripts o entornos sin soporte de color
hash-analyzer "texto" --calculate --no-color

# Variable de entorno
export NO_COLOR=1
hash-analyzer "texto" --calculate
```

### **Modo Silencioso para Scripts**
```bash
# Redirigir salida estándar
hash-analyzer archivo.txt --algorithm SHA256 --calculate > hash_resultado.txt

# Solo el hash (para uso en scripts)
hash-analyzer "texto" --algorithm MD5 --calculate | grep "MD5" | awk '{print $2}'
```

### **Múltiples Entradas por Lote**
```bash
# Procesar múltiples archivos
for file in *.txt; do
    echo "=== $file ==="
    hash-analyzer "$file" --algorithm SHA256 --calculate
done
```

---

## 📊 **CÓDIGOS DE SALIDA**

| **Código** | **Significado** | **Descripción** |
|------------|-----------------|-----------------|
| `0` | `EXIT_SUCCESS` | Ejecución exitosa |
| `1` | `EXIT_FAILURE` | Error general |
| `2` | `INVALID_ARGUMENT` | Argumentos inválidos |
| `3` | `FILE_NOT_FOUND` | Archivo no encontrado |
| `4` | `HASH_MISMATCH` | Hash no coincide (verificación) |
| `5` | `UNKNOWN_ALGORITHM` | Algoritmo no soportado |

### **Ejemplos en Scripts**
```bash
#!/bin/bash

# Verificar integridad y actuar según resultado
hash-analyzer --verify backup.tar.gz "$EXPECTED_HASH"

case $? in
    0) echo "Integridad confirmada - Proceder con instalación" ;;
    4) echo "ERROR: Archivo corrupto - Abortar" ;;
    *) echo "Error inesperado - Revisar logs" ;;
esac
```

---

## 💾 **FORMATOS DE SALIDA**

### **Salida Estándar (Consola)**
```text
Formato coloreado con emojis y formato legible
```

### **Salida a Archivo**
```text
Hash Analysis Results
==================================================
        MD5: d41d8cd98f00b204e9800998ecf8427e
       SHA1: da39a3ee5e6b4b0d3255bfef95601890afd80709
     SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

### **Formato JSON (Futura Implementación)**
```json
{
  "input": "texto de prueba",
  "results": {
    "MD5": "1a79a4d60de6718e8e5b326e338ae533",
    "SHA256": "6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090"
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

---

## 🔐 **REFERENCIA DE ALGORITMOS**

### **Algoritmos Soportados**

| **Algoritmo** | **Longitud** | **Seguridad** | **Uso Recomendado** |
|---------------|--------------|---------------|---------------------|
| `MD5` | 128 bits | ❌ Obsoleto | Checksums no críticos |
| `SHA1` | 160 bits | ⚠️ Débil | Compatibilidad legacy |
| `SHA256` | 256 bits | ✅ Seguro | Uso general |
| `SHA512` | 512 bits | ✅ Muy Seguro | Alta seguridad |
| `SHA3-256` | 256 bits | ✅ Seguro | Aplicaciones modernas |
| `BLAKE2b` | 512 bits | ✅ Seguro | Alto rendimiento |

### **Recomendaciones por Caso de Uso**

#### **Integridad de Archivos**
```bash
# Para verificación rápida (no seguridad)
hash-analyzer archivo.iso --algorithm MD5

# Para seguridad básica
hash-analyzer documento.pdf --algorithm SHA256

# Para máxima seguridad
hash-analyzer contrato.txt --algorithm SHA3-512
```

#### **Contraseñas (con salt)**
```bash
# NO USAR directamente para contraseñas
# Usar funciones de derivación como PBKDF2, bcrypt
```

---

## 🚨 **MEJORES PRÁCTICAS**

### **Seguridad**
```bash
# ✅ Correcto - Verificar con algoritmos seguros
hash-analyzer --verify firmware.bin "$SHA256_HASH"

# ❌ Evitar - Usar MD5 para seguridad
hash-analyzer --verify contraseñas.txt "$MD5_HASH"
```

### **Rendimiento**
```bash
# Para archivos grandes, usar algoritmos más eficientes
hash-analyzer video_4k.mp4 --algorithm BLAKE2b --calculate

# Benchmark previo para elegir algoritmo óptimo
hash-analyzer "tu_dato" --benchmark
```

### **Scripting y Automatización**
```bash
#!/bin/bash
# Ejemplo de implementación en scripts

FILE="$1"
EXPECTED_HASH="$2"

# Verificar integridad
if hash-analyzer --verify "$FILE" "$EXPECTED_HASH"; then
    echo "✅ Verificación exitosa"
    # Continuar con procesamiento
else
    echo "❌ Error de integridad"
    exit 1
fi
```

---

## 🔄 **ACTUALIZACIONES Y MANTENIMIENTO**

### **Verificar Versión**
```bash
hash-analyzer --version
```

### **Actualizar Herramienta**
```bash
# Desde PyPI
pip install --upgrade hash-analyzer

# Desde código fuente
git pull origin main
pip install --upgrade -r requirements.txt
```

---

## 📞 **SOPORTE Y SOLUCIÓN DE PROBLEMAS**

### **Problemas Comunes**
```bash
# Error: Archivo no encontrado
hash-analyzer archivo_inexistente.txt --calculate

# Solución: Verificar ruta
ls -la archivo_inexistente.txt

# Error: Algoritmo no soportado  
hash-analyzer "texto" --algorithm INVALID_ALGO --calculate

# Solución: Listar algoritmos disponibles
hash-analyzer --list-algorithms
```

### **Modo Debug**
```bash
# Habilitar logs detallados
export HASH_ANALYZER_DEBUG=1
hash-analyzer "test" --calculate

# Limpiar cache (si es necesario)
rm -rf __pycache__/ src/__pycache__/
```

---

**`DOCUMENTO CLASIFICADO COMO: INFORMACIÓN OPERATIVA COMPLETA`**  
**`DISTRIBUCIÓN AUTORIZADA: USUARIOS REGISTRADOS`**  
**`VIGENCIA: INDEFINIDA (Sujeta a actualizaciones)`**

---
*Documentación generada automáticamente por el sistema Hash Analyzer v1.0.0*  
*Mantenido por: s1lence | Cybersecurity Engineering Student*  
*Última verificación: ${current_date}*
