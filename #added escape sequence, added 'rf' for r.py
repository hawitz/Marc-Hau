#added escape sequence, added 'rf' for raw strings
def print_marc():
  print(rf"""
                        ________      ___________
  |\    /|      /\      |       \     |
  | \  / |     /  \     |        |    |
  |  \/  |    /----\    |________/    |
  |      |   /      \   |       \     |
  |      |  /        \  |        \    |__________
  """)
def print_hau():
  print(rf"""
  |       |        /\        |       |
  |       |       /  \       |       |  
  |-------|      /----\      |       |
  |       |     /      \     |       |
  |       |    /        \    |_______|
  """)
print_marc()
print_hau()