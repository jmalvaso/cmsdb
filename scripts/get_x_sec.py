def get_xsec_values(process, energy):
    """
    Recursively retrieve the xsec values for the given process and its sub-processes.
    
    :param process: The process to retrieve xsec values for.
    :param energy: The energy level to retrieve xsec values for.
    :return: A list of tuples containing process names and their xsec values.
    """
    xsec_values = []
    
    if energy in process.xsecs:
        xsec = process.xsecs[energy]
        xsec_values.append((process.name, xsec))
        
    # Check for sub-processes if they exist
    if hasattr(process, 'subprocesses') and process.subprocesses:
        for sub_process in process.subprocesses:
            xsec_values.extend(get_xsec_values(sub_process, energy))
        
    return xsec_values

def save_xsecs_to_file(processes, filename, energy):
    """
    Save the xsec values of the processes to a file.
    
    :param processes: List of processes to save xsec values for.
    :param filename: The name of the file to save the xsec values to.
    :param energy: The energy level to save xsec values for.
    """
    with open(filename, 'w') as file:
        for process in processes:
            xsec_values = get_xsec_values(process, energy)
            for name, xsec in xsec_values:
                file.write(f"{name}: {xsec}\n")