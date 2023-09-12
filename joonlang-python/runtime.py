import sys

class Joon:
    def __init__(self) -> None:
        self.data = {}
        self.start_marker = "하시면 어떻게든 됩니다."
        self.end_marker = "끝내는 것도 자유입니다."
        self.operators = ["네?", "에?", "워터밤"]
    
    def read_joon_file(self, filename) -> None:
        try:
            with open(filename, 'r', encoding="UTF-8") as joon_file:
                lines = joon_file.readlines()
                val, message = self.validate_joon_code(lines)
                if val:
                    for line in lines:
                        l = line.strip()
                        if l != self.start_marker and l != self.end_marker and l != '' and not l.startswith('#'):
                            self.check_type(l)
                else:
                    if message == self.start_marker:
                        print("에러: 어떻게 하셔도 안되네요?")
                    elif message == self.end_marker:
                        print("에러: 진짜 끝내버렸네....")

        except FileNotFoundError:
            print(f"에러: 안타깝네요 '{filename}'가 없네요.")
    
    def validate_joon_code(self, lines) -> bool and str:
        if len(lines) < 2:
            return False, "여러분 그럴 시간에 코드 한 줄 더 쓰세요."
        
        start_marker = "하시면 어떻게든 됩니다."
        end_marker = "끝내는 것도 자유입니다."
        
        if lines[0].strip() != start_marker:
            return False, start_marker
        if lines[-1].strip() != end_marker:
            return False, end_marker
        
        return True, None
    
    # calculate values from 네?, 에?, and 워터밤 with variables
    def calculate_val(self, line) -> int:
        vals = line.split(" ")
        for i in range(len(vals)):
            v = vals[i].replace("님", '')
            # print(v)
            if "네?" in v or "에?" in v:
                n = v.count("네")
                e = v.count('에')
                total = n - e
                if total < 0:
                    total = str(total)
                else:
                    total = "+" + str(total)
                vals[i] = total
            elif v in self.data:
                vals[i] = str(self.data[v])
            elif v == "워터밤":
                vals[i] = "*"
        string_exec = ""
        for s in vals:
            string_exec += s
        try:
            num = eval(string_exec)
            return num
        except:
            raise Exception("안타깝네요. 문법 공부 더하고 오세요.")

    def calculate_output(self, line):
        vars = line.split(' ')
        return_string = ""
        for i in range(len(vars)):
            v = vars[i]
            if "님맥사세요" in v:
                v = v.replace("님맥사세요", '')
                if "!" in v:
                    v = v.replace("!", '')
                if v in self.data:
                    v = self.data[v]
                    if vars[i].endswith('!'):
                        v = chr(v)
                    return_string += str(v)
                elif "네?" in v or "에?" in v:
                    n = v.count("네")
                    e = v.count('에')
                    total = n - e
                    return_string += str(total)
            elif v == "선택은자유입니다":
                    return_string += ' '
        return return_string

    def check_type(self, line) -> None:
        if "님이말씀해보세요" in line:
            self.parse_var(line)
        elif "님?" in line:
            self.parse_assign(line)
        elif "자러가시는거에요" in line:
            self.parse_loop(line)
        elif "님맥사세요" in line:
            self.parse_output(line)
        elif "그냥여쭤^^보는거에요" in line:
            self.parse_condition(line)
    
    # 님이말씀해보세요
    def parse_var(self, line):
        var = line.split("님이말씀해보세요")
        if var[0] == '':
            raise Exception("안타깝네요. 변수 어디갔습니까?")
        elif var[1] != '':
            raise Exception("차고로 와. 말씀 뒤에 추가적으로 허용안합니다.")
        elif var[0] in self.operators:
            raise Exception("너도 데앤할래? 변수와 연산자가 같을수 없어요.")
        self.data[var[0]] = 0

    # 님?
    def parse_assign(self, line):
        var = line.split("님? ")
        if var[0] == '':
            raise Exception("안타깝네요. 변수 어디갔습니까?")
        if var[0] not in  self.data:
            raise Exception("안타깝네요. 변수 선언 어디갔습니까?")
        elif var[0] in self.operators:
            raise Exception("너도 데앤할래? 변수와 연산자가 같을수 없어요.")
        val = self.calculate_val(var[1])
        self.data[var[0]] += val

    # 자러가시는거에요
    def parse_loop(self, line):
        pass

    # 님맥사세요
    def parse_output(self, line):
        output = self.calculate_output(line)
        print(output)

    # 그냥여쭤^^보는거에요
    def parse_condition(self, line):
        pass