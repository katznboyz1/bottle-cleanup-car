.
├── README.md: the readme with information about this project
├── main.py: the main program that will control the speed and all of that stuff
├── requirements.txt: the PIP requirements
├── .speedtime: the last time that the speed was updated by the main program (used as a timeout to make sure that the program didnt stop responding to speed updates, to help prevent a physical crash of the car)
└── web
    ├── app.py: the flask app for the web interface
    └── templates
        └── index.html: the homepage for the web interface