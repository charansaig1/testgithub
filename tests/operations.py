from src.operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(1,2)==3
    assert add(-1,1)==0

def test_sub():
    assert sub(8,3)==5
    assert sub(5,2)==3
    assert sub(7,1)==6