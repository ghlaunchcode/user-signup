from flask import Flask, request
import os
import cgi
import jinja2


# init Flask w/ Debugging
g_app = Flask( __name__ )
g_app.config['DEBUG'] = True

# init Template directory for jinja env / set autoescaping to true
g_template_dir = os.path.join( os.path.dirname(__file__), 'templates' )
g_jinja_env = jinja2.Environment( loader =  jinja2.FileSystemLoader( g_template_dir ), autoescape=True )


# default entry point
@g_app.route( "/" ) #no post
def index( ):
    # open template
    indexTemplate = g_jinja_env.get_template('index.html')
    return indexTemplate.render(title="New User")


@g_app.route("/", methods=["POST"])
def verify():
    isError = False
    # Data:
    statusUserName = ""
    strUserName = ""
    strErrUserName = ""
    statusPassword0 = ""
    strErrPassword0 = ""
    statusPassword1 = ""
    strErrPassword1 = ""
    statusEmail = ""
    strEmail = ""
    strErrEmail = ""

    ERRSTR_STATUS_ERROR = "status-condition_ERROR"
    ERRSTR_EMPTY_FIELD = " Field is required!"
    ERRSTR_LENGTH_FIELD = " Field must be 3 to 20 characters!"
    ERRSTR_SPACES_FIELD = " Field must not contain spaces!"
    ERRSTR_MATCH_FIELD = " Fields must match!"
    ERRSTR_INVALID_EMAIL = " Field must contain valid email!"

    usUserName = cgi.escape( request.form['textUserName'] )
    usPassword0 = cgi.escape( request.form['textPassword0'] )
    usPassword1 = cgi.escape( request.form['textPassword1'] )
    usEmail = cgi.escape( request.form['textEmail'] )

    # Check fields for empty
    if usUserName == "":
        isError = True
        statusUserName = ERRSTR_STATUS_ERROR
        strErrUserName += ERRSTR_EMPTY_FIELD

    if usPassword0 == "":
        isError = True
        statusPassword0 = ERRSTR_STATUS_ERROR
        strErrPassword0 += ERRSTR_EMPTY_FIELD

    if usPassword1 == "":
        isError = True
        statusPassword1 = ERRSTR_STATUS_ERROR
        strErrPassword1 += ERRSTR_EMPTY_FIELD

    # NOTE: email may be empty

    # Username between 3 & 20 no spaces

    if len(usUserName) < 3 or len(usUserName) > 20:
        isError = True
        statusUserName = ERRSTR_STATUS_ERROR
        strErrUserName += ERRSTR_LENGTH_FIELD

    # returns -1 if not found, else index
    if usUserName.find(" ") > -1:
        isError = True
        statusUserName = ERRSTR_STATUS_ERROR
        strErrUserName += ERRSTR_SPACES_FIELD

    # Password Length 3 - 20 
    if len( usPassword0 ) < 3 or len( usPassword0 ) > 20:
        isError = True
	statusPassword0 = ERRSTR_STATUS_ERROR
        strErrPassword0 += ERRSTR_LENGTH_FIELD

    #Password Length 3 - 20
    if len( usPassword1 ) < 3 or len( usPassword1 ) > 20:
        isError = True
        statusPassword1 = ERRSTR_STATUS_ERROR
	strErrPassword1 += ERRSTR_LENGTH_FIELD

    # Passwords Match
    if usPassword0 != usPassword1:
        isError = True
        statusPassword0 = ERRSTR_STATUS_ERROR
        statusPassword1 = ERRSTR_STATUS_ERROR
        strErrPassword0 += ERRSTR_MATCH_FIELD
        strErrPassword1 += ERRSTR_MATCH_FIELD


    # if email entered, must contain @ .
    if len(usEmail) > 0:
        if usEmail.find("@") == -1 or usEmail.find(".") == -1:
            isError = True
            statusEmail = ERRSTR_STATUS_ERROR
            strErrEmail += ERRSTR_INVALID_EMAIL
        if len(usEmail) < 3 or len(usEmail) > 20:
            isError = True
            statusEmail = ERRSTR_STATUS_ERROR
            strErrEmail += ERRSTR_LENGTH_FIELD

    if isError:
        #TODO: check escaping
        indexTemplate = g_jinja_env.get_template('index.html')
        return indexTemplate.render( title="New User",
            statusUserName = statusUserName, strUserName = usUserName, strerrUserName = strErrUserName,
            statusPassword0 = statusPassword0, strerrPassword0 = strErrPassword0,
            statusPassword1 = statusPassword1, strerrPassword1 = strErrPassword1,
            statusEmail = statusEmail, strEmail = usEmail, strerrEmail = strErrEmail )
    else:
        indexTemplate = g_jinja_env.get_template('welcome.html')
        return indexTemplate.render( title="Home", strUserName = usUserName )


def main():
    #print( "begin main()")
    g_app.run()
    #print( "leaving main()")

if __name__ == "__main__":
    main()
