#https://www.google.com.br/maps/place/R.+Cenair+Maic%C3%A1+-+Jardim+dos+Lagos,+Gua%C3%ADba+-+RS,+92500-000/
import webbrowser
import sys
base_url='https://www.google.com.br/maps/place/'

def get_place_argument(place):
    return(place.replace(' ','+'))
def args_to_str(args):
    arg_str=args[1]
    for arg in args[2:]:
        arg_str=arg_str+" "+str(arg)
    return arg_str

def main():
    webbrowser.open(base_url+get_place_argument(args_to_str(sys.argv)))
    sys.exit()

if __name__=='__main__':
    main()
