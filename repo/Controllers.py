# Controllers.py BEGIN
#
#
#
###########################################################################
# + Importing Models.py BEGIN
###########################################################################
from Models import *
###########################################################################
# - Importing Models.py END
###########################################################################
#
#
#
###########################################################################
# + Controlling "__name__" Variable BEGIN
###########################################################################
control_name_variable(__name__)
###########################################################################
# - Controlling "__name__" Variable END
###########################################################################
#
#
#
###########################################################################
# + loginController BEGIN
###########################################################################
def loginController(request):
  title="Login"
  parameters={"title":title}

  if(request.method=="GET"):
    if g.user:
      return redirectRoute("panel")
    return render_template("login.html",parameters=parameters)

  elif(request.method=="POST"):
    if g.user:
      return redirectRoute("panel")
    else:
      if(request.form["username"]=="admin" and request.form["password"]=="123"):
        session["user"] = request.form["username"]
        return redirectRoute("panel")
      else:
        parameters["errors"]="error"
        return render_template("login.html",parameters=parameters)
  else:
    abort(405)
###########################################################################
# - loginController END
###########################################################################
#
#
#
###########################################################################
# + logoutController BEGIN
###########################################################################
def logoutController(request):
 
  if(request.method=="POST"):
    if g.user:
      session.pop("user",None)
    return redirectRoute("login")


  else:
    abort(405)
###########################################################################
# - logoutController END
###########################################################################
#
#
#
###########################################################################
# + panelController BEGIN
###########################################################################
def panelController(request):
  title="Panel"
  parameters={"title":title}

  if(request.method=="GET"):
    if g.user:
      parameters["username"]=g.user
      return render_template("panel.html",parameters=parameters)

    else:
      return redirect(url_for("loginRoute"))
  else:
    abort(405)
###########################################################################
# - panelController END
###########################################################################
#
#
# Controllers.py END