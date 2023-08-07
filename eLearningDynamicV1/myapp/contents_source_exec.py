from jinja2 import Template
import string
import yaml
import re

def convert_list_elements(my_list, data):
    converted_list = re.sub(r"\|(\w+)\|", lambda match: data.get(match.group(1), match.group()), my_list)
    # converted_list.append(converted_item)
    return converted_list

html = open('../templates/myapp/learn_git_contents_one_template.html')
html_read = html.read()
template = Template(html_read)
with open('../templates/myapp/learn_git_contents.yaml') as file:
    obj = yaml.safe_load(file)
# print(obj['array'][0])
base_data = {}
for num in range(len(obj['array'])):
    print("num:"+str(num))
    for k, v in obj['array'][num].items():
        e = num+1
        print(k+str(e))
        data = {
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
with open("../templates/myapp/learn_git_contents_one.html", "w") as f:
    f.write(results)

print("書き込みが完了しました")