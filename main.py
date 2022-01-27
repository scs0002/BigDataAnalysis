import UserTake as UT

if(UT.userres.status_code == 200):
    print(UT.userres.status_code.text)
else:
    print("그런 소환사는 없습니다.")
