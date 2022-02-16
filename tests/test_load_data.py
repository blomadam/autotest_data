import pytest
from autotest_data.load_data import load_data
import hashlib

@pytest.mark.parametrize("test_file, expected_hash", [
    # filenames and md5 hashes for files from sql queries
    ("data/00raw/main_table.csv.gz", "ff7247b0119c3df7a1e593576c206c6f"),
    ("data/00raw/keywords_table.csv.gz", "f8363838960fc63139d58324a43e11c6"),
])
def test_data(test_file, expected_hash):
    hash_buffer_length = 65536  # read files in 64kb chunks
    md5_sum = hashlib.md5()
    with open(test_file, 'rb') as f:
        while True:
            data = f.read(hash_buffer_length)
            if not data:
                break
            md5_sum.update(data)
    result = md5_sum.hexdigest()
    assert result == expected_hash


@pytest.mark.skip(reason="input checking not implemented")
def test_invalid_data_input():
    with pytest.raises(ValueError):
        load_data("2")


@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"
