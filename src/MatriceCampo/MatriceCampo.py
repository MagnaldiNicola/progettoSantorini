
class Matrice:
 def __init__(self,cols, rows):
  self.cols=cols
  self.rows=rows
  self.matrix = []
  for j in range (0, rows-1):
   row=[]
   for i in range(0,cols-1):
    row.append([])
   self.matrix.append(row)


 # da finiredef set(self,x,y,cella):

 def get(self, x, y):
  return self.matrix()

 def riga(self, x):
  return self.matrix[x]

 # da finire    def show(self):

 #   da finire  def __str__(self):







