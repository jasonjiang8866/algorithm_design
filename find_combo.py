from itertools import combinations
#given a list, lenght of subset and a number, return the subset whose total sum is equal to the number given
class find_combo:
    def __init__(self, lst, num):
        self.lst=lst
        self.num=num

    def combo(self):
        return combinations(self.lst,self.num)

    def sum_combo(self):
        result={}
        for item in self.combo():
            if sum(item) not in result:
                result[sum(item)]=[item]
            else:
                result[sum(item)].append(item)
        return result

    def diff_combo(self):
        result={}
        for item in self.combo():
            if abs(item[0]-item[1]) not in result:
                result[abs(item[0]-item[1])]=[item]
            else:
                result[abs(item[0]-item[1])].append(item)
        return result

    def show_me_result(self, num):
        summy=self.sum_combo()
        diffy=self.diff_combo()
        return {'sum':summy[num],'diff':diffy[num]}
