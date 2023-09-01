# TachCau
tool tach cau
B1: Xử lý các file pdf thành file docx:
Sử dụng các tool có sẵn trên mạng để convert ví dụ: https://smallpdf.com/pdf-to-word

B2: Cài đặt các thư viện đã được đề cập ở trên
pip install doc2txt python-docx nltk langdetect
Đối với thư viện nltk cần cài thêm gói punkt: nltk.download('punkt')

B3: Các file đầu vào cần được đặt chung thư mục với file main.py

B4: Chạy các version:
Verion 1: Cặp EN-VN thông thường: Các argument --input_file1, --input_file2.
input_vi.docx và input_en.docx là hai file đầu vào
python main.py version1 --input_file1 input_vi.docx --input_file2 input_en.docx
Version 2: Văn bản song ngữ trong cùng 1 file: Argument: --input_file. input_v2.docx là file đầu vào 
python main.py version2 --input_file input_v2.docx
