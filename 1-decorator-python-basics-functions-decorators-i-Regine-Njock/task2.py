def get_html_greeting():
    massage='Hello, world!'

    def make_bold():
        return  f"<strong> {massage} </strong>"
        
    return make_bold()

@ get_html_greeting
#print(get_html_greeting())
def get_custom_html_greeting(first, last):
    first=[]
    last=[]
    return f'{first}{last}'
print(get_custom_html_greeting('James', 'Brown'))
