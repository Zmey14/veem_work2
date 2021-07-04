import sys
import hashlib


def main():
    if len(sys.argv) != 3:
        print("main.py path_file path_dir ")
        sys.exit()
    else:
        path_file = sys.argv[1]
        path_dir = sys.argv[2]
        
        try:
            with open(path_file, 'r') as f:
                for line in f:
                    if len(line.split()) == 3:
                        file_name = line.strip().split()[0]
                        alg = line.strip().split()[1]
                        hash = line.strip().split()[2]
                        KEEP = 65536
                        md5 = hashlib.md5()
                        sha1 = hashlib.sha1()
                        sha256 = hashlib.sha256()
                        try:
                            with open(path_dir + file_name, 'rb') as x:
                                while True:
                                    data = x.read(KEEP)
                                    if not data:
                                        break
                                    md5.update(data)
                                    sha1.update(data)
                                    sha256.update(data)

                            if alg == 'md5':
                                hash_sum = md5.hexdigest()
                            elif alg == 'sha1':
                                hash_sum = sha1.hexdigest()
                            elif alg == 'sha256':
                                hash_sum = sha256.hexdigest()
                            else:
                                print(file_name, "Error heshing")

                            if hash == hash_sum:
                                print(file_name, "OK")
                            else:
                                print(file_name, "FAIL")

                        except FileNotFoundError:
                            print(file_name, "NOT FOUND")
                    else:
                        print(file_name, "Error format input")
        except FileNotFoundError:
            print('FileNotFoundError')
            sys.exit()

if __name__ == '__main__':
    main()