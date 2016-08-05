#!/usr/bin/env python

import sys
import mechanize
import json

def explore(url):
    br = mechanize.Browser()
    br.set_handle_robots(False)

    try:
        br.open(url)
    except Exception as e:
        print e

    link_list = []
    try:
        for link in br.links():
            if link.url.startswith("http"):
			    link_list.append(link.url)
    except Exception as e:
        print e

    tree[url] = link_list

    for i in link_list:
        if i not in tree.keys():
            tree[i] = []

tree = {}

if(len(sys.argv) == 1): #explore current tree
	try:
		with open('map.json', 'r') as f:
			tree = json.loads(f.read())
	except Exception as e:
		print e
		print "failed to load"
        tree = {}
    if len(tree) == 0:
        print "Give a root url first"  #can't explore empty tree
    else:
        explored = False
        for i in tree.keys():
            if len(tree[i]) == 0: #haven't explored here yet, let's do it
                explored = True
                explore(i)
           if explored: break
	if tree:
		with open('map.json', 'w') as f:
			json.dump(tree, f)
else: #start new tree
	root_site = sys.argv[1]
	explore(root_site)
	if tree: #check if tree is empty
		with open('map.json', 'w') as f:
			json.dump(tree, f)

