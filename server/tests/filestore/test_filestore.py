from filestore import Filestore
import pytest
import os

FILE = "test.json"


def delete_file():
    try:
        os.remove(FILE)
    except FileNotFoundError:
        pass


@pytest.fixture(autouse=True)
def delete_store():
    delete_file()
    yield
    delete_file()


def test_empty_filestore_creation():
    fs = Filestore(FILE)
    assert fs is not None


def test_empty_filestore_contains_no_collections():
    fs = Filestore(FILE)
    assert len(fs.collection_names()) == 0


def test_put_creates_collection():
    fs = Filestore(FILE)
    fs.put("col", "id_1", {'a': 1, 'b': 2})
    assert fs.collection_names()[0] == 'col'


def test_retrieve():
    fs = Filestore(FILE)
    fs.put("col", "id_1", {'a': 1, 'b': 2})
    fs.put("col", "id_2", {'a': 3, 'b': 4})
    assert fs.get("col", "id_1") is not None
    assert fs.get("col", "id_1")['a'] == 1


def test_retrieve_none():
    fs = Filestore(FILE)
    fs.put("col", "id_1", {'a': 1, 'b': 2})
    assert fs.get("col", "id_2") is None
    assert fs.get("other_col", "id_1") is None


def test_file_store():
    fs1 = Filestore(FILE)
    fs1.put("col", "id_1", {'a': 1, 'b': 2})

    fs2 = Filestore(FILE)
    assert fs2.get("col", "id_1") is not None
