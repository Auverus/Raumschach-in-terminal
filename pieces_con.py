import math
class move(): 
    def knight_can_move(self,d_x,d_y,d_z, g_x,g_y,g_z):
        if g_z == d_z:
            if math.fabs(d_x-g_x) == 2 and math.fabs(d_y-g_y) == 1:
                return True
                
            elif math.fabs(d_x-g_x) == 1 and math.fabs(d_y-g_y) == 2:
                return True
                
            else:
                return False

        elif g_x == g_x:
            if math.fabs(d_z-g_z) == 2 and math.fabs(d_y-g_y) == 1:
                return True
                
            elif math.fabs(d_z-g_z) == 1 and math.fabs(d_y-g_y) == 2:
                return True
                
            else:
                return False      
        
        elif d_y == g_y:
            if math.fabs(d_z-g_z) == 2 and math.fabs(d_x-g_x) == 1:
                return True
                
            elif math.fabs(d_z-g_z) == 1 and math.fabs(d_x-g_x) == 2:
                return True
                
            else:
                return False
                
        else:
            return False   
    def pawn_black_can_move(self, d_x,d_y,d_z, g_x,g_y,g_z):
        if d_x == g_x:
            if d_y == g_y + 1 and d_z == g_z:
                return True
                
            if d_y == g_y and d_z == g_z-1:
                return True
        else:
            return False
    def king_can_move(self, d_x,d_y,d_z, g_x,g_y,g_z):
        if math.fabs(d_x - g_x) <= 1 and math.fabs(d_y - g_y) <= 1 and math.fabs(d_z - g_z) <= 1:
            return True
            
        else:
            return False
    def queen_can_move(self, d_x,d_y,d_z, g_x,g_y,g_z):
    
        if d_x != g_x or d_y != g_y or d_z != g_z:
        
            if d_z == g_z:
                if math.fabs(d_y-g_y) == math.fabs(d_x-g_x):
                    return True
                    
                elif d_x == g_x or d_y == g_y:
                    return True
                    
            elif d_x == g_x:
                if math.fabs(d_y-g_y) == math.fabs(d_z-g_z):
                    return True
                    
                elif d_y == g_y or d_y == g_y:
                    return True
                    
            elif d_y == g_y:
                if math.fabs(d_x-g_x) == math.fabs(d_z-g_z):
                    return True
                    
                if d_x == g_x or d_z == g_z:
                    return True
                
            elif math.fabs(d_y-g_y) == math.fabs(d_x-g_x) and math.fabs(d_x-g_x) == math.fabs(d_z - g_z):
                return True
                
            else:
                return False
                
        else: return False
    def thief_can_move(self, d_x,d_y,d_z, g_x,g_y,g_z):
        if d_x != g_x or d_y != g_y or d_z != g_z:
            if math.fabs(d_y-g_y) == math.fabs(d_x-g_x) and math.fabs(d_x-g_x) == math.fabs(d_z - g_z):
                return True
                
            else:
                return False

    def bishop_can_move(self, d_x,d_y,d_z, g_x,g_y,g_z):
    
        if d_x != g_x or d_y != g_y or d_z != g_z:
            if d_z == g_z:
                if math.fabs(d_y-g_y) == math.fabs(d_x-g_x):
                    return True    
                    
            elif d_x == g_x:
                if math.fabs(d_y-g_y) == math.fabs(d_z-g_z):
                    return True
                    
            elif d_y == g_y:
                if math.fabs(d_x-g_x) == math.fabs(d_z-g_z):
                    return True
                    
            else:
                return False
                
        else:
            return False
    def rook_can_move(self, d_x,d_y,d_z, g_x,g_y,g_z):
        
        if d_x == g_x and d_y == g_y and d_z != g_z:
            return True
            
        elif d_x == g_x and d_y != g_y and d_z == g_z:
            return True
            
        elif d_x != g_x and d_y == g_y and d_z == g_z:
            return True
            
        else:
            return False
    def pawn_white_can_move(self, d_x,d_y,d_z, g_x,g_y,g_z):
        if d_x == g_x:
            if d_y == g_y - 1 and d_z == g_z:
                return True
                
            if d_y == g_y and d_z == g_z+1:
                return True
        else:
            return False