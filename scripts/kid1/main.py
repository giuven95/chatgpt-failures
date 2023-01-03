

import random

SEQUENCES = [['East', 'South', 'West', 'North'], ['Alpha', 'Beta', 'Gamma', 'Delta'], ['Qui', 'Quo', 'Qua'], ['Donald', 'Duck', 'Dunn'], 
             ['Mambo #1', 'Mambo #2', 'Mambo #3', 'Mambo #4', 'Mambo #5'], ['Pippo', 'Pluto', 'Paperino'], ['Apple', 'Banana', 'Cherry'],
             ['Jesse Pinkman', 'Saul Goodman', 'Gustavo Fring', 'Walter White'],
             ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], ['S', 'M', 'L', 'XL', 'XXL', 'XXXL'], 
             ['Thumb', 'Index Finger', 'Middle Finger', 'Ring Finger', 'Pinky'], ['Mars', 'Earth', 'Venus', 'Mercury', 'Jupiter'],
             ['Orange', 'Is', 'The', 'New', 'Black'], ['Red', 'Green', 'Blue'], ['One', 'Two', 'Three', 'Four', 'Five'], 
             ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo'], ['Little', 'Red', 'Riding', 'Hood'], ['Car', 'Bike', 'Scooter'], 
             ['Sun', 'Moon', 'Star'], ['Ace', 'King', 'Queen', 'Jack'], ['Python', 'Java', 'C++'], ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si'], 
             ['January', 'February', 'March', 'April'], ['Rome', 'London', 'Paris'], ['September', 'October', 'November', 'December'], 
             ['Harry Potter', 'Hermione Granger', 'Ron Weasley'], ['Aaa', 'Bbb', 'Ccc', 'Ddd', 'Eee'], ['Cable', 'Wire', 'Plug'], 
             ['First', 'Second', 'Third', 'Fourth'], ['Eeny', 'Meeny', 'Miny', 'Moe']]

NAMES = ['John', 'Mary', 'Mike', 'Daisy', 'Jackie', 'Cindy', 'Sam', 'Nancy', 'Karen', 'Paul', 'Dave', 'Gina', 'Joe', 
         'Alice', 'Rob', 'Chris', 'Scott', 'Stephanie', 'Carol', 'Mikey', 'Bobby', 'Kathy', 'Molly', 'Diane', 'Linda']

FRACTIONS = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']

def make_kid1_question_answer():
  seq = random.choice(SEQUENCES)
  random.shuffle(seq)
  name = random.choice(NAMES)
  ll = len(seq)
  ss = ""
  template = " One of them is called {}."
  for nn in range(ll - 1):
    ss += template.format(seq[nn])
  question = "{}'s mom has {} kids. {} Who is the {} kid?".format(name, ll, ss, FRACTIONS[ll-1])
  answer = name
  return {"question": question, "answer": answer}

def main():
  print(make_kid1_question_answer())

if __name__ == "__main__":
  main()
