from __future__ import print_function
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cnocr.utils import data_dir, read_charset

BAD_CHARS = [5751, 5539, 5536, 5535, 5464, 4105]


def main():
    # charset_fp = os.path.join(data_dir(), 'models', 'label_cn.txt')
    # 当前脚本的目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 构造 label_cn.txt 的路径
    label_file_path = os.path.join(script_dir, '..', 'cnocr', 'label_cn.txt')
    # 确保路径是正确的
    label_file_path = os.path.normpath(label_file_path)
    print("label_cn.txt 文件的位置:", label_file_path)
    charset_fp = os.path.join(label_file_path)
    alphabet, inv_alph_dict = read_charset(charset_fp)
    for idx in BAD_CHARS:
        print('idx: {}, char: {}'.format(idx, alphabet[idx]))


if __name__ == '__main__':
    main()
