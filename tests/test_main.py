import pytest
import os.path
import os
import filecmp

import subprocess

def test_cr_cp_files():
    subprocess.run('echo 123 >> m.txt && cp m.txt p.txt', shell=True)
    assert os.path.exists('/home/tampeiser/Programms/Pytest/m.txt')
    assert os.path.exists('/home/tampeiser/Programms/Pytest/p.txt')

def test_path():
    sum_1 = subprocess.call(["md5sum /home/tampeiser/Programms/Pytest/m.txt"], shell=True)
    sum_2 = subprocess.call(["md5sum /home/tampeiser/Programms/Pytest/p.txt"], shell=True)
    assert sum_1 == sum_2

def test_inside():
    filecmp.cmp('/home/tampeiser/Programms/Pytest/m.txt', '/home/tampeiser/Programms/Pytest/p.txt')
