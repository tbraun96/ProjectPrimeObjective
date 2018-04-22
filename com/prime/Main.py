from com.prime.gpu.GPUMathKernel import GPUMathKernel

kernel = GPUMathKernel()
vals = kernel.add([2, 3, 4], [5, 6, 7])

print("Vals:", vals[0], vals[1], vals[2])
