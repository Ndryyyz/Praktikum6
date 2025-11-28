import math

# Fungsi a(x): mengembalikan x**2
a = lambda x: x**2

# Fungsi b(x, y): mengembalikan akar dari x**2 + y**2
b = lambda x, y: math.sqrt(x**2 + y**2)

# Fungsi c(*args): mengembalikan rata-rata dari semua argumen
c = lambda *args: sum(args) / len(args)

# Fungsi d(s): menggabungkan set menjadi string
d = lambda s: "".join(set(s))

# Program utama untuk testing
def main():
    print("=== TESTING LAMBDA FUNCTIONS ===\n")
    
    # Test fungsi a
    print("1. Fungsi a(x) = x**2")
    x = 5
    hasil_a = a(x)
    print(f"   a({x}) = {hasil_a}\n")
    
    # Test fungsi b
    print("2. Fungsi b(x, y) = sqrt(x**2 + y**2)")
    x, y = 3, 4
    hasil_b = b(x, y)
    print(f"   b({x}, {y}) = {hasil_b}\n")
    
    # Test fungsi c
    print("3. Fungsi c(*args) = rata-rata")
    angka = [10, 20, 30, 40, 50]
    hasil_c = c(*angka)
    print(f"   c({angka}) = {hasil_c}\n")
    
    # Test fungsi d
    print("4. Fungsi d(s) = gabung set string")
    string = "hello"
    hasil_d = d(string)
    print(f"   d('{string}') = '{hasil_d}'")
    print(f"   (menghilangkan duplikat karakter)\n")

if __name__ == "__main__":
    main()
