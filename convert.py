import os
from PIL import Image

def convert_png_to_pdf(source_folder, destination_folder):
    # Duyệt qua toàn bộ cấu trúc thư mục
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            if filename.endswith(".png"):
                # Đường dẫn đầy đủ tới tệp PNG
                png_path = os.path.join(root, filename)
                
                # Tạo cấu trúc thư mục tương ứng trong thư mục đích
                relative_path = os.path.relpath(root, source_folder)
                pdf_folder = os.path.join(destination_folder, relative_path)
                if not os.path.exists(pdf_folder):
                    os.makedirs(pdf_folder)
                
                # Đường dẫn đầy đủ tới tệp PDF
                pdf_path = os.path.join(pdf_folder, filename.replace(".png", ".pdf"))
                
                # Mở tệp PNG và chuyển đổi sang PDF
                image = Image.open(png_path)
                
                # Check if the image has an alpha channel
                if image.mode == 'RGBA':
                    rgb_image = Image.new('RGB', image.size, (255, 255, 255))  # White background
                    rgb_image.paste(image, mask=image.split()[3])  # Paste using alpha channel as mask
                    rgb_image.save(pdf_path, "PDF", resolution=100.0)
                else:
                    image.convert('RGB').save(pdf_path, "PDF", resolution=100.0)
                
                print(f"Đã chuyển đổi: {png_path} -> {pdf_path}")

# Đường dẫn tới thư mục nguồn và đích
source_folder = r"C:\Users\HI.WELCOME TO NET\Downloads\SP_S"
destination_folder = r"C:\Users\HI.WELCOME TO NET\Downloads\SPS"

# Chuyển đổi các tệp PNG sang PDF
convert_png_to_pdf(source_folder, destination_folder)