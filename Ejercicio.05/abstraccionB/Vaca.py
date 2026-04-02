from Mob import Mob

class Vaca(Mob):
    """Mob pasivo, suena 'Muuuu', camina lento."""
    # TODO: implementa hacer_sonido, comportamiento, moverse
    
    def hacer_sonido(self) -> str:
            return "Muuuu"  
        
    def comportamiento(self) -> str:
            return "pasivo"
        
    def moverse(self) -> str:
            return "camina lento"   
        
    pass
