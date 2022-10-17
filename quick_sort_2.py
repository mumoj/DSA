versions = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
sequence = [i.split('.') for i in versions if i != ""]
sequence = [[int(i) for i in version ] for version in sequence]
print(sequence)

def quick_sort(sequence):
            
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    versions_greater = []
    versions_lower = []

    def major_version_comparison(version, pivot):
        if version[0] > pivot [0]:
            versions_greater.append(version)
        elif version[0] == pivot[0]:
            return version
        else:
            versions_lower.append(version)


    def minor_version_comparion(version, pivot):
        if version[1] > pivot[1]:
            versions_greater.append(version)
        elif version[1] == pivot[1]:
            return version
        else:
            versions_lower.append(version)

    def revision_version_comparison(version, pivot):
        if version[2] > pivot[2]:
            print(f"Versions Great 1 : {versions_greater}")
            versions_greater.append(version)
        else:
            print(f"Versions Low 1: {versions_lower}")
            versions_lower.append(version)
            print(f"Versions Low 1: {versions_lower}")

    for i, version in enumerate(sequence):
        version = major_version_comparison(version, pivot)
        if version:
            if len(pivot) > 1 and len(version) > 1:

                version = minor_version_comparion(version, pivot)
                print(f"Version Checkpoint {version} - {pivot}")
                if version:
                    print(f"Version Checkpoint 2 {version} - {pivot}")
                    if len(pivot) == 3 and len(version) == 3:
                        revision_version_comparison(version, pivot)
                        print(f"Versions Great : {versions_greater}")
                        print(f"Versions Low : {versions_lower}")
                    elif len(version) == 3 :
                        versions_greater.append(version)
                    else:
                        versions_lower.append(version)
                else:
                    pass

            elif len(version) >1:
                versions_greater.append(version)
            else:
                versions_lower.append(version)
        else:
            pass

  
    print(f"version Lower {versions_lower}")
    print(f"version Greater {versions_greater}")
    print(f"Pivot{pivot}")

    return quick_sort(versions_lower) + [pivot] + quick_sort(versions_greater)
     


s = quick_sort(sequence=sequence)
s = [[str(i) for i in version ] for version in s]

l = [".".join(i) for i in s]

print(l)