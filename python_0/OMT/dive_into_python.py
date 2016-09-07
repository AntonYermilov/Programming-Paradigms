import dis;

def double_swap(a, b):
    a, b = b, a = a, b;
    return a, b;

print("Looks like double_swap(1, 2) = (1, 2), because of double swap");
print("Actually: {} ?!".format(double_swap(1, 2)));
print("\nAnalyze Disassembly!");
print("Bytecode of double_swap:");
dis.dis(double_swap);

print();
print("As you can see a, b = b, a = a, b is same as");
print("\t0. a', b' = a, b; # 0, 3, 6")
print("\t1. a, b = a', b'; # 13, 16");
print("\t2. b, a = a', b'; # 22, 25");
