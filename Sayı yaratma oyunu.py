#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random


# In[4]:


cevap = random.randint(50,250)
sayac = 0

while sayac == 10:
    tekrar = str(input('Oyunu tekrar oynamak ister misiniz?e/h: '))
    if tekrar == 'h':
            break
    
    else:
        while sayac <= 10:
            sayi = int(input('Lütfen 50-250 aralığında bir sayi giriniz: '))
            sayac += 1
            if sayi < 50 or sayi > 250:
                print('Lütfen belirtlien değerler aralığında sayı girin:')
                sayac -=1
            else:
                pass
            if sayi == cevap:
                print('Tebrikler!{} cevabını {}. denemede buldunuz.' . format(cevap, sayi))
                continue
                
            elif sayi < cevap:
                print('Daha büyük bir sayi girin')
                
            elif sayi > cevap:
                print('Daha kücük bir sayi girin')
        
       
            
    
     

