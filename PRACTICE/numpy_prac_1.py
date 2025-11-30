import numpy as np
np1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np1[:,1:2])

#arithmetic
np2= np.array([1,2,3])
print (np2+34)
#"broadcasting"
#means multiplication of matrix rules got it
np3= np.array([[1,2,3,4,]])
np4= np.array([[1],[2],[3],[4]])
#1x4 and 4x1 so mutliplication gives 4x4
print (np3*np4)


# aggerate functions 
np5= np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(np.sum(np5))
print(np.mean(np5))
print(np.std(np5))
print(np.var(np5))

#filtering
np6= np.array([[67,20,30,19,5],[16,27,68,19,10]])

teenagers= np6 [ np6 < 18]
adults= np6 [ np6 >= 18]
even= np6[np6%2==0]
print(teenagers , adults , even)

#preserving the array after filtering 
adults_1= np.where(np6>=18 , np6 ,0 )  #replacing with 0
print(adults_1)

#random numbers
#randomnumbergenerator
rng= np.random.default_rng()
print(rng.integers(1,7))
#1,7 is the range or
print(rng.integers(low=1,high=7))
#for arrays 

print(rng.integers(low=1,high=101, size=6))
print(rng.integers(low=1,high=7,size=(2,3)))

fruits= np.array(["apple","banana","orange","cocnut","pineapple"])
fruits= rng.choice(fruits,size=(3,3))

print(fruits)