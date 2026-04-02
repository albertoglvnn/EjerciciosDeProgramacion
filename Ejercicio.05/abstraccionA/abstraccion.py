from abc import ABC, abstractmethod

#clase abstracta (platilla)

class Animal(ABC):
    
    
   @abstractmethod
   def hablar(self):
       pass  #no se implementa el metodo
   
   
   
   #clase en especifico
   
   class perro(Animal):
       
       def hablar(self):
           return "guau guau"
   
   class gato(Animal):
         
         def hablar(self):
              return "miau miau"
          
#usar las clases 
perro = perro()
gato = gato()   
print(perro.hablar())
print(gato.hablar())    