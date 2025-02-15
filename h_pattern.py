# to make hte patternn of H 
'''
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH HHHHH HHHHH HHHHH HHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
'''

def pattern(n):
    #for top pyramid
    for i in range (n):
        print(" "*(n-i-1)+"H"*(2*i+1))
    
    #for middle pillar
    for i in range(n):
        print(" "*(n//2)+"H"*(n)+" "*((n)*3)+"H"*(n)) 

    #for middle horizontal line
    for i in range(n-2):
        print(" "*(n//2)+"H"*(n*5)) 
    
    #for bottom pillar
    for i in range(n):
        print(" "*(n//2)+"H"*(n)+" "*((n)*3)+"H"*(n)) 

    #for bottom pyramid
    for i in range (n):
        print(" "*((4*n)+i)+"H"*(2*(n-i)-1))

num = int(input())
pattern(num)