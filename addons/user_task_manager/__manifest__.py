{
    'name': 'user task manager',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'manage user task efficiently',
    'description': """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse nec consectetur sapien. Ut sit amet 
     lacus arcu. Praesent a tortor bibendum, semper quam sed, semper sem. """,
     'author': 'Milagros',
     'website': 'https://miweb.com',
     'depends': ["base"],
     'data': [
        "security/task_security.xml",
        "security/ir.model.access.csv",
        "views/task_views.xml",
     ],
     'installable': True,
     'application': True,




   

}