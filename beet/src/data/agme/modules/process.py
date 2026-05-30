def process_dialogs(dialogs, options_index_list=()):
    options_index = 0
    new_dialogs = []
    for dialog_index, dialog in enumerate(dialogs):
        after = []
        if "menu" in dialog:
            end_label = f'__menu.{".".join([f"{i[0]}" for i in options_index_list] + [str(options_index)])}.next'
            for option_index, option in enumerate(dialog['menu']):
                for key, value in option.items():
                    if isinstance(value, str):
                        continue
                    next_options_index = options_index_list + ((options_index, option_index),)
                    label = f'__menu.{".".join(f"{i[0]}_{i[1]}" for i in next_options_index)}'
                    after.append({"label": label})
                    after.extend(process_dialogs(value, options_index_list=next_options_index))
                    after.append({"jump": end_label})
                    option[key] = label
            after.append({"label": end_label})
            options_index += 1
        new_dialogs.append(dialog)
        new_dialogs.extend(after)
    return new_dialogs