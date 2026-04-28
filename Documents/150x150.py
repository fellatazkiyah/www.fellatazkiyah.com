import os
from PIL import Image

def resize_images():
    for filename in os.listdir('.'):
        if filename.lower().endswith('.jpg'):
            try:
                img = Image.open(filename)
                img_resized = img.resize((150, 150))
                img_resized.save(filename)
                print(f"--> Berhasil mengubah ukuran: {filename}")
            except Exception as e:
                print(f"--> Gagal memproses: {filename}")

if __name__ == "__main__":
    print("--> Memulai proses pengubahan ukuran gambar")
    resize_images()
    print("--> Proses selesai")
