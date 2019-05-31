def traverse(data, on_dict_item=None, on_list_item=None):

    def traverse_dict(data):
        for k, v in data.iteritems():
            if on_dict_item:
                on_dict_item(data, k, v)
            traverse_data(v)

    def traverse_list(data):
        for i, v in enumerate(data):
            if on_list_item:
                on_list_item(data, i, v)
            traverse_data(v)

    def traverse_data(data):
        if isinstance(data, dict):
            traverse_dict(data)
        elif isinstance(data, list):
            traverse_list(data)

    traverse_data(data)


def decode_geometry(data, decode, keys):

    def on_dict_item(dict, key, value):
        if key in keys:
            dict[key] = decode(value)

    traverse(data, on_dict_item=on_dict_item)
