a = 1664525
c = 29381213
m = 60000000000
x0 = 522

with open('generated_numbers.csv', 'w') as file:
    for i in range(1000):
        x = (a * x0 + c) % m
        uniform = x / m
        file.write(f"{i+1};{uniform:.10f}".replace('.', ',') + '\n')
        x0 = x

print("file 'generated_numbers.csv' created successfully!")