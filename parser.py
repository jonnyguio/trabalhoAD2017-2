import re
with open("teste.txt", "r") as n_f:
    lines = n_f.readlines()
    result = []
    for line in lines:
        st = ""
        for line in lines:
            if "E[Nq1]" not in result:
                st = "E[Nq1]" if st == "" else st
                if "E[Nq1]" in line and "p" not in line and "&" not in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                elif "E[Nq1]" in line and "p" in line and "&" in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                    result.append("E[Nq1]")
                    break
            elif "E[Nq2]" not in result:
                st = "E[Nq2]" if st == "" else st
                if "E[Nq2]" in line and "p" not in line and "&" not in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                elif "E[Nq2]" in line and "p" in line and "&" in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                    result.append("E[Nq2]")
                    break
            elif "E[N1]" not in result:
                st = "E[N1]" if st == "" else st
                if "E[N1]" in line and "p" not in line and "&" not in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                elif "E[N1]" in line and "p" in line and "&" in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                    result.append("E[N1]")
                    break
            elif "E[N2]" not in result:
                st = "E[N2]" if st == "" else st
                if "E[N2]" in line and "p" not in line and "&" not in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                elif "E[N2]" in line and "p" in line and "&" in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                    result.append("E[N2]")
                    break
            elif "E[T1]" not in result:
                st = "E[T1]" if st == "" else st
                if "E[T1]" in line and "p" not in line and "&" not in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                elif "E[T1]" in line and "p" in line and "&" in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                    result.append("E[T1]")
                    break
            elif "E[T2]" not in result:
                st = "E[T2]" if st == "" else st
                if "E[T2]" in line and "p" not in line and "&" not in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                elif "E[T2]" in line and "p" in line and "&" in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                    result.append("E[T2]")
                    break
            elif "E[W1]" not in result:
                st = "E[W1]" if st == "" else st
                if "E[W1]" in line and "p" not in line and "&" not in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                elif "E[W1]" in line and "p" in line and "&" in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                    result.append("E[W1]")
                    break
            elif "E[W2]" not in result:
                st = "E[W2]" if st == "" else st
                if "E[W2]" in line and "p" not in line and "&" not in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                elif "E[W2]" in line and "p" in line and "&" in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                    result.append("E[W2]")
                    break
            elif "V[W1]" not in result:
                st = "V[W1]" if st == "" else st
                if "V[W1]" in line and "p" not in line and "&" not in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                elif "V[W1]" in line and "p" in line and "&" in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                    result.append("V[W1]")
                    break
            elif "V[W2]" not in result:
                st = "V[W2]" if st == "" else st
                if "V[W2]" in line and "p" not in line and "&" not in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                elif "V[W2]" in line and "p" in line and "&" in st:
                    number = re.match(r".*(\d+)\.(\d+)", line)
                    st = st + " & " + "{}.{}".format(number.group(1), number.group(2))
                    result.append("V[W2]")
                    break
        print(st)