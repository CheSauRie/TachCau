import docx2txt
import argparse
from nltk.tokenize import sent_tokenize
from langdetect import detect

def extract_sentences_from_plain_files(input_file1, input_file2, output_file1, output_file2):
    text1 = docx2txt.process(input_file1)
    text2 = docx2txt.process(input_file2)
    sentences1 = sent_tokenize(text1)
    sentences2 = sent_tokenize(text2)

    with open(output_file1, 'w', encoding='utf-8') as file1, open(output_file2, 'w', encoding='utf-8') as file2:
        for sentence in sentences1:
            file1.write(sentence + '\n')
        for sentence in sentences2:
            file2.write(sentence + '\n')

def extract_sentences_from_translated_file(input_file, output_file_en, output_file_vi):
    text = docx2txt.process(input_file)
    quan = sent_tokenize(text)
    print(quan)
    paragraphs = text.split('\n\n')
    # print(paragraphs)
    sentences_en = []
    sentences_vi = []

    for paragraph in paragraphs:
        sentences = sent_tokenize(paragraph)
        for sentence in sentences:
            language = detect(sentence)
            if language == 'en':
                sentences_en.append(sentence)
            elif language == 'vi':
                sentences_vi.append(sentence)

    with open(output_file_en, 'w', encoding='utf-8') as file_en:
        for sentence in sentences_en:
            file_en.write(sentence + '\n')

    with open(output_file_vi, 'w', encoding='utf-8') as file_vi:
        for sentence in sentences_vi:
            file_vi.write(sentence + '\n')

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
