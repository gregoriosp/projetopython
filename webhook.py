#!/usr/bin/env python3
import os
import subprocess
import sys

def main():
    # Obtendo a lista de arquivos modificados
    result = subprocess.run(
        ['git', 'diff', '--cached', '--name-only', '--diff-filter=ACM'], 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE
    )

    if result.returncode != 0:
        print("Erro ao obter arquivos modificados.")
        sys.exit(1)

    files = result.stdout.decode().strip().split('\n')
    python_files = [f for f in files if f.endswith('.py')]

    if not python_files:
        print("Nenhum arquivo Python modificado.")
        return 0

    print("Verificando formatação dos arquivos Python...")
    black_result = subprocess.run(['black', '--check'] + python_files)

    if black_result.returncode != 0:
        print("Alguns arquivos não estão formatados corretamente. Por favor, formate-os usando 'black'.")
        return 1

    print("Todos os arquivos Python estão formatados corretamente.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
