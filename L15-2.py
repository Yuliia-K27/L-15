import pytest
from tree import Tree

@pytest.fixture
def tree():
    return Tree()

def test_add_node(tree):
    tree.add_node(5)
    assert tree.root.data == 5

def test_add_list(tree):
    data_list = [5, 3, 7, 1, 9]
    tree.add_list(data_list)
    assert tree.root.data == 5
    assert tree.root.left.data == 3
    assert tree.root.right.data == 7
    assert tree.root.left.left.data == 1
    assert tree.root.right.right.data == 9

def test_find_min(tree):
    data_list = [5, 3, 7, 1, 9]
    tree.add_list(data_list)
    assert tree.find_min() == 1

def test_find_max(tree):
    data_list = [5, 3, 7, 1, 9]
    tree.add_list(data_list)
    assert tree.find_max() == 9

def test_remove(tree):
    data_list = [5, 3, 7, 1, 9]
    tree.add_list(data_list)

    # Видалення листка
    tree.remove(1)
    assert tree.root.left.left is None

    # Видалення елемента з одним нащадком
    tree.remove(3)
    assert tree.root.left.data == 5

    # Видалення кореневого елемента з двома нащадками
    tree.remove(5)
    assert tree.root.data == 7

    # Видалення елемента, який не знайдено
    assert tree.remove(100) == False
