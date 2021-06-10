from ruamel import yaml 

### SOURCE :  ###
def get_clicked_column(mouse_pos):
    x = mouse_pos[0]
    for i in range(1, 8):
        if x < i * WIDTH / 8:
            return i - 1
    return 7

def get_clicked_row(mouse_pos):
    y = mouse_pos[1]
    for i in range(1, 8):
        if y < i * HEIGHT / 8:
            return i - 1
    return 7

###

def parse_yaml(path):
    with open(path) as file :
        params = yaml.load(file, Loader = yaml.Loader)
    
    return params
          
