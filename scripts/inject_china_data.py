#!/usr/bin/env python3
"""注入当代中国版新内容到游戏数据文件"""
import json, os

BASE = 'public/data/zh-cn'
SCRIPTS = 'scripts'

with open(f'{BASE}/events.json')        as f: events  = json.load(f)
with open(f'{BASE}/talents.json')       as f: talents = json.load(f)
with open(f'{BASE}/age.json')           as f: ages    = json.load(f)
with open(f'{SCRIPTS}/new_events.json') as f: new_events  = json.load(f)
with open(f'{SCRIPTS}/new_talents.json')as f: new_talents = json.load(f)
with open(f'{SCRIPTS}/new_events_novel.json') as f: new_events_novel = json.load(f)
with open(f'{SCRIPTS}/new_talents_novel.json')as f: new_talents_novel = json.load(f)

events.update(new_events)
events.update(new_events_novel)
talents.update(new_talents)
talents.update(new_talents_novel)

# 当代中国事件年龄分布
age_event_map = {
    "16": ["41000*0.3","41001*0.5","41002*0.3","41004*0.5","41005*0.4","41006*0.3"],
    "17": ["41001*0.5","41003*0.4","41004*0.3","41007*0.5"],
    "18": ["41000*0.3","41002*0.3","41016*0.5","41041*0.5"],
    "19": ["41010*0.5","41011*0.3","41015*0.4","41017*0.4","41041*0.5"],
    "20": ["41010*0.4","41011*0.3","41012*0.3","41013*0.3","41014*0.4","41015*0.3"],
    "21": ["41011*0.3","41013*0.3","41014*0.4","41015*0.3","41016*0.4","41017*0.4"],
    "22": ["41013*0.3","41014*0.3","41016*0.4","41017*0.4","41020*0.4","41041*0.5","41070*5"],
    "23": ["41020*0.4","41021*0.5","41022*0.2","41024*0.4","41028*0.4","41041*0.4"],
    "24": ["41020*0.4","41021*0.5","41022*0.2","41023*0.5","41024*0.4","41026*0.5"],
    "25": ["41021*0.5","41022*0.3","41023*0.5","41024*0.4","41025*0.4","41026*0.4","41027*0.3","41030*0.3","41031*0.5","41040*0.3","41041*0.4","41042*0.2","41044*0.4"],
    "26": ["41021*0.5","41023*0.5","41024*0.4","41025*0.4","41026*0.4","41027*0.3","41030*0.4","41031*0.5","41040*0.3","41041*0.4","41043*0.3"],
    "27": ["41021*0.4","41023*0.4","41025*0.3","41026*0.4","41027*0.4","41030*0.5","41031*0.5","41080*5"],
    "28": ["41022*0.2","41024*0.4","41027*0.3","41029*0.3","41030*0.4","41032*0.4","41033*0.4","41043*0.3","41044*0.3","41045*0.3"],
    "30": ["41024*0.3","41027*0.3","41029*0.3","41030*0.3","41031*0.4","41032*0.4","41033*0.4","41034*0.4","41036*0.3","41043*0.3","41044*0.3","41052*0.3"],
    "32": ["41027*0.3","41029*0.3","41033*0.4","41034*0.4","41035*0.4","41036*0.3","41043*0.3","41044*0.3","41052*0.3"],
    "35": ["41027*0.3","41033*0.3","41034*0.3","41036*0.4","41050*0.5","41051*0.4","41052*0.3","41053*0.4"],
    "38": ["41050*0.5","41051*0.5","41052*0.4","41053*0.4","41054*0.4","41055*0.3","41090*5"],
    "40": ["41050*0.4","41051*0.4","41052*0.3","41053*0.5","41054*0.4","41055*0.3"],
    "45": ["41050*0.3","41051*0.3","41052*0.3","41053*0.5","41054*0.4","41055*0.3"],
    "50": ["41053*0.5","41054*0.4","41055*0.3"],
}

# 诡秘之主世界线事件（条件触发，需天赋4001）
novel_mystery_map = {
    "18": ["42000*3"],
    "19": ["42001*3","42002*3"],
    "20": ["42003*3"],
    "21": ["42004*3","42005*3"],
    "22": ["42006*3"],
    "23": ["42007*3"],
    "24": ["42008*3"],
    "25": ["42009*3"],
    "26": ["42010*3"],
    "27": ["42011*3"],
    "28": ["42012*3"],
    "30": ["42013*3"],
    "33": ["42014*3"],
    "40": ["42015*3"],
    "60": ["42099*3"],
}

# 没钱修什么仙世界线事件（条件触发，需天赋4002）
novel_xianxia_map = {
    "18": ["43000*3"],
    "19": ["43001*3","43002*3"],
    "20": ["43003*3"],
    "21": ["43004*3"],
    "22": ["43005*3"],
    "23": ["43006*3"],
    "24": ["43007*3"],
    "25": ["43008*3"],
    "26": ["43009*3"],
    "27": ["43010*3"],
    "28": ["43011*3"],
    "30": ["43012*3"],
    "32": ["43013*3"],
    "35": ["43014*3"],
    "40": ["43015*3"],
    "60": ["43099*3"],
}

def merge_age_map(base_map, extra_map):
    for age_str, evts in extra_map.items():
        if age_str in base_map:
            base_map[age_str] = base_map[age_str] + evts
        else:
            base_map[age_str] = evts
    return base_map

age_event_map = merge_age_map(age_event_map, novel_mystery_map)
age_event_map = merge_age_map(age_event_map, novel_xianxia_map)

for age_str, new_evts in age_event_map.items():
    if age_str in ages:
        ages[age_str]['event'] = list(ages[age_str]['event']) + new_evts
    else:
        ages[age_str] = {'age': int(age_str), 'event': new_evts}

with open(f'{BASE}/events.json',  'w', encoding='utf-8') as f:
    json.dump(events,  f, ensure_ascii=False, separators=(',',':'))
with open(f'{BASE}/talents.json', 'w', encoding='utf-8') as f:
    json.dump(talents, f, ensure_ascii=False, separators=(',',':'))
with open(f'{BASE}/age.json',     'w', encoding='utf-8') as f:
    json.dump(ages,    f, ensure_ascii=False, separators=(',',':'))

total_new = len(new_events) + len(new_events_novel)
total_new_tlt = len(new_talents) + len(new_talents_novel)
print(f"事件总数: {len(events)}  (新增 {total_new} 个，含小说世界线 {len(new_events_novel)} 个)")
print(f"天赋总数: {len(talents)} (新增 {total_new_tlt} 个，含小说天赋 {len(new_talents_novel)} 个)")
print(f"年龄段更新: {len(age_event_map)} 个")
