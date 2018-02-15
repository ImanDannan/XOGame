class xo_matrix():
  Init_Matrix=[["-","-","-"],["-","-","-"],["-","-","-"]]
  Current_Matrix=[]
  def __init__(self,player_name):
     self.player_name = player_name
     self.Current_Matrix= self.Init_Matrix
   
  def ShowMatrix(self):
    #print self.Current_Matrix
    row_no=0
    for row in self.Current_Matrix:
      print self.Current_Matrix[row_no]
      row_no=row_no+1

  def Set_Cell(self,row,col,xo):
          self.Current_Matrix[row][col]=xo
    
     

  def IsEmpty_Cell(self,row,col):
      if self.Current_Matrix[row][col] == "-":
         return True
      else:
         return False

  def IsFull_Matrix(self):
      row_no=0
      col_no=0
      rowstr=""
      for row in self.Current_Matrix: 
         for col in  self.Current_Matrix[row_no]:
            rowstr=rowstr+col
            col_no=col_no+1
         row_no=row_no+1
      if rowstr.find("-") == -1:
            print ("Game is over")
            return True
      return False      

  def CheckRow(self):
      row_no=0
      for row in self.Current_Matrix:
          rowstr=""
          for col in  self.Current_Matrix[row_no]:
            #print col
             rowstr=rowstr+col
             if rowstr=="xxx" or rowstr=="ooo":
                 print (self.player_name + " Won!")
                 return True
          row_no=row_no+1 
      return False
     
  def CheckColumn(self):
      row_no=0
      col_no=0
      col1str=""
      col2str=""
      col3str=""
      for  row_no in range(0,3):
        for col_no in  range(0,3):
           if col_no==0:
                col1str=col1str+self.Current_Matrix[row_no][col_no]
           elif col_no==1:
                col2str=col2str+self.Current_Matrix[row_no][col_no]
           elif col_no==2:
                col3str=col3str+self.Current_Matrix[row_no][col_no]
           col_no=col_no+1
        row_no=row_no+1 
      
      #out loop 
      if col1str=="xxx" or col1str=="ooo" or col2str=="xxx" or col2str=="ooo"or col3str=="xxx" or col3str=="ooo" :
            print (self.player_name + " Won!")
            return True
      else:
             return False    
  
#-------------------------------
  def CheckDiagonal(self):
      row_no=0
      col_no=0
      diagonal1str=""
      diagonal2str=""
      for  row_no in range(0,3):
        for col_no in  range(0,3):
           if col_no==row_no :
                diagonal1str=diagonal1str+self.Current_Matrix[row_no][col_no]
           if (col_no+row_no)==2:
                diagonal2str=diagonal2str+self.Current_Matrix[row_no][col_no]
           col_no=col_no+1
        row_no=row_no+1 
      
      #out loop 
      if diagonal1str=="xxx" or diagonal1str=="ooo" or diagonal2str=="xxx" or diagonal2str=="ooo" :
            print (self.player_name + " Won!")
            return True
      else:
             return False 






player1= xo_matrix("Player1")
player2= xo_matrix("Player2")
player1.player_name=raw_input("Enter Player1 Name ")
player2.player_name=raw_input("Enter Player2 Name ")

print (player1.player_name + " x ||| " + player2.player_name + " o ")
game_over=False
while not(game_over) :
   player1.ShowMatrix()
   Wrong_Enter= False 
   while not(Wrong_Enter):
     print player1.player_name + " Turn:"
     while True:
         row= raw_input("Enter Cell row no (1-3)")
         if row.isdigit():
            row=int(row)
            if row in [1,2,3]:
               row=row-1
               break
             
     while True:
        col= raw_input("Enter Cell col no (1-3)")
        if col.isdigit():
           col=int(col)
           if col in [1,2,3]:
              col=col-1
              break
           
          
     if player1.IsEmpty_Cell(row,col) and player2.IsEmpty_Cell(row,col):
       xo="x"
       player1.Set_Cell(row,col,xo)
       if player1.CheckRow():
          game_over=True  
       if player1.CheckColumn():
          game_over=True
       if player1.CheckDiagonal():
          game_over=True  
       if player1.IsFull_Matrix():
          game_over=True            
       Wrong_Enter=True 
     else:
       print("Cell not Empty! Try another Cell")
       Wrong_Enter=False

#----------------------------------
   player1.ShowMatrix()
   Wrong_Enter= False 
   while not(Wrong_Enter) and not(game_over):
     print player2.player_name + " Turn:"
     while True:
         row= raw_input("Enter Cell row no (1-3)")
         if row.isdigit():
            row=int(row)
            if row in [1,2,3]:
               row=row-1
               break
            
         
     while True:
        col= raw_input("Enter Cell col no (1-3)")
        if col.isdigit():
           col=int(col)
           if col in [1,2,3]:
              col=col-1
              break
           
        
     if player2.IsEmpty_Cell(row,col) and player1.IsEmpty_Cell(row,col):
       xo="o"
       player2.Set_Cell(row,col,xo)
       if player2.CheckRow():
         game_over=True
       if player2.CheckColumn():
         game_over=True
       if player2.CheckDiagonal():
           game_over=True    
       if player2.IsFull_Matrix():
         game_over=True
           
       Wrong_Enter=True 
     else:
       print("Cell not Empty! Try another Cell")
       Wrong_Enter=False







