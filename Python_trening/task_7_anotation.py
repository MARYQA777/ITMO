a: int = 5
b: str = 'строка'
c: list =[1, 2]

def ident(s: str, width: int) -> str:
    return "" * (max(0, width - len(s))) + s

print ('indent(69,69)')

def strings_lendht(s: str="") -> int:
    return len(s)

def min_list(a: list, b: list ) -> int:
    return max(len(a), len(b))





