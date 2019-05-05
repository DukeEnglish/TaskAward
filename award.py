#!/usr/bin/python
#-*- coding:UTF-8 -*-
#-----------------------------------------------------------------------#
# File Name: awardpy
# Author: Junyi Li
# Personal Page: DukeEnglish.github.io
# Mail: 4ljy@163.com
# Created Time: 2019-05-05
# Description:
#-----------------------------------------------------------------------#

import sys
import random
import json
# 连续100个，可以有一个额外抽奖。100。
# 连续400个，可以有一个额外抽奖 1k。
# 缺少总额控制机制

DAILY_AWARD = 10
EXTRA_DAILY_AWARD = 1000
MINUS_DAILY_AWARD = 0

WEEKLY = 50 # >=100 weekly

MONTH_AWARD = 1000 # >= 400 monthly
EXTRA_AWARD_MONTH = 0

WORK_OUT = 20
COURSERA = 30
# 总额为600 + 额外的 1k奖励 + 月1k奖励 + 周400奖励 = 3k
# 需要添加的是锻炼，看coursera的课程的奖励，完成工作的奖励。思考：这些是否需要添加，毕竟我目前要规范的是平时的SM。
# 其实现在总额并不确定，，，先看看情况吧
TOTAL_MONTH = 2600

def excise_award():
	ea = extra_daily_award()
	print("extra_daily_award", ea)
	print("d_award", WORK_OUT) 
	res = WORK_OUT+ea
	return res

def coursera_award():
	ea = extra_daily_award()
	print("extra_daily_award", ea)
	print("d_award", COURSERA) 
	res = COURSERA+ea
	return res


def extra_daily_award():
	n = random.randint(1,20)
	print("random_sm_prob_num", n)
	if n == 10:
		extra_award = random.randint(MINUS_DAILY_AWARD, (100 if EXTRA_DAILY_AWARD >= 100 else EXTRA_DAILY_AWARD))
		print("TODAY'S EXTRA_DAILY_AWARD:", extra_award)
		return extra_award
	else:
		return 0

def weekly_award():
	prob = random.random()*0.8
	return ((prob+0.2)*WEEKLY)

def monthly_award():
	prob = random.random()*0.9
	return ((prob+0.1)*MONTH_AWARD)


def daily_award(daily_task):
	
	
	d_award = daily_task*DAILY_AWARD/10
	ea = extra_daily_award()
	print("extra_daily_award", ea)
	print("d_award", d_award) 
	res = d_award+ea
	return res

def init_log():
	fr = open("log.txt", "r")
	log_line = fr.readline()
	# print(log_line)
	json_line = json.loads(log_line)
	json_line["daily_award"] = 0
	json_line["weekly_award"] = 0
	json_line["monthly_award"] = 0
	json_line["total_month"] = TOTAL_MONTH
	print("init log done")
	json_log = json.dumps(json_line)
	fr = open("log.txt", "w")
	fr.write(json_log)

def log_excise():
	fr = open("log.txt", "r")
	log_line = fr.readline()
	# print(log_line)
	json_line = json.loads(log_line)
	json_line["total_month"] += excise_award()
	print("excise done")
	json_log = json.dumps(json_line)
	fr = open("log.txt", "w")
	fr.write(json_log)
	
def log_coursera():
	fr = open("log.txt", "r")
	log_line = fr.readline()
	# print(log_line)
	json_line = json.loads(log_line)
	json_line["total_month"] += coursera_award()
	print("coursera done")
	json_log = json.dumps(json_line)
	fr = open("log.txt", "w")
	fr.write(json_log)

def main():

	total_award = 0
	wa = 0
	ma = 0
	# 读取历史奖励数据
	fr = open("log.txt", "r")
	log_line = fr.readline()
	# print(log_line)
	json_line = json.loads(log_line)
	total_d_award = json_line["daily_award"]
	total_w_award = json_line["weekly_award"]
	total_m_award = json_line["monthly_award"]

	print("read log done")
	print("total_d_award", total_d_award)
	print("total_w_award", total_w_award)
	print("total_m_award", total_m_award)
	# 每天奖励结算方法：
	# 完成sm
	daily_task = int(sys.argv[1])
	today_daily_award = daily_award(daily_task)
	print("sm_today_daily_award", today_daily_award)
	# if daily_accumulation > 100
	if total_d_award >=100:
		wa = weekly_award()
		print("You are awarded because of 100 daily_task completed", wa)
		total_d_award = 0
		total_w_award += 1
	if total_w_award >= 4:
		ma = monthly_award()
		print("You are awarded because of 400 daily_task completed", ma)
		total_w_award = 0
		total_m_award += 1
		json_line["total_month"] += TOTAL_MONTH
	if total_m_award >=4:
		print("You are awarded because you have insisted on this for 4 months, program it right now please")

	total_d_award += daily_task
	json_line["daily_award"] = total_d_award
	json_line["weekly_award"] = total_w_award
	json_line["monthly_award"] = total_m_award
	json_log = json.dumps(json_line)
	fr = open("log.txt", "w")
	fr.write(json_log)
	total_award = today_daily_award+ wa + ma
	print("today total award", total_award)
	json_line["total_month"] = json_line["total_month"] - total_award

if __name__ == '__main__':
	if sys.argv[1]=="init":
		init_log()
	elif sys.argv[1]=="e"
		log_excise
	elif sys.argv[1]=="c"
		log_coursera
	else:
		main()
