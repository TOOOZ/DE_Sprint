x1 = '111';
x2 = '101';



def toBinary(num):
    result = '';
    while num >1:
        result+= str(num % 2);
        num= num//2;
    result+=str(num);
    return result[::-1];
            
def toTen(num):
    num = num[::-1];
    result = 0;
    i= len(num)-1;
    while i > -1 :
        result+= int(num[i])*(2**i);
        i-=1;
    return result;
        
result = toTen(x1) * toTen(x2);
result = toBinary(result);
print(result);

