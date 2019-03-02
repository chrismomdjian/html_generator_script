def welcome_template(className, classImg, classLink, surveyLink):
    htmlContent = '''
    <html>
        <head>
            <title>{class_name}</title>
        </head>
        <body>
            <h1>Welcome, %FirstName%!</h1>
            <p>Class Image</p>
            <img src="{class_img}" />

            <br />

            <p>Class Link</p>
            <a href="{class_link}">{class_link}</a>

            <br />

            <p>Class Survey</p>
            <a href="{survey_link}">{survey_link}</a>
        </body>
    </html>
    '''.format(class_name=className, class_img=classImg, class_link=classLink, survey_link=surveyLink)

    return htmlContent
