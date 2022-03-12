p_a,p_b=int(input())/100,int(input())/100

def f(n):
  if (n==1)|(n==0):
    return 1
  return n*f(n-1)

def prob(p_a,p_b):
  p,n=0,18
  not_prime=[0,1,4,6,8,9,10,12,14,15,16,18]
  for i in not_prime:
    for j in not_prime:
      p+=f(n)/(f(i)*f(n-i))*(p_a**i)*((1-p_a)**(n-i))*f(n)/(f(j)*f(n-j))*(p_b**j)*((1-p_b)**(n-j))
  return 1-p

print(prob(p_a,p_b))