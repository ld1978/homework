#!/usr/bin/env python
# -*- conding:utf-8 -*-
# __Author__:'liudong'

with open('menu_list.txt', 'r',encoding='utf-8') as states:
    stats=states.read().split()
#print(stats_line)
stats_list=stats[0]+'\n'+stats[7]+'\n'+stats[14]+'\n'+stats[21]
beijing_province=stats[1]+'\n'+stats[3]+'\n'+stats[5]+'\n'
tianjin_province=stats[8]+'\n'+stats[10]+'\n'+stats[12]+'\n'
guangdong_city=stats[15]+'\n'+stats[17]+'\n'+stats[19]+'\n'
zhejiang_city=stats[22]+'\n'+stats[24]+'\n'+stats[26]+'\n'
bejing_haidian=stats[2]+'\n'
beijing_dongcheng=stats[4]+'\n'
beijing_fengtai=stats[6]+'\n'
tianjin_heping=stats[9]+'\n'
tianjin_hexi=stats[11]+'\n'
tianjin_hedong=stats[13]+'\n'
guangdong_guangzhou=stats[16]+'\n'
guangdong_fuoshan=stats[18]+'\n'
guangdong_shenzhen=stats[20]+'\n'
zhejiang_ningbo=stats[23]+'\n'
zhejiang_hangzhou=stats[25]+'\n'
zhejiang_wenzhou=stats[27]+'\n'
def Display_stats(): #显示省市主界面
    print ("-------------------------------------------------")
    print ("重点省市查询:")
    #print ("-------------------------------------------------")
    print(stats_list)   #遍历行政省级地区键值
    print("---------------------------------------------------")
    print('Q[q] for exit')

def display_Beijing():  #显示北京的信息
    print('beijing provinces list:')
    print('---------------------------------------------------')
    print(beijing_province)
    print('---------------------------------------------------')
    print('B[b]:BACK,Q[q]:EXIT')
def display_Tianjin():
    print('Tianjin provinces list')
    print('---------------------------------------------------')
    print(tianjin_province)
    print('---------------------------------------------------')
    print('B[b]:BACK,Q[q]:EXIT')
def display_Guangdong():
    print('GuangDong provinces list')
    print('---------------------------------------------------')
    print(guangdong_city)
    print('---------------------------------------------------')
    print('B[b]:BACK,Q[q]:EXIT')
def display_Zhejiang():
    print('Zhejiang provinces list')
    print('---------------------------------------------------')
    print(zhejiang_city)
    print('---------------------------------------------------')
    print('B[b]:BACK,Q[q]:EXIT')

if __name__ == '__main__':
    Display_stats()
    while True:
        stats_choice=input('Please press number 1-4 for stats information:')
        if stats_choice == 'B' or stats_choice == 'b':
            Display_stats()
        if stats_choice == 'Q' or stats_choice=='q':
            exit()
        else:
            if stats_choice == "1":
                display_Beijing()
                province_choice=input('Press number for province information:')
                if province_choice =='q' or province_choice == 'Q':
                    exit()
                if province_choice == 'b' or province_choice == 'B':
                    display_Beijing()
                if province_choice == '1':
                    print('---------------------------------------------------')
                    print(bejing_haidian)
                    print('---------------------------------------------------')
                    quit_back_choice=input('B[b]:BACK,Q[q]:EXIT]')
                    if quit_back_choice == 'B' or quit_back_choice == 'b':
                        display_Beijing()
                    if quit_back_choice == 'q' or quit_back_choice == 'Q':
                        exit()
                if province_choice == '2':
                    print('---------------------------------------------------')
                    print(beijing_dongcheng)
                    print('---------------------------------------------------')
                    quit_back_choice=input('B[b]:BACK,Q[q]:EXIT]')
                    if quit_back_choice == 'B' or quit_back_choice == 'b':
                        display_Beijing()
                    if quit_back_choice == 'q' or quit_back_choice == 'Q':
                        exit()
                if province_choice == '3':
                    print('---------------------------------------------------')
                    print(beijing_fengtai)
                    print('---------------------------------------------------')
                    quit_back_choice=input('B[b]:BACK,Q[q]:EXIT]')
                    if quit_back_choice == 'B' or quit_back_choice == 'b':
                        display_Beijing()
                    if quit_back_choice == 'q' or quit_back_choice == 'Q':
                        exit()

            if stats_choice == "2":
                display_Tianjin()
                province_choice=input('Press number for provice information:')
                if province_choice =='q' or province_choice == 'Q':
                    exit()
                if province_choice == 'b' or province_choice == 'B':
                    Display_stats()
                if province_choice == '1':
                    print('---------------------------------------------------')
                    print(tianjin_heping)
                    print('---------------------------------------------------')
                    quit_back_choice=input('B[b]:BACK,Q[q]:EXIT]')
                    if quit_back_choice == 'B' or quit_back_choice == 'b':
                        display_Tianjin()
                    if quit_back_choice == 'q' or quit_back_choice == 'Q':
                        exit()
                if province_choice == '2':
                    print('---------------------------------------------------')
                    print(tianjin_hexi)
                    print('---------------------------------------------------')
                    quit_back_choice=input('B[b]:BACK,Q[q]:EXIT]')
                    if quit_back_choice == 'B' or quit_back_choice == 'b':
                        display_Tianjin()
                    if quit_back_choice == 'q' or quit_back_choice == 'Q':
                        exit()
                if province_choice == '3':
                    print('---------------------------------------------------')
                    print(tianjin_hedong)
                    print('---------------------------------------------------')
                    quit_back_choice=input('B[b]:BACK,Q[q]:EXIT]')
                    if quit_back_choice == 'B' or quit_back_choice == 'b':
                        display_Tianjin()
                    if quit_back_choice == 'q' or quit_back_choice == 'Q':
                        exit()

            if stats_choice == "3":
                display_Guangdong()
                province_choice=input('Press number for provice information:')
                if province_choice =='q' or province_choice == 'Q':
                    exit()
                if province_choice == 'b' or province_choice == 'B':
                    Display_stats()
                if province_choice == '1':
                    print('---------------------------------------------------')
                    print(guangdong_guangzhou)
                    print('---------------------------------------------------')
                    quit_back_choice=input('B[b]:BACK,Q[q]:EXIT]')
                    if quit_back_choice == 'B' or quit_back_choice == 'b':
                        display_Guangdong()
                    if quit_back_choice == 'q' or quit_back_choice == 'Q':
                        exit()
                if province_choice == '2':
                    print('---------------------------------------------------')
                    print(guangdong_fuoshan)
                    print('---------------------------------------------------')
                    quit_back_choice=input('B[b]:BACK,Q[q]:EXIT]')
                    if quit_back_choice == 'B' or quit_back_choice == 'b':
                        display_Guangdong()
                    if quit_back_choice == 'q' or quit_back_choice == 'Q':
                        exit()
                if province_choice == '3':
                    print('---------------------------------------------------')
                    print(guangdong_shenzhen)
                    print('---------------------------------------------------')
                    quit_back_choice=input('B[b]:BACK,Q[q]:EXIT]')
                    if quit_back_choice == 'B' or quit_back_choice == 'b':
                        display_Guangdong()
                    if quit_back_choice == 'q' or quit_back_choice == 'Q':
                        exit()

            if stats_choice == "4":
                display_Zhejiang()
                province_choice=input('Press number for provice information:')
                if province_choice =='q' or province_choice == 'Q':
                    exit()
                if province_choice == 'b' or province_choice == 'B':
                    Display_stats()
                if province_choice == '1':
                    print('---------------------------------------------------')
                    print(zhejiang_ningbo)
                    print('---------------------------------------------------')
                    quit_back_choice=input('B[b]:BACK,Q[q]:EXIT]')
                    if quit_back_choice == 'B' or quit_back_choice == 'b':
                        display_Zhejiang()
                    if quit_back_choice == 'q' or quit_back_choice == 'Q':
                        exit()
                if province_choice == '2':
                    print('---------------------------------------------------')
                    print(zhejiang_hangzhou)
                    print('---------------------------------------------------')
                    quit_back_choice=input('B[b]:BACK,Q[q]:EXIT]')
                    if quit_back_choice == 'B' or quit_back_choice == 'b':
                        display_Zhejiang()
                    if quit_back_choice == 'q' or quit_back_choice == 'Q':
                        exit()
                if province_choice == '3':
                    print('---------------------------------------------------')
                    print(zhejiang_wenzhou)
                    print('---------------------------------------------------')
                    quit_back_choice=input('B[b]:BACK,Q[q]:EXIT]')
                    if quit_back_choice == 'B' or quit_back_choice == 'b':
                        display_Zhejiang()
                    if quit_back_choice == 'q' or quit_back_choice == 'Q':
                        exit()


