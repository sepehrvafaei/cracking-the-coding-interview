#methood 1

def func(x):
	if(len(x)==len(set(x))):
		return True
	return False

#method 2

def func2(x):
    MAX_CHAR=256
    arr=[False]*MAX_CHAR
    for i in range(len(x)):
        if(arr[ord(x[i])]):
            return False
        else:
            arr[ord(x[i])]=True
    return True

#method 3

def func3(x):
    string="".join(sorted(x))
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            return False
    return True
