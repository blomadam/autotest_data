import pytest
import hashlib


@pytest.mark.parametrize("test_file, expected_hash", [
    # filenames and md5 hashes for files from sql queries
    ("data/01interim/main_table_vectorized.csv.gz", "0cb10d37ce8fe0e0252a26235fa7dc79"),
    ("data/01interim/keywords_table_vectorized.csv.gz", "4692fe0054a330ee4d1c407e8c0b9e6f"),
])
def test_interim_data(test_file, expected_hash):
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
