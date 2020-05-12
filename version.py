
def checkVersion(version1, version2):
    if version1==version2 or version1 == ''or version2 == '':
        return 0
    MAX_VERSION = "0.0.0"
    versionBITS1 = version1.split(".")
    versionBITS2 = version2.split(".")
    if len(versionBITS1) >= len(versionBITS2):
        minbitversion = versionBITS2
        maxbitversion = versionBITS1
    else:
        minbitversion = versionBITS1
        maxbitversion = versionBITS2
    for index, bit in enumerate(minbitversion):
        try:
            if int(bit) > int(maxbitversion[index]):
                MAX_VERSION = ".".join(minbitversion)
                break
            elif int(bit) < int(maxbitversion[index]):
                MAX_VERSION = ".".join(maxbitversion)
                break
            else:
                MAX_VERSION = ".".join(maxbitversion)
        except IndexError as err:
            pass
    if MAX_VERSION == version1:
        CODE = 1
    elif MAX_VERSION == version2:
        CODE = -1
    else:
        CODE = 0

    return CODE
if __name__ == '__main__':
    version1='1.0.1'
    version2='1.0.0'
    over=checkVersion(version1,version2)
    print(over)