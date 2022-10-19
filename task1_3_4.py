
x = '[{}({})]';           #Тестируемая строка
my_stack = [];      #Стек
counter = 0;        #Счетчик


i = 0;              #Счетчик цила

while i < len(x):
    if (i==0 and (x[0] == '}' or x[0] == ')' or x[0] == ']')):    #Если строка начинается с закрытой скобки
       counter = -1;
       break;   
        
    if (x[i] == '}'):                       #Если текущий элемент это закрытая скобка
        if (my_stack[-1] == '{'):           #То смотрим предыдущий элемент
            counter-=1; 
            my_stack.pop();
        else:
            couter = -1;
            break;
    elif (x[i] == ']'):
        if (my_stack[-1] == '['):
            counter-=1;
            my_stack.pop();
        else:
            couter = -1;
            break;
    elif (x[i] == ')'):
        if (my_stack[-1] == '('):
            counter-=1;
            my_stack.pop();
        else:
            couter = -1;
            break;
    else:
        my_stack.append(x[i]);
        counter+=1;
    i+=1;

if (counter == 0):          #если счетчик =0 то последовательность правильная
    print('true');
else:
    print('false');