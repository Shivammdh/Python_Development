def fab(n):
	a=0
	b=1
	t=0
	s=0

	while(t<n):
		print(a)
		s=a+b
		a=b
		b=s
		t+=1
num=int(input())
fab(num)