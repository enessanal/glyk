# Controllers.py BEGIN
#
#
#
###########################################################################
# + Controlling "__name__" Variable BEGIN
###########################################################################
if __name__ == "__main__":
    print("Exiting...\nRun this command => \"python main.py\"")
    exit()
###########################################################################
# - Controlling "__name__" Variable END
###########################################################################
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
#
#
#
#
#
#
#
#
#
###########################################################################
# + Route Login BEGIN
###########################################################################
@app.route("/login",methods=["GET","POST"])
def loginRoute():	
  return loginController(request)
###########################################################################
# - Route Login END
###########################################################################
#
#
#
###########################################################################
# + Route Logout BEGIN
###########################################################################
@app.route("/logout",methods=["POST"])
def logoutRoute():	
  return logoutController(request)
###########################################################################
# - Route Logout END
###########################################################################
#
#
#
###########################################################################
# + Route Panel BEGIN
###########################################################################
@app.route("/panel",methods=["GET"])
def panelRoute():	
  return panelController(request)
###########################################################################
# - Route Panel END
###########################################################################
#
#
#
###########################################################################
# + Route Home BEGIN
###########################################################################
@app.route("/",methods=["GET"])
def homeRoute():	
  return redirectRoute("login")
###########################################################################
# - Route Home END
###########################################################################
#
#
#
###########################################################################
# + App Before Request BEGIN
###########################################################################
@app.before_request
def before_request():
  print("----------------------------")
  print("----------------------------")
  g.user = None
  if "user" in session:
    g.user = session["user"]
###########################################################################
# - App Before Request END
###########################################################################
#
#
# Controllers.py END