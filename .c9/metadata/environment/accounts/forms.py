{"filter":false,"title":"forms.py","tooltip":"/accounts/forms.py","ace":{"folds":[],"scrolltop":255.453125,"scrollleft":0,"selection":{"start":{"row":40,"column":42},"end":{"row":40,"column":42},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":17,"state":"start","mode":"ace/mode/python"}},"hash":"ee27a8cb8d4c3e6085963073b8ec4bd599400985","undoManager":{"mark":46,"position":46,"stack":[[{"start":{"row":0,"column":24},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":1,"column":0},"end":{"row":3,"column":50},"action":"insert","lines":["from django.contrib.auth.models import User","from django.contrib.auth.forms import UserCreationForm","from django.core.exceptions import ValidationError"],"id":3}],[{"start":{"row":10,"column":58},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"remove","lines":["    "],"id":5}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":12,"column":0},"end":{"row":23,"column":0},"action":"insert","lines":["class UserRegistrationForm(UserCreationForm):","    \"\"\"Form used to register a new user\"\"\"","","    password = forms.CharField(widget=forms.PasswordInput)","    password2 = forms.CharField(","        label=\"Password Confirmation\",","        widget=forms.PasswordInput)","    ","    class Meta:","        model = User","        fields = ['email', 'username', 'password1', 'password2']",""],"id":7}],[{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["1"],"id":8}],[{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"remove","lines":["1"],"id":9}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "],"id":10}],[{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["#"]}],[{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":["i"],"id":12},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":[" "],"id":13},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["h"]},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["a"]},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":[" "],"id":14},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["t"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["o"]}],[{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":[" "],"id":15},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["b"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":[" "],"id":16},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["o"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["n"]}],[{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["l"],"id":17},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["y"]}],[{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":[" "],"id":18},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["p"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":["a"]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["s"]},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["w"],"id":19},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["o"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["r"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["d"]}],[{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":[" "],"id":20},{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"insert","lines":["t"]},{"start":{"row":15,"column":33},"end":{"row":15,"column":34},"action":"insert","lines":["o"]}],[{"start":{"row":15,"column":34},"end":{"row":15,"column":35},"action":"insert","lines":[" "],"id":21},{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"insert","lines":["u"]},{"start":{"row":15,"column":36},"end":{"row":15,"column":37},"action":"insert","lines":["s"]},{"start":{"row":15,"column":37},"end":{"row":15,"column":38},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":38},"end":{"row":15,"column":39},"action":"insert","lines":[" "],"id":22},{"start":{"row":15,"column":39},"end":{"row":15,"column":40},"action":"insert","lines":["t"]},{"start":{"row":15,"column":40},"end":{"row":15,"column":41},"action":"insert","lines":["h"]},{"start":{"row":15,"column":41},"end":{"row":15,"column":42},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":42},"end":{"row":15,"column":43},"action":"insert","lines":[" "],"id":23},{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"insert","lines":["d"]},{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"insert","lines":["j"]},{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"insert","lines":["a"]},{"start":{"row":15,"column":46},"end":{"row":15,"column":47},"action":"insert","lines":["n"]},{"start":{"row":15,"column":47},"end":{"row":15,"column":48},"action":"insert","lines":["d"]},{"start":{"row":15,"column":48},"end":{"row":15,"column":49},"action":"insert","lines":["o"]}],[{"start":{"row":15,"column":49},"end":{"row":15,"column":50},"action":"insert","lines":[" "],"id":24},{"start":{"row":15,"column":50},"end":{"row":15,"column":51},"action":"insert","lines":["p"]},{"start":{"row":15,"column":51},"end":{"row":15,"column":52},"action":"insert","lines":["a"]},{"start":{"row":15,"column":52},"end":{"row":15,"column":53},"action":"insert","lines":["s"]},{"start":{"row":15,"column":53},"end":{"row":15,"column":54},"action":"insert","lines":["w"]}],[{"start":{"row":15,"column":53},"end":{"row":15,"column":54},"action":"remove","lines":["w"],"id":25}],[{"start":{"row":15,"column":53},"end":{"row":15,"column":54},"action":"insert","lines":["s"],"id":26},{"start":{"row":15,"column":54},"end":{"row":15,"column":55},"action":"insert","lines":["w"]},{"start":{"row":15,"column":55},"end":{"row":15,"column":56},"action":"insert","lines":["o"]},{"start":{"row":15,"column":56},"end":{"row":15,"column":57},"action":"insert","lines":["r"]},{"start":{"row":15,"column":57},"end":{"row":15,"column":58},"action":"insert","lines":["d"]}],[{"start":{"row":15,"column":58},"end":{"row":15,"column":59},"action":"insert","lines":[" "],"id":27},{"start":{"row":15,"column":59},"end":{"row":15,"column":60},"action":"insert","lines":["p"]},{"start":{"row":15,"column":60},"end":{"row":15,"column":61},"action":"insert","lines":["r"]},{"start":{"row":15,"column":61},"end":{"row":15,"column":62},"action":"insert","lines":["o"]},{"start":{"row":15,"column":62},"end":{"row":15,"column":63},"action":"insert","lines":["p"]},{"start":{"row":15,"column":63},"end":{"row":15,"column":64},"action":"insert","lines":["e"]},{"start":{"row":15,"column":64},"end":{"row":15,"column":65},"action":"insert","lines":["r"]},{"start":{"row":15,"column":65},"end":{"row":15,"column":66},"action":"insert","lines":["t"]},{"start":{"row":15,"column":66},"end":{"row":15,"column":67},"action":"insert","lines":["i"]},{"start":{"row":15,"column":67},"end":{"row":15,"column":68},"action":"insert","lines":["e"]},{"start":{"row":15,"column":68},"end":{"row":15,"column":69},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":69},"end":{"row":15,"column":70},"action":"insert","lines":["."],"id":28}],[{"start":{"row":15,"column":70},"end":{"row":15,"column":71},"action":"insert","lines":[" "],"id":29},{"start":{"row":15,"column":71},"end":{"row":15,"column":72},"action":"insert","lines":["C"]},{"start":{"row":15,"column":72},"end":{"row":15,"column":73},"action":"insert","lines":["a"]},{"start":{"row":15,"column":73},"end":{"row":15,"column":74},"action":"insert","lines":["n"]}],[{"start":{"row":15,"column":74},"end":{"row":15,"column":75},"action":"insert","lines":["n"],"id":30},{"start":{"row":15,"column":75},"end":{"row":15,"column":76},"action":"insert","lines":["o"]},{"start":{"row":15,"column":76},"end":{"row":15,"column":77},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":77},"end":{"row":15,"column":78},"action":"insert","lines":[" "],"id":31},{"start":{"row":15,"column":78},"end":{"row":15,"column":79},"action":"insert","lines":["b"]},{"start":{"row":15,"column":79},"end":{"row":15,"column":80},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":80},"end":{"row":15,"column":81},"action":"insert","lines":[" "],"id":32},{"start":{"row":15,"column":81},"end":{"row":15,"column":82},"action":"insert","lines":["d"]},{"start":{"row":15,"column":82},"end":{"row":15,"column":83},"action":"insert","lines":["i"]},{"start":{"row":15,"column":83},"end":{"row":15,"column":84},"action":"insert","lines":["f"]},{"start":{"row":15,"column":84},"end":{"row":15,"column":85},"action":"insert","lines":["e"]},{"start":{"row":15,"column":85},"end":{"row":15,"column":86},"action":"insert","lines":["r"]},{"start":{"row":15,"column":86},"end":{"row":15,"column":87},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":86},"end":{"row":15,"column":87},"action":"remove","lines":["e"],"id":33},{"start":{"row":15,"column":85},"end":{"row":15,"column":86},"action":"remove","lines":["r"]},{"start":{"row":15,"column":84},"end":{"row":15,"column":85},"action":"remove","lines":["e"]}],[{"start":{"row":15,"column":84},"end":{"row":15,"column":85},"action":"insert","lines":["r"],"id":34},{"start":{"row":15,"column":85},"end":{"row":15,"column":86},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":85},"end":{"row":15,"column":86},"action":"remove","lines":["e"],"id":35},{"start":{"row":15,"column":84},"end":{"row":15,"column":85},"action":"remove","lines":["r"]}],[{"start":{"row":15,"column":84},"end":{"row":15,"column":85},"action":"insert","lines":["r"],"id":36}],[{"start":{"row":15,"column":84},"end":{"row":15,"column":85},"action":"remove","lines":["r"],"id":37}],[{"start":{"row":15,"column":84},"end":{"row":15,"column":85},"action":"insert","lines":["f"],"id":38},{"start":{"row":15,"column":85},"end":{"row":15,"column":86},"action":"insert","lines":["e"]},{"start":{"row":15,"column":86},"end":{"row":15,"column":87},"action":"insert","lines":["r"]},{"start":{"row":15,"column":87},"end":{"row":15,"column":88},"action":"insert","lines":["e"]},{"start":{"row":15,"column":88},"end":{"row":15,"column":89},"action":"insert","lines":["n"]},{"start":{"row":15,"column":89},"end":{"row":15,"column":90},"action":"insert","lines":["t"]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":["#"],"id":39}],[{"start":{"row":16,"column":59},"end":{"row":16,"column":60},"action":"insert","lines":[" "],"id":40},{"start":{"row":16,"column":60},"end":{"row":17,"column":0},"action":"insert","lines":["",""]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":17,"column":4},"end":{"row":19,"column":35},"action":"insert","lines":["password1 = forms.CharField(","        label=\"Password\",","        widget=forms.PasswordInput)"],"id":41}],[{"start":{"row":16,"column":60},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":42},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":["#"]}],[{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":[" "],"id":43},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["W"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":[" "],"id":44}],[{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"remove","lines":[" "],"id":45},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"remove","lines":["e"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"remove","lines":["W"]},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"remove","lines":[" "]},{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"remove","lines":["#"]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":27,"column":64},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":46},{"start":{"row":28,"column":0},"end":{"row":28,"column":8},"action":"insert","lines":["        "]},{"start":{"row":28,"column":8},"end":{"row":29,"column":0},"action":"insert","lines":["",""]},{"start":{"row":29,"column":0},"end":{"row":29,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":8},"action":"remove","lines":["    "],"id":47}],[{"start":{"row":29,"column":4},"end":{"row":46,"column":24},"action":"insert","lines":["def clean_email(self):","        email = self.cleaned_data.get('email')","        username = self.cleaned_data.get('username')","        if User.objects.filter(email=email).exclude(username=username):","            raise forms.ValidationError(u'Email address must be unique')","        return email","","    def clean_password2(self):","        password1 = self.cleaned_data.get('password1')","        password2 = self.cleaned_data.get('password2')","","        if not password1 or not password2:","            raise ValidationError(\"Please confirm your password\")","        ","        if password1 != password2:","            raise ValidationError(\"Passwords must match\")","        ","        return password2"],"id":48}]]},"timestamp":1567939119239}