from jinja2 import Template
import string
import yaml
import re

def convert_list_elements(my_list, data):
    converted_list = re.sub(r"\|(\w+)\|", lambda match: data.get(match.group(1), match.group()), my_list)
    # converted_list.append(converted_item)
    return converted_list

html_template = '../templates/myapp/learn_react_contents_one_template.html'
yaml_contents = '../templates/myapp/learn_react_contents_one.yaml'
html_product = '../templates/myapp/learn_react_contents_one.html'

open_template = open(html_template)
read_template = open_template.read()
processing_template = Template(read_template)

with open(yaml_contents) as open_yaml:
    load_yaml = yaml.safe_load(open_yaml)
    
collect_data = {}
for section_cnt in range(len(load_yaml['array'])):
    print("num:"+str(section_cnt))
    for title, description in load_yaml['array'][section_cnt].items():
        section_num = section_cnt + 1
        print(title+str(section_num))
        section_data = {
        title+str(section_num) : description,
        }

        collect_data = {**collect_data, **section_data}
print(collect_data)
render_template = processing_template.render(collect_data)
print(render_template)
results = convert_list_elements(render_template, collect_data)
print(results)
with open(html_product, "w") as f:
    f.write(results)

print("書き込みが完了しました")