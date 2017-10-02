from flask import Flask;

g_app = Flask( __name__ )
g_app.config('[DEBUG]') = True

@g_app.route( "/" ) #no post
def index( ):

    # open template


    return g_userForm.format( )#TODO)


@g_app.route("/", methods="[POST]")
def verify():

    return ""


def main():
    print( "begin main()")
    g_app.run()
    print( "leaving main()")

if __name__ == "__main__":
    main()