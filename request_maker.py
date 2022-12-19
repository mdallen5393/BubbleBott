#!/usr/bin/env python3
from sys import argv
from read import get_bubble_id
import requests

def make_url(args):
    if args:
        arr = list(map(strtoplus, args))
        if arr[0] == 'bubble':
            if len(arr) == 1:
                # print('listing bubbles')
                url = f'http://127.0.0.1:5000/list_bubbles'
                response = requests.get(url)
                # print(response.json())
                print_response(response.json())
            else:
                # print(bubble_exists(arr[1]))
                if (bubble_exists(arr[1])):
                    url = f'http://127.0.0.1:5000/list_resources?bubble_name={arr[1]}'
                    # print(url)
                    response = requests.get(url)
                    # print(response.json())
                    print_response(response.json())
                else:
                    print('adding bubble')
                    url = f'http://127.0.0.1:5000/add_bubble?bubble_name={arr[1]}&owner={arr[2]}&desc={arr[3]}'
                    # print(url)
                    response = requests.post(url)
                    # print(response.json())
                    print_response(response.json())
        elif arr[0] == 'add':
            print('adding resource')
            url = f'http://127.0.0.1:5000/add_resource?bubble_name={arr[1]}&owner={arr[2]}&desc={arr[3]}&content={arr[4]}'
            response = requests.post(url)
            # print(response.json())
            print_response(response.json())
        elif arr[0] == 'pop':
            if len(arr) == 2:
                try:
                    print('deleting bubble')
                    url = f'http://127.0.0.1:5000/delete_bubble?bubble_name={arr[1]}'
                    response = requests.delete(url)
                    # print(response.json())
                    print_response(response.json())
                except Exception as e:
                    print(f'An Error Occurred: bubble \'{arr[1]}\' does not exist')
            if len(arr) == 3:
                print('deleting resource')
                url = f'http://127.0.0.1:5000/delete_resource?bubble_name={arr[1]}&idx={arr[2]}'
                response = requests.delete(url)
                # print(response.json())
                print_response(response.json())
        else:
            print('invalid command')

def bubble_exists(name):
    try:
        get_bubble_id(name)
        return True
    except Exception:
        return False

def strtoplus(input):
    plusStr = input.replace(' ', '+')
    return plusStr

def print_response(response_json):
    if isinstance(response_json, list):
        if 'name' in response_json[0]:
            for obj in response_json:
                print(f"\n{obj['name']}: {obj['description']}")
                print(f"\towner: {obj['owner']}\tdate created: {obj['createdAt']}")
        else:
            for obj in response_json:
                # print(obj)
                print(f"\n[{obj['idx']}] {obj['content']}")
                print(f"\t{obj['description']}")
                print(f"\t{obj['owner']}\tdate created: {obj['createdAt']}")
    else:
        if 'name' in response_json:
            print(f"\n{obj['name']}: {obj['description']}")
            print(f"\towner: {obj['owner']}\tdate created: {obj['createdAt']}")
        else:
            print('Success!')
    print()

if __name__ == '__main__':
    make_url(argv[1:])
