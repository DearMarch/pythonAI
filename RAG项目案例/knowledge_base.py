"""
知识库
"""
import os
import config_data as config
import hashlib

def check_md5(md5_str: str):

    if not os.path.exists(config.md5_path):
        open(config.md5_path, "w", encoding="utf-8").close()
        return False
    else:
        for line in open(config.md5_path, "r", encoding="utf-8").readlines():
            line = line.strip()
            if line == md5_str:
                return True

        return False


def save_md5(md5_str: str):

    with open(config.md5_path, "a", encoding="utf-8") as f:
        f.write(md5_str + "\n")


def get_string_md5(input_str: str, encoding="utf-8"):
    str_bytes = input_str.encode(encoding=encoding)

    md5_obj = hashlib.md5()
    md5_obj.update(str_bytes)
    md5_hex = md5_obj.hexdigest()

    return md5_hex


if __name__ == '__main__':
    save_md5("4ef520d6cd20ba4a727af08e17e4939e")
    print(check_md5("4ef520d6cd20ba4a727af08e17e4939e"))