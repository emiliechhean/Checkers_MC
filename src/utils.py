from ruamel import yaml 

### SOURCE :  ###
def get_clicked_column(mouse_pos, params):
    x = mouse_pos[0]
    for i in range(1, 8):
        if x < i * params['WIDTH'] / 8:
            return i - 1
    return 7

def get_clicked_row(mouse_pos, params):
    y = mouse_pos[1]
    for i in range(1, 8):
        if y < i * params['HEIGHT'] / 8:
            return i - 1
    return 7

###

def parse_yaml(path):
    with open(path) as file :
        params = yaml.load(file, Loader = yaml.Loader)
    
    return params
          
