#  Copyright> YEAR:2022 WHO:Sergey Efimov EMAIL:kilitary@gmail.com WHERE:RUSSIA WHY:L

import os
import subprocess


def _generate_share_dictionary(headerRow):
    """Accepts a variable width, white space delimited string that we attempt
        to divine column delimiters from. Returns a dictionary of field names
        and a tuple with start/stop slice positions"""

    # This used to be a more complex problem before I realized I didn't have
    # to do GET * in my source. GET Name, Path greatly simplifies
    # but this code is generic so I keep it as is

    header = headerRow
    fields = header.split()
    tempOrds = {}
    ords = {}
    # Populate the temporary ordinals dictionary with field name and the
    # starting, zero based, ordinal for it.
    # i.e. given
    # Name     Path
    # 01234567890123456789
    # we would expect Name:0, Path:9
    for field in fields:
        tempOrds[field] = headerRow.index(field)

    # Knowing our starting ordinal positions, we will build a dictionary of tuples
    # that contain starting and ending positions of our fields
    for iter in range(0, len(fields) - 1):
        ords[fields[iter]] = (tempOrds[fields[iter]], tempOrds[fields[iter + 1]])

    # handle the last element
    ords[fields[-1]] = (tempOrds[fields[-1]], len(headerRow))

    return ords

def get_network_shares():
    """Use WMIC to get the full share list. Needed because "net share" isn't parseable"""
    _command = r"C:\Windows\System32\wbem\WMIC.exe /output:stdout /namespace:\\root\cimv2 path Win32_Share GET Name, Path"
    # _command = r"C:\Windows\System32\wbem\WMIC.exe /output:stdout /namespace:\\root\cimv2 path Win32_Share GET *"
    _results = subprocess.check_output(_command, shell=True).decode('UTF-8')

    _headerRow = _results.splitlines()[0]
    headerOrdinals = _generate_share_dictionary(_headerRow)

    _shares = parse_network_shares_name_path(headerOrdinals, _results)
    return _shares

def parse_network_shares_name_path(header, results):
    """Rip apart the results using our header dictionary"""
    _shares = {}
    # use the above to slice into our results
    # skipping first line since it is header
    for _line in results.splitlines():
        if _line:
            _shares[_line[header["Name"][0]: header["Name"][1]].rstrip()] = _line[header["Path"][0]: header["Path"][1]].rstrip()
    return _shares

def translate_local_path_to_share(currentPath):
    """Convert the supplied path to the best match in the shares list"""
    shareName = ""
    defaultShare = ""
    shares = get_network_shares()

    # find the first share match
    if currentPath in shares.values():
        shareName = [key for key, value in shares.items() if value == currentPath][0]
    else:
        # see if we can find a partial match
        # favor longest path
        best = ""
        pathLength = 0
        for share, path in shares.items():
            # path can be empty due to IPC$ share
            if path:
                # Is the share even applicable?
                if path in currentPath:
                    # Favor the non default/admin share (DriveLetter$)
                    if share.endswith('$'):
                        defaultShare = currentPath.replace(path[:-1], share)
                    else:
                        if len(path) > pathLength:
                            shareName = currentPath.replace(path[:-1], share)

        # No other share was found
        if defaultShare and not shareName:
            shareName = defaultShare
    x = os.path.join(r"\\" + os.environ['COMPUTERNAME'], shareName)
    print("Current folder {} maps to {}".format(currentPath, x))

    return os.path.join(r"\\" + os.environ['COMPUTERNAME'], shareName)

def main():
    current = os.getcwd()
    # current = "C:\WINDOWS"
    share = translate_local_path_to_share(current)
    print("{} aka {}".format(current, share))

if __name__ == "__main__":
    main()
