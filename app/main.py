from generators.abs_range import abs_generator
from generators.pairwise_products import pairwise_mult
from generators.password_generator import password_gen
from generators.threaded_passwords import threaded_password_gen

def main():
    print("=== Генератор модулей ===")
    gen_abs = abs_generator(-3, 3)
    for _ in range(4):
        print(next(gen_abs))

    print("\\n=== Попарное умножение списков ===")
    gen_prod = pairwise_mult([1,2,3], [4,5,6])
    for _ in range(3):
        print(next(gen_prod))

    print("\\n=== Генератор паролей ===")
    gen_pass = password_gen()
    for _ in range(5):
        print(next(gen_pass))

    print("\\n=== Многопоточный генератор паролей ===")
    passwords = threaded_password_gen(count=5, threads=3)
    for p in passwords:
        print(p)

if __name__ == "__main__":
    main()