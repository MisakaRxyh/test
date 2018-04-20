from app.drawimg import Drawimg


# 用于统计处理从数据库中获取到的职位信息
class Parse:
    def resultParse(name, count, citylist, salarylist, educationlist):
        if count:
            info_count = {
                'skillName': name,
                'positionCount': count,
                'mainCity': {
                    'firstCity': citylist[0][0],
                    'secondCity': citylist[1][0],
                    'thirdCity': citylist[2][0],
                },
                'mainSalary': salarylist[0][0],
                'mainEducation': educationlist[0][0],
            }
        else:
            info_count = {}
        print(info_count)
        return info_count

    def PositionCount(result):
        count = 0
        for c in result:
            count += 1
        return count

    def CityParse(result):
        citylist = {}
        for r in result:
            if r[3] not in citylist.keys():
                citylist[r[3]] = 1
            else:
                citylist[r[3]] += 1
        print(citylist)
        citylist = sorted(citylist.items(), key=lambda c: c[1], reverse=True)
        print(citylist)
        return citylist

    def SalaryParse(result):
        salarylist = {
            '2k-5k': 0,
            '5k-10k': 0,
            '10k-15k': 0,
            '15k-20k': 0,
            '20k以上': 0,
        }
        for r in result:
            low = int(r[4].lower().split('k', 1)[0])
            str = r[4].lower().split('k')[1].split('-')
            if len(str) == 2:
                high = int(r[4].lower().split('k')[1].split('-')[1])
            elif len(str) == 1:
                high = low
            avg = (low + high) / 2
            if avg >= 2 and avg < 5:
                salarylist['2k-5k'] += 1
            elif avg >= 5 and avg < 10:
                salarylist['5k-10k'] += 1
            elif avg >= 10 and avg < 15:
                salarylist['10k-15k'] += 1
            elif avg >= 15 and avg < 20:
                salarylist['15k-20k'] += 1
            elif avg >= 20:
                salarylist['20k以上'] += 1
        salarylist = sorted(salarylist.items(), key=lambda c: c[1], reverse=True)
        print(salarylist)
        return salarylist

    def EducationParse(result):
        educationlist = {}
        for r in result:
            if r[5] not in educationlist.keys():
                educationlist[r[5]] = 1
            else:
                educationlist[r[5]] += 1
        educationlist = sorted(educationlist.items(), key=lambda c: c[1], reverse=True)
        print(educationlist)
        return educationlist

    def pathParse(path):
        path = path.split('\\', 2)[2].replace('\\', '/')
        path = '/' + path
        oldsignal = ['+', '#']
        newsignal = [r'%2B', r'%23']
        for s in oldsignal:
            if s in path:
                i = oldsignal.index(s)
                path.replace(s, newsignal[i])
                print(i, s, newsignal[i])
        print(path)
        return path

    def getReslut(result, name):
        name = name
        pc = Parse.PositionCount(result)
        cp = Parse.CityParse(result)
        sp = Parse.SalaryParse(result)
        ep = Parse.EducationParse(result)
        result = Parse.resultParse(name, pc, cp, sp, ep)
        return result
