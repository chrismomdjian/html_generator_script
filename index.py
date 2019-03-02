from classes import classes
from welcome_email_template import welcome_template
from overdue_email_template import overdue_template

for _class in classes:
    className   = classes[_class]["class_name"]
    classLink   = classes[_class]["class_link"]
    surveyLink  = classes[_class]["survey_link"]
    classImg    = classes[_class]["class_img"]

    # welcome email
    f = open("template_files/welcome_templates/{}_welcome.html".format(className), "w")

    welcomeContent = welcome_template(className, classImg, classLink, surveyLink)

    f.write(welcomeContent)
    f.close()

    # overdue email
    f2 = open("template_files/overdue_templates/{}_overdue.html".format(className), "w")

    overdueContent = overdue_template(className, classImg, classLink, surveyLink)

    f2.write(overdueContent)
    f2.close()
