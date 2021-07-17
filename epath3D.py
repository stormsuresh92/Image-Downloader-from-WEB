from requests_html import HTMLSession
import os

s = HTMLSession()


def left_column(foldername):
    os.mkdir(os.path.join(os.getcwd(), foldername))
    os.chdir(os.path.join(os.getcwd(), foldername))
    r = s.get('https://www.epath3d.com/templates.php')
    titles = r.html.find('li')
    for title in titles:
        try:
            text = title.full_text.strip()
        except:
            pass
        img = 'https://www.epath3d.com/templates/' + text + '.jpg'
        
        try:
            with open (text.replace(' ', '_') + '.jpg', 'wb') as f:
                r = s.get(img)
                f.write(r.content)
        except:
            pass
        
left_column('images')