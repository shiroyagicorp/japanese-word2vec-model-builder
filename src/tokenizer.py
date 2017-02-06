import os
import subprocess
import sys
import tempfile

import MeCab


__neologd_repo_name = 'mecab-ipadic-neologd'
__neologd_repo_url = 'https://github.com/neologd/mecab-ipadic-neologd.git'


def download_neologd(dic_path):
    dic_path = os.path.abspath(dic_path)
    with tempfile.TemporaryDirectory() as temp_dir:
        subprocess.call(['git', 'clone', '--depth', '1', __neologd_repo_url],
                        stdout=sys.stdout, cwd=temp_dir)
        neologd_dir_path = os.path.join(temp_dir, __neologd_repo_name)
        subprocess.call(['./bin/install-mecab-ipadic-neologd', '-y', '-u',
                         '-p', dic_path],
                        stdout=sys.stdout, cwd=neologd_dir_path)


def get_tagger(dic_path):
    return MeCab.Tagger('-d {}'.format(dic_path))


def tokenize(text, tagger):
    tokens = []
    for line in tagger.parse(text).split('\n'):
        if line == 'EOS':
            break
        surface = line.split('\t')[0]
        tokens.append(surface)
    return tokens
