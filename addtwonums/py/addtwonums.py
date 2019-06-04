#!/usr/bin/python

from typing import List

"""
You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order and each of their nodes 
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the 
number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode)-> ListNode:
        carry_ = 0
        run1 = l1
        run2 = l2
        ret_ = None
        run_ret = None

        while run1 and run2:
            sum_ = run1.val + run2.val + carry_

            if not ret_:
                ret_ = ListNode(sum_ % 10)
                run_ret = ret_
            else:
                run_ret.next = ListNode(sum_ % 10)
                run_ret = run_ret.next
            carry_ = sum_ // 10
            run1 = run1.next
            run2 = run2.next
        else:
            while run1:
                sum_ = run1.val + carry_
                if not ret_:
                    ret_ = ListNode(sum_ % 10)
                    run_ret = ret_
                else:
                    run_ret.next = ListNode(sum_ % 10)
                    run_ret = run_ret.next
                carry_ = sum_ // 10
                run1 = run1.next
            while run2:
                sum_ = run2.val + carry_
                if not ret_:
                    ret_ = ListNode(sum_ % 10)
                    run_ret = ret_
                else:
                    run_ret.next = ListNode(sum_ % 10)
                    run_ret = run_ret.next
                carry_ = sum_ // 10
                run2 = run2.next
            if carry_:
                run_ret.next = ListNode(carry_)

        return ret_
            

    def print_solution(self, input: ListNode):
        r_list = []
        runner = input

        while runner:
            r_list.insert(0, runner.val)
            runner = runner.next

        print(''.join(map(str, r_list)))

    def build_listnode(self, input: List[int])-> ListNode:
        m = None
        rm = None
        for i in input:
            if not m:
                m = ListNode(i)
                rm = m
            else:
                rm.next = ListNode(i)
                rm = rm.next
        return m
