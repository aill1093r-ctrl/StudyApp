[app]
title = StudyApp
package.name = studyapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,plyer
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, POST_NOTIFICATIONS, FOREGROUND_SERVICE
services = StudyService:service.py
