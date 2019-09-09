{"filter":false,"title":"settings.py","tooltip":"/django_auth/settings.py","undoManager":{"mark":53,"position":53,"stack":[[{"start":{"row":27,"column":18},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":28,"column":1},"end":{"row":28,"column":61},"action":"insert","lines":["ALLOWED_HOSTS = [os.environ.get(\"C9_HOSTNAME\"), '127.0.0.1']"],"id":3}],[{"start":{"row":27,"column":17},"end":{"row":27,"column":19},"action":"insert","lines":["''"],"id":4}],[{"start":{"row":27,"column":18},"end":{"row":27,"column":86},"action":"insert","lines":["dbfeec08f9a3407f8235018204ae74e3.vfs.cloud9.us-east-1.amazonaws.com'"],"id":5}],[{"start":{"row":27,"column":85},"end":{"row":27,"column":87},"action":"remove","lines":["''"],"id":6}],[{"start":{"row":27,"column":85},"end":{"row":27,"column":86},"action":"insert","lines":["\""],"id":7}],[{"start":{"row":27,"column":85},"end":{"row":27,"column":86},"action":"remove","lines":["\""],"id":8}],[{"start":{"row":27,"column":85},"end":{"row":27,"column":86},"action":"insert","lines":["'"],"id":9}],[{"start":{"row":28,"column":34},"end":{"row":28,"column":45},"action":"remove","lines":["C9_HOSTNAME"],"id":10},{"start":{"row":28,"column":34},"end":{"row":28,"column":49},"action":"insert","lines":["AWS_C9_HOSTNAME"]}],[{"start":{"row":27,"column":0},"end":{"row":27,"column":1},"action":"insert","lines":["#"],"id":11}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"remove","lines":["#"],"id":12}],[{"start":{"row":39,"column":33},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":15},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":14},"action":"insert","lines":["'accounts'"],"id":16}],[{"start":{"row":40,"column":14},"end":{"row":40,"column":15},"action":"insert","lines":[","],"id":17}],[{"start":{"row":121,"column":23},"end":{"row":122,"column":0},"action":"insert","lines":["",""],"id":18}],[{"start":{"row":123,"column":0},"end":{"row":123,"column":74},"action":"insert","lines":["MESSAGE_STORAGE = \"django.contrib.messages.storage.session.SessionStorage\""],"id":19}],[{"start":{"row":123,"column":74},"end":{"row":124,"column":0},"action":"insert","lines":["",""],"id":20}],[{"start":{"row":58,"column":17},"end":{"row":58,"column":52},"action":"insert","lines":["os.path.join(BASE_DIR, 'templates')"],"id":21}],[{"start":{"row":123,"column":74},"end":{"row":124,"column":0},"action":"insert","lines":["",""],"id":22}],[{"start":{"row":125,"column":0},"end":{"row":125,"column":64},"action":"insert","lines":["EMAIL_BACKEND = \"django.core.mail.backends.console.EmailBackend\""],"id":23}],[{"start":{"row":124,"column":0},"end":{"row":125,"column":0},"action":"insert","lines":["",""],"id":24}],[{"start":{"row":125,"column":0},"end":{"row":125,"column":1},"action":"insert","lines":["#"],"id":25},{"start":{"row":125,"column":1},"end":{"row":125,"column":2},"action":"insert","lines":["T"]},{"start":{"row":125,"column":2},"end":{"row":125,"column":3},"action":"insert","lines":["o"]}],[{"start":{"row":125,"column":3},"end":{"row":125,"column":4},"action":"insert","lines":[" "],"id":26},{"start":{"row":125,"column":4},"end":{"row":125,"column":5},"action":"insert","lines":["s"]},{"start":{"row":125,"column":5},"end":{"row":125,"column":6},"action":"insert","lines":["e"]},{"start":{"row":125,"column":6},"end":{"row":125,"column":7},"action":"insert","lines":["n"]}],[{"start":{"row":125,"column":7},"end":{"row":125,"column":8},"action":"insert","lines":[" "],"id":27}],[{"start":{"row":125,"column":7},"end":{"row":125,"column":8},"action":"remove","lines":[" "],"id":28}],[{"start":{"row":125,"column":7},"end":{"row":125,"column":8},"action":"insert","lines":["d"],"id":29}],[{"start":{"row":125,"column":8},"end":{"row":125,"column":9},"action":"insert","lines":[" "],"id":30},{"start":{"row":125,"column":9},"end":{"row":125,"column":10},"action":"insert","lines":["e"]},{"start":{"row":125,"column":10},"end":{"row":125,"column":11},"action":"insert","lines":["m"]},{"start":{"row":125,"column":11},"end":{"row":125,"column":12},"action":"insert","lines":["a"]},{"start":{"row":125,"column":12},"end":{"row":125,"column":13},"action":"insert","lines":["i"]},{"start":{"row":125,"column":13},"end":{"row":125,"column":14},"action":"insert","lines":["l"]}],[{"start":{"row":125,"column":14},"end":{"row":125,"column":15},"action":"insert","lines":[" "],"id":31},{"start":{"row":125,"column":15},"end":{"row":125,"column":16},"action":"insert","lines":["t"]},{"start":{"row":125,"column":16},"end":{"row":125,"column":17},"action":"insert","lines":["o"]}],[{"start":{"row":125,"column":17},"end":{"row":125,"column":18},"action":"insert","lines":[" "],"id":32},{"start":{"row":125,"column":18},"end":{"row":125,"column":19},"action":"insert","lines":["t"]},{"start":{"row":125,"column":19},"end":{"row":125,"column":20},"action":"insert","lines":["h"]},{"start":{"row":125,"column":20},"end":{"row":125,"column":21},"action":"insert","lines":["e"]}],[{"start":{"row":125,"column":21},"end":{"row":125,"column":22},"action":"insert","lines":[" "],"id":33},{"start":{"row":125,"column":22},"end":{"row":125,"column":23},"action":"insert","lines":["c"]},{"start":{"row":125,"column":23},"end":{"row":125,"column":24},"action":"insert","lines":["o"]},{"start":{"row":125,"column":24},"end":{"row":125,"column":25},"action":"insert","lines":["n"]},{"start":{"row":125,"column":25},"end":{"row":125,"column":26},"action":"insert","lines":["s"]},{"start":{"row":125,"column":26},"end":{"row":125,"column":27},"action":"insert","lines":["o"]},{"start":{"row":125,"column":27},"end":{"row":125,"column":28},"action":"insert","lines":["l"]},{"start":{"row":125,"column":28},"end":{"row":125,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":126,"column":0},"end":{"row":126,"column":1},"action":"insert","lines":["#"],"id":34}],[{"start":{"row":126,"column":65},"end":{"row":127,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":127,"column":0},"end":{"row":128,"column":0},"action":"insert","lines":["",""]},{"start":{"row":128,"column":0},"end":{"row":128,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":128,"column":1},"end":{"row":128,"column":2},"action":"insert","lines":[" "],"id":36},{"start":{"row":128,"column":2},"end":{"row":128,"column":3},"action":"insert","lines":["T"]},{"start":{"row":128,"column":3},"end":{"row":128,"column":4},"action":"insert","lines":["o"]},{"start":{"row":128,"column":4},"end":{"row":128,"column":5},"action":"insert","lines":["s"]},{"start":{"row":128,"column":5},"end":{"row":128,"column":6},"action":"insert","lines":["e"]},{"start":{"row":128,"column":6},"end":{"row":128,"column":7},"action":"insert","lines":["n"]},{"start":{"row":128,"column":7},"end":{"row":128,"column":8},"action":"insert","lines":["d"]}],[{"start":{"row":128,"column":8},"end":{"row":128,"column":9},"action":"insert","lines":[" "],"id":37},{"start":{"row":128,"column":9},"end":{"row":128,"column":10},"action":"insert","lines":["r"]},{"start":{"row":128,"column":10},"end":{"row":128,"column":11},"action":"insert","lines":["e"]},{"start":{"row":128,"column":11},"end":{"row":128,"column":12},"action":"insert","lines":["a"]},{"start":{"row":128,"column":12},"end":{"row":128,"column":13},"action":"insert","lines":["l"]}],[{"start":{"row":128,"column":13},"end":{"row":128,"column":14},"action":"insert","lines":[" "],"id":38}],[{"start":{"row":128,"column":13},"end":{"row":128,"column":14},"action":"remove","lines":[" "],"id":39},{"start":{"row":128,"column":12},"end":{"row":128,"column":13},"action":"remove","lines":["l"]},{"start":{"row":128,"column":11},"end":{"row":128,"column":12},"action":"remove","lines":["a"]},{"start":{"row":128,"column":10},"end":{"row":128,"column":11},"action":"remove","lines":["e"]},{"start":{"row":128,"column":9},"end":{"row":128,"column":10},"action":"remove","lines":["r"]}],[{"start":{"row":128,"column":9},"end":{"row":128,"column":10},"action":"insert","lines":["a"],"id":40},{"start":{"row":128,"column":10},"end":{"row":128,"column":11},"action":"insert","lines":["c"]},{"start":{"row":128,"column":11},"end":{"row":128,"column":12},"action":"insert","lines":["t"]},{"start":{"row":128,"column":12},"end":{"row":128,"column":13},"action":"insert","lines":["u"]},{"start":{"row":128,"column":13},"end":{"row":128,"column":14},"action":"insert","lines":["a"]},{"start":{"row":128,"column":14},"end":{"row":128,"column":15},"action":"insert","lines":["l"]}],[{"start":{"row":128,"column":15},"end":{"row":128,"column":16},"action":"insert","lines":[" "],"id":41},{"start":{"row":128,"column":16},"end":{"row":128,"column":17},"action":"insert","lines":["e"]},{"start":{"row":128,"column":17},"end":{"row":128,"column":18},"action":"insert","lines":["m"]},{"start":{"row":128,"column":18},"end":{"row":128,"column":19},"action":"insert","lines":["a"]},{"start":{"row":128,"column":19},"end":{"row":128,"column":20},"action":"insert","lines":["i"]},{"start":{"row":128,"column":20},"end":{"row":128,"column":21},"action":"insert","lines":["l"]}],[{"start":{"row":128,"column":21},"end":{"row":129,"column":0},"action":"insert","lines":["",""],"id":42}],[{"start":{"row":129,"column":0},"end":{"row":133,"column":16},"action":"insert","lines":["EMAIL_USE_TLS = True","EMAIL_HOST = 'smtp.gmail.com'","EMAIL_HOST_USER = os.environ.get(\"EMAIL_ADDRESS\")","EMAIL_HOST_PASSWORD = os.environ.get(\"EMAIL_PASSWORD\")","EMAIL_PORT = 587"],"id":43}],[{"start":{"row":128,"column":4},"end":{"row":128,"column":5},"action":"insert","lines":[" "],"id":44}],[{"start":{"row":127,"column":0},"end":{"row":128,"column":0},"action":"insert","lines":["",""],"id":45}],[{"start":{"row":128,"column":0},"end":{"row":128,"column":2},"action":"insert","lines":["\"\""],"id":46}],[{"start":{"row":128,"column":2},"end":{"row":128,"column":3},"action":"insert","lines":["\""],"id":47}],[{"start":{"row":134,"column":16},"end":{"row":135,"column":0},"action":"insert","lines":["",""],"id":48},{"start":{"row":135,"column":0},"end":{"row":136,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":136,"column":0},"end":{"row":136,"column":2},"action":"insert","lines":["\"\""],"id":49}],[{"start":{"row":136,"column":2},"end":{"row":136,"column":3},"action":"insert","lines":["\""],"id":50}],[{"start":{"row":126,"column":0},"end":{"row":126,"column":1},"action":"remove","lines":["#"],"id":51}],[{"start":{"row":136,"column":3},"end":{"row":137,"column":0},"action":"insert","lines":["",""],"id":52},{"start":{"row":137,"column":0},"end":{"row":138,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":138,"column":0},"end":{"row":141,"column":1},"action":"insert","lines":["AUTHENTICATION_BACKENDS = [","    'django.contrib.auth.backends.ModelBackend',","    'accounts.backends.EmailAuth'","]"],"id":53}],[{"start":{"row":126,"column":0},"end":{"row":126,"column":1},"action":"insert","lines":["#"],"id":54}],[{"start":{"row":128,"column":0},"end":{"row":128,"column":2},"action":"remove","lines":["\"\""],"id":55}],[{"start":{"row":128,"column":0},"end":{"row":128,"column":1},"action":"remove","lines":["\""],"id":56},{"start":{"row":128,"column":0},"end":{"row":129,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":135,"column":2},"end":{"row":135,"column":3},"action":"remove","lines":["\""],"id":57},{"start":{"row":135,"column":1},"end":{"row":135,"column":2},"action":"remove","lines":["\""]},{"start":{"row":135,"column":0},"end":{"row":135,"column":1},"action":"remove","lines":["\""]},{"start":{"row":134,"column":0},"end":{"row":135,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":1471.15625,"scrollleft":0,"selection":{"start":{"row":121,"column":23},"end":{"row":121,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":113,"state":"start","mode":"ace/mode/python"}},"timestamp":1568022344852,"hash":"f33e2f733c143392f4e20421a399b3c0043eefd1"}