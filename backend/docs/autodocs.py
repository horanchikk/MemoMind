# -*- coding: utf-8 -*-
import os
import re

from jinja2 import FileSystemLoader, Environment, select_autoescape


class AutoDocs:
    MD_RULES = [
        # colorize numbers
        (r'(-?\d+)', r'<span class="text-orange-400">\1</span>'),
        # code
        # ```lang
        # source code
        # ```
        (r'```([\w_]+)\s+([\s\S]+?)\s+```', r'<pre><code class="language-\1">\2</code></pre>'),
        # code `example`
        (r'`([^`\n]*?)`', r'<div class="flex"><div class="flex bg-fore/[0.1] px-4 rounded-lg h-min">\1</div></div>'),
        # list
        # - element
        (r'((\n *- +[^\n]+)+)', r'<ul class="flex flex-col gap-1 pl-4 list-disc">\1</ul>'),
        (r'\n *- +([^\n]+)', r'<li>\1</li>'),
        # horizontal line
        # ---
        (r'---', r'<div class="flex h-[0.5px] bg-fore w-2/3 self-center"></div>'),
        # links
        # [link text](URL)
        (r'\[([^]]+)]\((https?://[^\s)]+)\)',
         r'<a id="\1" target="_blank" rel="noopener noreferrer" href="\2" class="text-pink-300">\1</a>'),
        # anchor link
        # [link text](#other_link)
        (r'\[([\S ]+)]\((#[^\s)]+)\)', r'<a href="\2" class="text-pink-300">\1</a>'),
        # images
        # [!alt](image URL)
        (r'\[!([^\S ]+)]\(([^\s]+)\)', r'<img alt="\1" src="\2">'),
        # italic text
        # **text**
        (r'\*\*([^\n*]+)\*\*', r'<i>\1</i>'),
        # bold text
        # *text*
        (r'\*([^\n*]+)\*', r'<b>\1</b>'),
    ]

    ERRORS_RULES = [
        re.compile(r'([\w_]+) *= *err_response\(\s*(\d+)\s*,\s*("[\S\s]+?")\s*\)'),
        re.compile(r'([\w_]+) *= *error_response\(\s*(\d+)\s*,\s*("[\S\s]+?")\s*\)'),
        re.compile(r'([\w_]+) *= *error\(\s*(\d+)\s*,\s*("[\S\s]+?")\s*\)'),
        re.compile(r'([\w_]+) *= *err\(\s*(\d+)\s*,\s*("[\S\s]+?")\s*\)'),
    ]

    @staticmethod
    def generate(
            root: str = './',
            template_folder: str = 'template',
            template_file: str = 'index.html',
            title: str = 'FastAPI Docs',
            tailwind_config_file: str = 'js/tailwind.config.js',
            models: list[tuple[str, str]] = None,
            methods: list[tuple[str, str]] = None,
            exceptions: list[str] = None,
            api_url: str = 'http://localhost:8000',
            tailwind_colors=None,
            thumb_color: str = 'pink',
            main_stylesheet: str = 'style/main.css',
    ) -> None:
        """Generates FastAPI docs via Jinja2

        Supports:
        - Pydantic models
        - Little markdown (lists, code, links)
        - Highlight.js and tailwind css 3 for template files

        :param root: root path
        :param template_folder: folder with jinja2 templates
        :param template_file: jinja2 template file
        :param tailwind_config_file: tailwind css config file
        :param title: docs title
        :param models: pydantic models
        :param methods: methods description
        :param exceptions: exceptions file
        :param api_url: current api
        :param tailwind_colors: tailwind colors JSON
        :param thumb_color: scrollbar thumb color
        :param main_stylesheet: main stylesheet file
        """
        if models is None:
            models = []
        if exceptions is None:
            exceptions = []
        if tailwind_colors is None:
            tailwind_colors = {
                'back': '#080f11',
                'fore': '#c44b79',
                'code-back': '#acacac',
                'back-light': '#f2cedb',
                'fore-light': '#ee4968',
            }

        if not root.endswith('/'):
            raise ValueError('root param should be ends with "/".')

        env = Environment(
            loader=FileSystemLoader(f'{root}{template_folder}'),
            autoescape=select_autoescape()
        )
        index_template = env.get_template(template_file)
        AutoDocs._tailwind_config_update(root + tailwind_config_file, tailwind_colors)
        AutoDocs._setup_scrollbar(f'{root}{main_stylesheet}', thumb_color)

        models = {i[0]: AutoDocs._add_model(f'{root}{i[1]}', i[0]) for i in models}
        methods_list = []
        for i in methods:
            methods_list.append(i[0])
            methods_list += AutoDocs._add_mount(f'{root}{i[1]}', models, i[0])
        errors_list = []
        for i in exceptions:
            errors_list += AutoDocs._add_error(f'{root}{i}')

        with open(f'{root}{template_file}', 'w', encoding='utf-8') as f:
            f.write(index_template.render(
                title=title,
                methods=methods_list,
                rootpath=root,
                errors=errors_list,
                api_url=api_url
            ))

    @staticmethod
    def _prepare_string_to_md(src: str) -> str:
        """Prepares string into markdown representation

        :param src: source string
        :return: prepared string
        """
        for pattern, replace_pattern in AutoDocs.MD_RULES:
            src = re.sub(pattern, replace_pattern, src)
        return src.strip()

    @staticmethod
    def _tailwind_config_update(
            config_file: str,
            colors: dict
    ):
        """Updates tailwind config

        :param config_file: tailwind.config.js file
        :param colors: dict of colors, where key is color name and value is color
        """
        with open(config_file, 'r', encoding='utf-8') as f:
            data = f.read()
        for key, value in colors.items():
            # key': '#[0-9a-fA-F] -> key': 'value
            data = re.sub(r'(' + key + r")'\s*:\s*'(#[a-f0-9A-F]+)", r"\1': '" + value, data)
        with open(config_file, 'w', encoding='utf-8') as f:
            f.write(data)

    @staticmethod
    def _setup_scrollbar(
            stylesheet: str,
            thumb_color: str
    ):
        """Setups scrollbar color

        :param stylesheet: path/to/main/css/file
        :param thumb_color: new thumb color
        """
        with open(stylesheet, 'r', encoding='utf-8') as f:
            data = f.read()
        # *::-webkit-scrollbar-thumb {background-color: asdasd; ->
        # *::-webkit-scrollbar-thumb {background-color: new color
        data = re.sub(
            r'webkit-scrollbar-thumb *{([\S\s]+?)background-color\s*:\s*[^;]+',
            r'webkit-scrollbar-thumb {\1background-color: ' + thumb_color, data)
        print(data)
        with open(stylesheet, 'w', encoding='utf-8') as f:
            f.write(data)

    @staticmethod
    def _add_error(path: str) -> list[dict[str, any]]:
        """Handles error

        :param path: path to error
        :return: list of errors
        """
        with open(path, 'r', encoding='utf-8') as f:
            module = f.read()

        errors = []
        for pattern in AutoDocs.ERRORS_RULES:
            errors += pattern.findall(module)

        return [{
            'name': i[0].replace('_', ' ').title(),
            'code': int(i[1]),
            'value': i[2]
        } for i in errors]

    @staticmethod
    def _add_model(path: str, model_name: str) -> dict[str, any] | None:
        """Handles model

        :param path: path/to/model
        :param model_name: Model name
        :return: dict of fields or None
        """
        with open(path, 'r', encoding='utf-8') as f:
            module = f.read()

        # ModelName(BaseModel):
        #    """doc
        #    """
        model = re.findall(
            model_name + r'\s*\(\S+\):\s*(\"{3}[^"]+\"{3}\s*)?(([\w_]+ *: *[\w_]+[^\n]*\s*)+)', module
        )
        if model:
            return {
                i[0]: {
                    'type': i[1],
                    'default': i[2].strip().lstrip('=').strip() if i[2] else None,
                    'doc': i[3].split('#')[1].strip() if '#' in i[3] else ''
                }
                for i in re.findall(r'([\w_]+) *: *([\w_\[\]]+)( *= *[^\n#]+)?([^#]*#[^\n]+)?', model[0][1])
            }

    @staticmethod
    def _add_mount(
            path: str,
            models: list[dict[str, any]],
            mount_path: str
    ) -> list[dict[str, any]]:
        """Handles FastAPI mount

        :param path: path/to/mount
        :param models: list of models
        :param mount_path: path in API,
        """
        with open(path, 'r', encoding='utf-8') as f:
            mount = f.read()
        methods = []
        # @get('/method')
        # def method_name(...):
        # """
        # """
        for i in re.findall(r"@[^.]+\.([^(]+)\(([^)]+)\)\s+([\s\S]+?\):)\s+(\"\"\"([\S\s]+?)\"\"\")?", mount):
            docstring = i[3].split('\n')
            # method name
            name = docstring[0]
            # def method_name(
            method_id = re.findall(r'def *([\w_]+)\(', i[2])[0]
            if method_id.startswith('_'):
                continue
            name = method_id.replace('_', ' ') if name else name[3:]
            # method desc
            description = re.findall(r'[^\n]+\s+([\S\s]+?):param', i[3])
            if description:
                description = AutoDocs._prepare_string_to_md(description[0])
                if ':param' in description:
                    description = None
            else:
                description = None
            # method params
            params = []
            json = []
            # :param param_name: param description
            params_result = re.findall(r':param (\S+?): +([^\n]+)', i[3])
            returns_result = re.findall(r':returns?: +([\S\s]+)', i[3])
            # arg_name: arg_type = default_value
            types_result = re.findall(r'([\w_]+) *: *([\w_]+\[[^]]+]|[\w_]+)( *= *([^,]+))?', i[2])
            for t in types_result:
                # Add model json params
                if t[1].endswith('Model'):
                    for field, value in models[t[1]].items():
                        json.append({
                            'name': field,
                            'type': value['type'],
                            'description': value['doc'],
                            'required': value['default'] is None
                        })
                    continue
                # add URL params
                res = list(filter(lambda x: x[0] == t[0], params_result))
                params.append({
                    'name': t[0],
                    'type': t[1],
                    'description': '' if not res else res[0][1],
                    'required': t[2] == ''
                })
            # create method
            method = {
                'name': name,
                'description': description,
                'id': method_id,
                'params': params,
                'json': json,
                'returns': AutoDocs._prepare_string_to_md(returns_result[0][:-3]) if returns_result else None,
                'http': f'{i[0].upper()} {mount_path}{i[1][1:-1]} HTTP/1.1',
            }
            methods.append(method)
        return methods
