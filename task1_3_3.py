num = 1648;

nums = [];
nums.append(num//1000);
nums.append(num//100%10);
nums.append(num//10%10);
nums.append(num%10);
print(nums[3])
result = '';
i=0;

while i < nums[0]:
    result +='M'
    i+=1;

i=0;

while i < nums[1]:
    if nums[1] >= 5 :
        if nums[1] == 9:
            result +='CM';
            break;
        else:
            result +='D';
            nums[1] = nums[1]-5;
   
    if nums[1] == 4:
        result +='CD'
        break;
    if (nums[1] != 0):
        result +='C'
    i+=1;
i= 0;

while i < nums[2]:
    if nums[2] >= 5 :
        if nums[2] == 9:
            result +='XC'
            break;
        else:
            result +='L'
            nums[2] = nums[2]-5;
    if nums[2] == 4:
        result +='XL'
        break;
    if (nums[2] != 0):
        result +='X'
    i+=1;
i= 0;

while i < nums[3]:
    if nums[3] >= 5 :
        if nums[3] == 9:
            result +='IX'
            break;
        else:
            result +='V'
            nums[3] = nums[3]-5;
    if nums[3] == 4:
        result +='IV'
        break;
    if (nums[3] != 0):
        result +='I'
        print(i)
        print(nums[3])
    i+=1;
    
print(result)