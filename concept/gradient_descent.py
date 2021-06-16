import numpy as np
def gradient_descent(x, y):
    #start with some value of m_curr and b_curr
    m_curr = b_curr = 0
    iterations = 500 #number of baby steps
    n = len(x)
    learningrate = 0.01
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr #as y = m*x + b
        cost  =(1/n) * sum((y - y_predicted)**2)#same as sum([val**2 for val in (y-y_predicted)])
        md = -(2/n) * sum(x * (y - y_predicted))#m derevative
        bd = -(2/n) * sum(y - y_predicted)#b deravitive
        m_curr = m_curr - learningrate * md
        b_curr = b_curr - learningrate * bd
        print(f'm: {m_curr}, b: {b_curr}, iteration: {i}, cost {cost}')


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])
gradient_descent(x, y)