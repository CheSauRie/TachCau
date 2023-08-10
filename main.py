import docx2txt
import argparse
from docx import Document
from nltk.tokenize import sent_tokenize
from langdetect import detect

def extract_sentences_from_plain_files(input_file1, input_file2, output_file1, output_file2):
    text1 = docx2txt.process(input_file1)
    text2 = docx2txt.process(input_file2)
    sentences1 = sent_tokenize(text1.replace("\n\n\n\n", " ").replace("\n\n\t", "! ").replace("\n\n", "! ")
                               .replace("\t", "! "))
    sentences2 = sent_tokenize(text2.replace("\n\n\n\n", " ").replace("\n\n\t", "! ").replace("\n\n", "! ")
                               .replace("\t", "! "))
    with open(output_file1, 'w', encoding='utf-8') as file1, open(output_file2, 'w', encoding='utf-8') as file2:
        for sentence in sentences1:
            file1.write(sentence + '\n')
        for sentence in sentences2:
            file2.write(sentence + '\n')
    with open(output_file1, 'r', encoding='utf-8') as file1, open(output_file2, 'r', encoding='utf-8') as file2:
        content1 = file1.read()
        content2 = file2.read()
    content1_with_spaces = content1.replace('!', ' ')
    content2_with_spaces = content2.replace('!', ' ')
    with open(output_file1, 'w', encoding='utf-8') as file1, open(output_file2, 'w', encoding='utf-8') as file2:
        file1.write(content1_with_spaces)
        file2.write(content2_with_spaces)

def is_heading(para):
    # Kiểm tra xem đoạn văn bản có phải là tiêu đề không
    return para.style.name.startswith('Heading')
def process_heading(heading):
    # Chuyển các dấu / thành dấu . trong tiêu đề
    return heading.replace('/', '. ')
def extract_sentences_from_translated_file(input_file, output_file_en, output_file_vi):
    doc = Document(input_file)
    content = []  # Lưu trữ nội dung của tệp

    for paragraph in doc.paragraphs:
        if is_heading(paragraph):
            heading_text = paragraph.text
            processed_heading = process_heading(heading_text)
            content.append(processed_heading)
        else:
            content.append(paragraph.text)
    extract_doc = ('\n'.join(content).replace("./", "! ").replace('\n\n', "! ").replace("\n", " ")
                   .replace("\n\n\n\n", " ").replace("\n\n\t", "! ").replace("\n\n", "! ").replace("\t", "! "))
    sentences = sent_tokenize(extract_doc)

    sentences_en = []
    sentences_vi = []

    for sentence in sentences:
        # Xác định ngôn ngữ
        language = detect(sentence)
        if language == 'en':
            sentences_en.append(sentence)
        elif language == 'vi':
            sentences_vi.append(sentence)
        else:
            sentences_en.append(sentence)

    # Lưu vào file
    with open(output_file_en, 'w', encoding='utf-8') as file_en:
        for sentence in sentences_en:
            file_en.write(sentence + '\n')

    # Lưu vào file
    with open(output_file_vi, 'w', encoding='utf-8') as file_vi:
        for sentence in sentences_vi:
            file_vi.write(sentence + '\n')

    with open(output_file_en, 'r', encoding='utf-8') as file1, open(output_file_vi, 'r', encoding='utf-8') as file2:
        content1 = file1.read()
        content2 = file2.read()
    content1_with_spaces = content1.replace('!', ' ')
    content2_with_spaces = content2.replace('!', ' ')
    with open(output_file_en, 'w', encoding='utf-8') as file1, open(output_file_vi, 'w', encoding='utf-8') as file2:
        file1.write(content1_with_spaces)
        file2.write(content2_with_spaces)

def main():
    parser = argparse.ArgumentParser(description='Tool Tách Câu')
    subparsers = parser.add_subparsers(dest='version', help='Version of the tool')

    # Verion 1
    version1_parser = subparsers.add_parser('version1', help='Version 1: Cặp EN-VN thông thường.')
    version1_parser.add_argument('--input_file1', type=str, required=True, help='Đường dẫn file đầu vào thứ nhất.')
    version1_parser.add_argument('--input_file2', type=str, required=True, help='Đường dẫn file đầu ra thứ hai.')
    version1_parser.add_argument('--output_file1', type=str, default='output_file1.txt', help='Đường dẫn file đầu ra thứ nhất.')
    version1_parser.add_argument('--output_file2', type=str, default='output_file2.txt', help='Đường dẫn file đầu ra thứ hai.')

    # Version 2
    version2_parser = subparsers.add_parser('version2', help='Version 2: Văn bản song ngữ trong cùng 1 file.')
    version2_parser.add_argument('--input_file', type=str, required=True, help='Đường dẫn file đầu vào.')
    version2_parser.add_argument('--output_file_v2_1', type=str, default='output_ver2_en.txt', help='Đường dẫn file đầu ra tiếng anh.')
    version2_parser.add_argument('--output_file_v2_2', type=str, default='output_ver2_vi.txt', help='Đường dẫn file đầu ra tiếng việt.')

    args = parser.parse_args()

    if args.version == 'version1':
        extract_sentences_from_plain_files(args.input_file1, args.input_file2, args.output_file1, args.output_file2)
        print('oke ver1.')

    elif args.version == 'version2':
        extract_sentences_from_translated_file(args.input_file, args.output_file_v2_1, args.output_file_v2_2)
        print('oke ver2.')

if __name__ == "__main__":
    main()
