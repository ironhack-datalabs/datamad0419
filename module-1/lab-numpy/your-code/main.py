#1. Import the NUMPY package under the name np.
import numpy as np
#import numpy.matlib 

#2. Print the NUMPY version and the configuration.
print(np.version.version)


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

# Usando funciones de numpy
# np.empty() #el contenido inicial es aleatorio dependiendo del estado de la memoria

# Usando librerias
# np.random.randint() 
# np.random.choice() 
# np.random.rand()
# np.random.random()
# ...

# Pasando una lista de listas random a array numpy
# lista = [[45,56],[77,3],[8,5]]
# np.array(lista)

a = np.random.random((2, 3, 5))



#4. Print a.
print('\nA = ', a)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5, 2, 3))


#6. Print b.
print('\nB = ', b)


#7. Do a and b have the same size? How do you prove that in Python code?
print('Size a: ', a.size, 'Size b:', b.size)
#print(np.add(a,b))

if a.size == b.size:
        print('Same size')
else:
    print('Diferent size')



#8. Are you able to add a and b? Why or why not?
# No es posible no tienen las mismas dimensiones
print('Shape a: ', a.shape)
print('Shape b: ', b.shape)


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose(1, 2, 0)
print('\nC = ', c)
print('Shape c: ', c.shape)
#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
print('Shape a: ', a.shape)
print('Shape c: ', c.shape)
d = np.add(a,c)

print('Suma a y c: \n', d)
# AHora funciona porque tienen la misma dimensión o forma

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print('\nA = ', a)
print('\nD = ', d)

#Tienen la misma dimensión y D es el resultado de haber sumado uno a cada elemento de A


#12. Multiply a and c. Assign the result to e.
e = np.multiply(a, c)
print('\nE = ', e)

#13. Does e equal to a? Why or why not?
print('A = E :', (a==e).all())
# Son iguales ya que se ha multiplicado elemento a elemento de a con c y esta es una matriz de unos


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max = d.max()
d_min = d.min()
d_mean = d.mean()


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty([2, 3, 5])
print('\nF = ', f)


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
"""
Para realizar la prueba de la pregunta 17 con los elementos dados en esta
d = np.array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])
d_max = d.max()
d_min = d.min()
d_mean = d.mean()
"""

print('\nD = ', d)

print('Mean: ', d_mean, 'Max: ', d_max, 'Min: ', d_min)
for x in range(len(d)):
	for y in range(len(d[x])):
		for z in range(len(d[x][y])):
			if d[x][y][z] == d_mean:
				f[x][y][z] = 50
			elif d[x][y][z] == d_max:
				f[x][y][z] = 100
			elif d[x][y][z] == d_min:
				f[x][y][z] = 0
			elif d[x][y][z] > d_min and d[x][y][z] < d_mean:
				f[x][y][z] = 25
			elif d[x][y][z] > d_mean and d[x][y][z] < d_max:
				f[x][y][z] = 75
			
	
"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""

print('\nD = ', d)
print('\nF = ', f)
# He comprobado con los datos del ejemplo y el resultado de f es el esperado

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
f = f.astype(np.chararray)
for x in range(len(f)):
	for y in range(len(f[x])):
		for z in range(len(f[x][y])):
			if f[x][y][z] == 0:
				f[x][y][z] = chr(ord('A'))
			elif f[x][y][z] == 25:
				f[x][y][z] = chr(ord('B'))
			elif f[x][y][z] == 50:
				f[x][y][z] = chr(ord('C'))
			elif f[x][y][z] == 75:
				f[x][y][z] = chr(ord('D'))
			elif f[x][y][z] == 100:
				f[x][y][z] = chr(ord('E'))

print('\nF = ', f)