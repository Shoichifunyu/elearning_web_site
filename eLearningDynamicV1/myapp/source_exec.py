import bs4 #ライブラリbs4をインポートする
from jinja2 import Template
import string
import yaml

#bs4で定義された関数を使ってsample.htmlを読み取る
html = open('../templates/myapp/learn_aws_tests_one_template.html')
html_read = html.read()
print(html_read)
template = Template(html_read)
with open('../templates/myapp/learn_aws_tests.yaml') as file:
    obj = yaml.safe_load(file)
# print(obj['array'][0])
base_data = {}
for num in range(len(obj['array'])):
    print("num:"+str(num))
    for key, value in obj['array'][num].items():
        data = {
        key+str(num) : value,
        # 's1-'+str(num) : question['s1'],
        # 's2-'+str(num) : question['s2'],
        # 's3-'+str(num) : question['s3'],
        # 's4-'+str(num) : question['s4'],
        # 'a-'+str(num) : question['a'],
        # 'a_des-'+str(num) : question['a_des'],
        }

        base_data = {**base_data, **data}
print(base_data)
out = template.render(base_data)
# print(template)
with open("../templates/myapp/test.html", "w") as f:
    f.write(out)

print("書き込みが完了しました")