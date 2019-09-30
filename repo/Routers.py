# Routers.py BEGIN
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
# + Importing Controllers.py BEGIN
###########################################################################
from Controllers import *
###########################################################################
# - Importing Models.py END
###########################################################################
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
#
###########################################################################
# + App 404 Handler BEGIN
###########################################################################
@app.errorhandler(404)
def page_not_found(e):
    print("404 Handler => "+request.url)
    return redirectRoute("home")
###########################################################################
# - App 404 Handler END
###########################################################################
#
#
# Routers.py END