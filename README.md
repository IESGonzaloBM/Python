# Calculadora binaria de 8 bits (Python) — README

> CLI que **suma** y **resta** números binarios de **1 a 8 bits**.
> **Salida exclusivamente en binario de 8 bits** (relleno con ceros a la izquierda).
> Si no se indica signo, el programa ejecuta **ambas operaciones** (suma y resta).

---

## 1) Descripción del módulo

Este proyecto implementa una **calculadora binaria de 8 bits** que opera con **enteros sin signo**.
- Los **operandos** se introducen como **cadenas binarias** de **1 a 8 bits** (`0`/`1`).
- La **operación** se define por **signo**: `+` (suma) o `-` (resta).
- Si **no** se especifica el signo, el programa **realiza ambas operaciones** con los mismos operandos y muestra **dos bloques** de salida.
- Antes de calcular, cada operando se **rellena a 8 bits** para el cálculo/visualización.



---

## 2) Requisitos

- **Python 3.10 o superior**.
- **Sin dependencias externas obligatorias.**
- Si en algún momento se añaden librerías, se listarán en el archivo **`dependecias.txt`** (ver sección 5).

---

## 3) Instalación de Python

### 3.1 Linux

#### Debian/Ubuntu (y derivados)
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
python3 --version
python3 -m pip --version
```

#### Fedora
```bash
sudo dnf install -y python3 python3-pip python3-virtualenv
python3 --version
python3 -m pip --version
```

#### Arch/Manjaro
```bash
sudo pacman -S --needed python python-pip
python --version
python -m pip --version
```

> **Entorno virtual (opcional recomendado)**
```bash
python3 -m venv .venv
# Activar:
# Linux/macOS:
source .venv/bin/activate
# (Salir: 'deactivate')
```

### 3.2 Windows

#### Opción A — Microsoft Store
1. Abrir **Microsoft Store**, buscar **Python 3.x** (Python Software Foundation).
2. Instalar y verificar:
```powershell
py --version
py -m pip --version
```

#### Opción B — Instalador oficial
1. Descargar desde **https://www.python.org/downloads/** el instalador de Python 3.x.
2. **Marcar** “**Add Python to PATH**” durante la instalación.
3. Verificar:
```powershell
py --version
py -m pip --version
```

> **Entorno virtual (opcional)**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
# (Salir: 'deactivate')
```

---

## 4) Ejecución del módulo

### Sintaxis general
```bash
python nombre_modulo.py OPERANDO1 [SIGNO] OPERANDO2
```
- `OPERANDO1` y `OPERANDO2`: binarios de **1 a 8 bits** (`^[01]{1,8}$`).
- `SIGNO` (opcional): `+` para **suma**, `-` para **resta**.
- Si **omites el signo**, el programa realiza **suma y resta** y muestra **dos bloques** de salida.

> En Windows puedes usar `py` en lugar de `python`.
> En Linux, si conviven varias versiones, usa `python3`.

### Ejemplos

**Suma explícita**
```bash
# Linux/macOS
python nombre_modulo.py 1010 + 11

# Windows
py nombre_modulo.py 1010 + 11
```
Salida esperada:
```
00001010
+ 00000011
= 00001101
```

**Resta explícita**
```bash
python nombre_modulo.py 10000000 - 1
```
Salida esperada:
```
10000000
- 00000001
= 01111111
```

**Sin signo (ejecuta ambas)**
```bash
python nombre_modulo.py 11111111 1
```
Salida esperada:
```
11111111
+ 00000001
= 00000000

11111111
- 00000001
= 11111110
```

>
---

## 5) Dependencias con `dependecias.txt` (opcional)

El archivo **`dependecias.txt`** lista, una por línea, las librerías Python que requiere el proyecto (si las hubiera).
Ejemplo de contenido:
```txt
# Ejemplos
colorama==0.4.6
rich>=13.0
pytest
```

### Instalación de dependencias
> Usa el intérprete para invocar `pip` y evitar confusiones con `pip`/`pip3`.
```bash
# Linux/macOS
python3 -m pip install -r dependecias.txt

# Windows (PowerShell/CMD)
py -m pip install -r dependecias.txt
```

Si el archivo **no existe** o **está vacío**, el proyecto **no requiere** dependencias externas.

---



## 6) Mensajes de error y códigos de salida

- **Operando inválido** (no binario o > 8 bits)
- Mensaje: `ERROR: Operando no binario (1–8 bits).` →
- **Signo/operación inválida** (distinta de `+` o `-`)
- Mensaje: `ERROR: Operación no soportada (usa + o -).` →


---

## 7) Problemas frecuentes (FAQ)

- **“python: command not found” / “py no se reconoce”** → Instala Python o ajusta el **PATH** (ver sección 3).
- **“pip no se reconoce”** → Usa `python -m pip` (o `py -m pip` en Windows).
- **Formato de operando incorrecto** → Revisa que sean solo `0`/`1` y longitud ≤ 8.
- **Signo en posición incorrecta** → Asegúrate de usar `OPERANDO1 [SIGNO] OPERANDO2`.

---