#!/usr/bin/env python3
"""
Main script untuk analisis harga beras Indonesia
Run: python main.py
"""

import subprocess
import sys
import os

def run_script(script_name):
    """Jalankan script dan tampilkan hasilnya"""
    print(f"\n{'='*60}")
    print(f"Menjalankan {script_name}...")
    print(f"{'='*60}")

    try:
        result = subprocess.run([sys.executable, script_name],
                              capture_output=True, text=True, encoding='utf-8')

        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"Error: {result.stderr}")

    except Exception as e:
        print(f"Error menjalankan {script_name}: {e}")

def main():
    print("ANALISIS HARGA BERAS INDONESIA")
    print("=" * 60)
    print("Pilih opsi:")
    print("1. Analisis data saja")
    print("2. Buat visualisasi saja")
    print("3. Analisis + Visualisasi (rekomendasi)")
    print("4. Keluar")

    try:
        choice = input("\nMasukkan pilihan (1-4): ").strip()

        if choice == '1':
            run_script('analisis_data.py')
        elif choice == '2':
            run_script('visualisasi_data.py')
        elif choice == '3':
            print("\n[*] Menjalankan analisis data terlebih dahulu...")
            run_script('analisis_data.py')
            print("\n[*] Membuat visualisasi...")
            run_script('visualisasi_data.py')
        elif choice == '4':
            print("[*] Sampai jumpa!")
        else:
            print("[ERROR] Pilihan tidak valid!")

    except KeyboardInterrupt:
        print("\n\n[*] Program dibatalkan.")
    except Exception as e:
        print(f"\n[ERROR] {e}")

if __name__ == "__main__":
    main()