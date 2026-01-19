import os

# --- KONFIGURASI ---
# 1. Atur path ke direktori dataset utama Anda
# (Saya mengambil path ini dari notebook Anda sebelumnya)
DATASET_ROOT = "audio_data_processed"

# 2. Atur nama file yang ingin dihapus
FILE_TO_DELETE = "001001.mp3"
# ---------------------

print(f"Starting deletion script...")
print(f"Target file: {FILE_TO_DELETE}")
print(f"Root directory: {DATASET_ROOT}\n")

# Pastikan direktori root ada
if not os.path.exists(DATASET_ROOT):
    print(f"ERROR: Root directory not found. Please check the path.")
    print("Script aborted.")
else:
    deleted_count = 0
    checked_folders = 0
    
    # Loop melalui setiap item (folder qari) di dalam DATASET_ROOT
    for reciter_folder in os.listdir(DATASET_ROOT):
        reciter_path = os.path.join(DATASET_ROOT, reciter_folder)
        
        # Pastikan itu adalah sebuah direktori
        if os.path.isdir(reciter_path):
            checked_folders += 1
            # Buat path lengkap ke file yang ditargetkan
            target_file_path = os.path.join(reciter_path, FILE_TO_DELETE)
            
            # Periksa apakah file tersebut ada
            if os.path.exists(target_file_path):
                try:
                    # Coba hapus file
                    os.remove(target_file_path)
                    print(f"[DELETED] {target_file_path}")
                    deleted_count += 1
                except OSError as e:
                    print(f"[ERROR] Failed to delete {target_file_path}: {e}")
            # else:
            #     # Opsional: Uncomment baris ini jika Anda ingin melihat folder yang TIDAK memiliki file tsb
            #     print(f"[Not Found] in {reciter_folder}")
                    
    print(f"\n--- Script Finished ---")
    print(f"Checked {checked_folders} folders.")
    print(f"Deleted {deleted_count} file(s) named '{FILE_TO_DELETE}'.")