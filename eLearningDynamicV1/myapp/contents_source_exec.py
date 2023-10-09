from jinja2 import Template
import string
import yaml
import re

def prepare_generate_html(html_template, yaml_contents):
    open_template = open(html_template)
    read_template = open_template.read()
    process_template = Template(read_template)

    with open(yaml_contents) as open_yaml:
        load_yaml = yaml.safe_load(open_yaml)

    return process_template, load_yaml

def generate_html_contents(load_yaml, process_template):        
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
    render_template = process_template.render(collect_data)
    print(render_template)
    generated_html_contents = convert_list_elements(render_template, collect_data)
    print(generated_html_contents)
    return generated_html_contents

def convert_list_elements(list, data):
    converted_list = re.sub(r"\|(\w+)\|", lambda match: data.get(match.group(1), match.group()), list)
    return converted_list

def make_html_file(generated_html_contents, html_product):
    with open(html_product, "w") as f:
        f.write(generated_html_contents)
    print("書き込みが完了しました")

if __name__ == '__main__':
    html_template = '../templates/myapp/learn_react_contents_one_template.html'
    yaml_contents = '../templates/myapp/learn_react_contents_one.yaml'
    html_product = '../templates/myapp/learn_react_contents_one.html'

    process_template, load_yaml = prepare_generate_html(html_template, yaml_contents)
    generated_html_contents = generate_html_contents(load_yaml, process_template)
    make_html_file(generated_html_contents, html_product)