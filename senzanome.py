import os
import glob
import itertools
import shutil
import markdown2
from distutils.dir_util import copy_tree
from string import Template
import config

def clear():
    dirname = os.path.join(os.getcwd(), config.OUT_DIR)
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
        print(" ")
        print(" [✓] Cleared previous build")

def copy_static_files():
    in_dir = os.path.join(os.getcwd(), config.SRC_DIR, 'static')
    out_dir = os.path.join(os.getcwd(), config.OUT_DIR)
    if (os.path.exists(in_dir)):
        print(" ")
        print(" Copying files...")
        copy_tree(in_dir, out_dir)
        print(" [✓] Copied static files")
        print(" ")

def get_out_filename(path):
    # strip 1st and 2nd level dirs from path. ie, converts "a/b/c/d.md" to "c/d.md"
    return os.path.join(*(path.split(os.path.sep)[3:])).replace(".md", ".html")

def parse(path):
    file = open(path, "r")
    return markdown2.markdown(file.read(), extras=["metadata"])

def make_template(path):
    template_path = os.path.join(os.getcwd(), config.SRC_DIR, path)
    template_file = open(template_path, "r")
    return Template(template_file.read())

def render(template, content):
    return template.substitute(**content)

def create_index(src, list_template_src, item_template_src):
    paths = glob.glob(src)

    list_template = make_template(list_template_src)
    item_template = make_template(item_template_src)
    
    items = []

    for path in paths:
        node = parse(path)
        node.metadata['url'] = get_out_filename(file.name)
        item = render(item_template, node.metadata)
        items.append(item)

    nodes = render(list_template, { 'content': "".join(items)})
    return nodes

def create_page(name, out_name, template_src, sections):
    page = render(make_template(template_src), sections)
    root = render(make_template(config.ROOT_TEMPLATE_SRC), { 'title': name, 'content': page })

    save_node(out_name, root)

def create_node(filename, node, template_src):
    root_template = make_template(config.ROOT_TEMPLATE_SRC)
    content_template = make_template(template_src)

    content = render(content_template, dict(**node.metadata, **{ 'content': node }))
    root = render(root_template, dict(**node.metadata, **{ 'content':content }))

    save_node(filename, root)

    return {
        'path': filename,
        'contents': node,
    }

def save_node(filename, content):
    out_path = os.path.join(os.getcwd(), config.OUT_DIR, filename)
    out_dir = os.path.dirname(out_path)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    out_file = open(out_path, "w")
    out_file.write(content)
    print(" [✓] Built", out_path)

def create_nodes(src, template_src):
    paths = glob.glob(src)
    
    print(" ")
    print(" Building from %d source(s)" % len(paths))

    for path in paths:
        content = parse(path)
        filename = get_out_filename(file.name)
        create_node(filename, content, template_src)

