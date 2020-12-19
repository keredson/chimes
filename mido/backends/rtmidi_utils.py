def expand_alsa_port_name(port_names, name):
    if name is None:
        return None

    for port_name in port_names:
        if name == port_name:
            return name

        # Try without client and port number (for example 128:0).
        without_numbers = port_name.rsplit(None, 1)[0]
        if name == without_numbers:
            return port_name

        if ':' in without_numbers:
            without_client = without_numbers.split(':', 1)[1]
            if name == without_client:
                return port_name
    else:
        # Let caller deal with it.
        return name
