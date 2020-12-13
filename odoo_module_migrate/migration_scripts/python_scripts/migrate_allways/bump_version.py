def bump_revision(**kwargs):
    tools = kwargs['tools']
    manifest_path = kwargs['manifest_path']
    target_version_name = kwargs['migration_steps'][-1]["target_version_name"]

    import re
    text = tools._read_content(manifest_path)
    old_term = r"('|\")version('|\").*('|\")[0-9]+\.[0-9]+(.*)('|\")"
    text = re.sub(old_term, r'"version": "{0}\4"'.format(target_version_name), text)

    tools._write_content(manifest_path, text)
