from flask import Flask;

g_app = Flask( '[DEBUG]' )

class UserForm:

    #TODO: make constructor
    def LoadTemplate():
        return ""

    def Render():
        strRet = LoadTemplate()
        return strRet

@g_app.route( "/" ) #no post
def index( ):

    #TODO: template argument
    iForm = UserForm()

    return iForm.Render();



def main():
    print( "begin main()")

    print( "leaving main()")

if __name__ == "__main__":
    main()