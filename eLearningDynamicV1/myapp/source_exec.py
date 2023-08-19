from jinja2 import Template
import string
import yaml
import re

def convert_list_elements(my_list, data):
    # converted_list = []
    # for item in my_list:
        # 正規表現を使用してマスタッシュ記法の変数を抽出し、対応する値で置換する
    # converted_list = re.sub(r"\{\{(\w+)\}\}", lambda match: data.get(match.group(1), match.group()), my_list)
    converted_list = re.sub(r"\|(\w+)\|", lambda match: data.get(match.group(1), match.group()), my_list)
    # converted_list.append(converted_item)
    return converted_list

#文字化けしている可能性がある為、learn_git_tests_two_template.htmlは要確認
html = open('../templates/myapp/learn_electric_circuit_tests_two_template.html')
html_read = html.read()
template = Template(html_read)
with open('../templates/myapp/learn_electric_circuit_tests_two.yaml') as file:
    obj = yaml.safe_load(file)
# print(obj['array'][0])
base_data = {}
for num in range(len(obj['array'])):
    print("num:"+str(num))
    for k, v in obj['array'][num].items():
        e = num+1
        print(k+str(e))
        data = {
        # ここはnumdではなく、eを指定する
        k+str(num+1) : v,
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
print(out)
results = convert_list_elements(out, base_data)
print(results)
with open("../templates/myapp/learn_electric_circuit_tests_two.html", "w") as f:
    f.write(results)

print("書き込みが完了しました")