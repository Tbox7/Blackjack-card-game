import random as rnd
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
blank =""" 
  ___ 
 |   | 
 |   | 
 |___| 
 """
ace =""" 
  __  
 |A  | 
 | /\| 
 |_\/| """

two = """ 
  ___  
 |2  | 
 | /\| 
 |_\/|"""
 
three = """ 
  ___  
 |3  | 
 | /\| 
 |_\/|"""

four = """
  ___  
 |4  | 
 | /\| 
 |_\/|"""

five = """
  ___  
 |5  | 
 | /\| 
 |_\/|"""

six = """
  ___  
 |6  | 
 | /\| 
 |_\/|"""

seven = """
  ___  
 |7  | 
 | /\| 
 |_\/|"""

eight = """
  ___  
 |8  | 
 | /\| 
 |_\/|"""

nine = """
  ___  
 |9  | 
 | /\| 
 |_\/|"""

ten = """
  ___  
 |10 | 
 | /\| 
 |_\/|"""

jack = """
  ___  
 |J  | 
 | /\| 
 |_\/|"""

queen = """
  ___  
 |Q  | 
 | /\| 
 |_\/|"""

king = """
  ___  
 |K  | 
 | /\| 
 |_\/|"""

cards = {
    11 : ace,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven,
    8: eight,
    9: nine,
    10: rnd.choice([ten, jack, queen, king])
}
