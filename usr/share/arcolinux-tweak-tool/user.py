# =================================================================
# =                  Author: Erik Dubois                          =
# =================================================================

from types import FunctionType
import Functions
import crypt
import os
from Functions import GLib

def create_user(self):
    username = self.hbox_username.get_text()
    name = self.hbox_name.get_text()
    atype = self.combo_account_type.get_active_text()
    password = self.hbox_password.get_text()
    confirm_password = self.hbox_confirm_password.get_text()
    user_password = "echo " + username + ":" + password    
    
    if password == confirm_password :
        if atype == "Administrator" :
            useradd ='useradd -m -G audio,video,network,storage,rfkill,wheel -c "'  + name + '" -s /bin/bash ' + username
            os.system(useradd)          
            os.system(user_password + " | " + "chpasswd -c SHA512")
        else:
            useradd ='useradd -m -G audio,video,network,storage,rfkill -c "'  + name + '" -s /bin/bash ' + username
            os.system(useradd)
            os.system(user_password + " | " + "chpasswd -c SHA512")
        GLib.idle_add(Functions.show_in_app_notification, self, "User has been created")
    else:
        GLib.idle_add(Functions.show_in_app_notification, self, "Passwords are not the same")
        Functions.MessageBox(self, "Message", "Passwords are not the same")


