from com.prime.gpu.GPUMathKernel import GPUMathKernel
from com.prime.intelligence.Brain import Brain

kernel = GPUMathKernel()
vals = kernel.add([1, 3, 4], [5, 6, 7])

print("Vals:", vals[0], vals[1], vals[2])
brain = Brain("eva_green.jpg", "BP", .7, 1, [1, 0], 2)
