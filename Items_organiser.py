import os, re, shutil, pynotify

#pynotify.init("image")
path = '/home/manhattan/Downloads/'
a=[]
for item in os.walk(path):
    a.append(item)

for s in a[0][2]:
    if re.search(r'(.jpg)$|(.jpeg)$|(.png)$|(.gif)$|(.ico)$',s.lower()):
        if os.path.exists(path+'Images/'+s):
            os.remove(path+s)
            #pynotify.Notification("Deleted",s+" already exists in Images/","/usr/share/icons/gnome/24x24/actions/edit-clear.png").show()
        else:
            shutil.move(path+s,path+'Images/')
            #pynotify.Notification("Moved",s+" to Images/","/usr/share/icons/gnome/24x24/actions/edit-redo.png").show()

    elif re.search(r'(.mp3)$|(.wma)$|(.ogg)$|(.amr)$|(.wav)$',s.lower()):
        if os.path.exists(path+'Music/'+s):
            os.remove(path+s)
            #pynotify.Notification("Deleted",s+" already exists in Music/","/usr/share/icons/gnome/24x24/actions/edit-clear.png").show()
        else:
            shutil.move(path+s,path+'Music/')
            #pynotify.Notification("Moved",s+" to Music/","/usr/share/icons/gnome/24x24/actions/edit-redo.png").show()

    elif re.search(r'(.zip)$|(.tar)$|(.tar.gz)$|(.tar.bz2)$|(.rar)$|(.7z)$|(.tar.7z)$',s.lower()):
        if os.path.exists(path+'Compressed Archives/'+s):
            os.remove(path+s)
            #pynotify.Notification("Deleted",s+" already exists in Compressed Archives/","/usr/share/icons/gnome/24x24/actions/edit-clear.png").show()
        else:
            shutil.move(path+s,path+'Compressed Archives/')
            #pynotify.Notification("Moved",s+" to Compressed Archives/","/usr/share/icons/gnome/24x24/actions/edit-redo.png").show()

    elif re.search(r'(.avi)$|(.mp4)$|(.wmv)$|(.3gp)$|(.mkv)$|(.flv)$|(.webm)$',s.lower()):
        if os.path.exists(path+'Videos/'+s):
            os.remove(path+s)
            #pynotify.Notification("Deleted",s+" already exists in Videos/","/usr/share/icons/gnome/24x24/actions/edit-clear.png").show()
        else:
            shutil.move(path+s,path+'Videos/')
            #pynotify.Notification("Moved",s+" to Videos/","/usr/share/icons/gnome/24x24/actions/edit-redo.png").show()
    
    elif re.search(r'(.doc)$|(.xls)$|(.ppt)$|(.odf)$|(.odt)$|(.txt)$|(.rtf)$',s.lower()):
        if os.path.exists(path+'Documents/'+s):
            os.remove(path+s)
            #pynotify.Notification("Deleted",s+" already exists in Documents/","/usr/share/icons/gnome/24x24/actions/edit-clear.png").show()
        else:
            shutil.move(path+s,path+'Documents/')
            #pynotify.Notification("Moved",s+" to Documents/","/usr/share/icons/gnome/24x24/actions/edit-redo.png").show()

    elif re.search(r'(.exe)$|(.msi)$|(.reg)$',s.lower()):
        if os.path.exists(path+'Windows Installers/'+s):
            os.remove(path+s)
            #pynotify.Notification("Deleted",s+" already exists in Windows Installers/","/usr/share/icons/gnome/24x24/actions/edit-clear.png").show()
        else:
            shutil.move(path+s,path+'Windows Installers/')
            #pynotify.Notification("Moved",s+" to Windows Installers/","/usr/share/icons/gnome/24x24/actions/edit-redo.png").show()

    elif re.search(r'(.c)$|(.py)$|(.vim)$|(.cpp)$|(.sql)',s.lower()):
        if os.path.exists(path+'Serious Stuff/'+s):
            os.remove(path+s)
            #pynotify.Notification("Deleted",s+" already exists in Serious Stuff/","/usr/share/icons/gnome/24x24/actions/edit-clear.png").show()
        else:
            shutil.move(path+s,path+'Serious Stuff/')
            #pynotify.Notification("Moved",s+" to Serious Stuff/","/usr/share/icons/gnome/24x24/actions/edit-redo.png").show()

    elif re.search(r'(.pdf)$',s.lower()):
        if os.path.exists(path+'PDFs/'+s):
            os.remove(path+s)
            #pynotify.Notification("Deleted",s+" already exists in PDFs/","/usr/share/icons/gnome/24x24/actions/edit-clear.png").show()
        else:
            shutil.move(path+s,path+'PDFs/')
            #pynotify.Notification("Moved",s+" to PDFs/","/usr/share/icons/gnome/24x24/actions/edit-redo.png").show()

    elif re.search(r'(.deb)$',s.lower()):
        if os.path.exists(path+'Linux Installers/'+s):
            os.remove(path+s)
            #pynotify.Notification("Deleted",s+" already exists in Linux Installers/","/usr/share/icons/gnome/24x24/actions/edit-clear.png").show()
        else:
            shutil.move(path+s,path+'Linux Installers/')
            #pynotify.Notification("Moved",s+" to Linux Installers/","/usr/share/icons/gnome/24x24/actions/edit-redo.png").show()

    elif re.search(r'(.htm)$|(.html)$|(.php)$',s.lower()):
        if os.path.exists(path+'Webpages/'+s):
            os.remove(path+s)
            #pynotify.Notification("Deleted",s+" already exists in Webpages/","/usr/share/icons/gnome/24x24/actions/edit-clear.png").show()
        else:
            shutil.move(path+s,path+'Webpages/')
            #pynotify.Notification("Moved",s+" to Webpages/","/usr/share/icons/gnome/24x24/actions/edit-redo.png").show()

    else:
        if re.match(r'search',s):
            os.remove(path+s)
            #pynotify.Notification("Deleted",s+" Useless Search file","/usr/share/icons/gnome/24x24/actions/edit-clear.png").show()
        elif os.path.exists(path+'Miscellaneous/'+s):
            os.remove(path+s)
            #pynotify.Notification("Deleted",s+" already exists in Miscellaneous/","/usr/share/icons/gnome/24x24/actions/edit-clear.png").show()
        else:
            shutil.move(path+s,path+'Miscellaneous/')
            #pynotify.Notification("Moved",s+" to Miscellaneous/","/usr/share/icons/gnome/24x24/actions/edit-redo.png").show()
