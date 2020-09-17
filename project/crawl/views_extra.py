### This view contains typo suggestion and auto-completion function

from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint
import json, time
from django.contrib.auth.decorators import login_required
from .models import History, Blogs
from django.contrib.auth.models import User
from .trie import Trie
from django.db.models import Q


# In actual, the trie will be built only for once and new words will be added in real time
# That trie module will be used further for different features


# Auto complete feature
# input 'ag' => ['age', 'agee', 'agree']
@login_required
def autoComplete(request, word):

	list = ['age',
	'agee',
	'agree',
	'bowl',
	'ball',
	'bat',
	'bark',
	'ba',
	'bench',
	'bet',
	'bery',
	'blink',
	'blie',]

	t = Trie()
	for words in list:
		t.insert(words)

	# Call auto function and print words
	print(t.auto(word))
	return HttpResponse('All words printed on console')


# Typo suggestion feature
# input 'agxe' => ['age', 'agee', 'agree']
@login_required
def typoSuggest(request, word):

	list = ['age',
	'agee',
	'agree',
	'bowl',
	'ball',
	'bat',
	'bark',
	'ba',
	'bench',
	'bet',
	'bery',
	'blink',
	'blie',]

	t = Trie()
	for words in list:
		t.insert(words)

	# Call suggest function and print words
	print(t.suggest(word))
	return HttpResponse('All related words are printed on console')
