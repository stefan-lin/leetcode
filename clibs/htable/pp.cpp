// pp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

#define SIZE 7
#define NEWLINE printf("\n")

typedef struct Item {
	int key;
	int value;
	Item *next;
} Item;

typedef struct Handler {
	int size;
	int count;
	Item **table;
} Handler;

unsigned int hash(unsigned int x) {
	x = ((x >> 16) ^ x) * 0x45d9f3b;
	x = ((x >> 16) ^ x) * 0x45d9f3b;
	x = (x >> 16) ^ x;
	return x;
}

unsigned int unhash(unsigned int x) {
	x = ((x >> 16) ^ x) * 0x119de1f3;
	x = ((x >> 16) ^ x) * 0x119de1f3;
	x = (x >> 16) ^ x;
	return x;
}

int validate_malloc_(void *ptr, const char *message) {
	if (!ptr) {
		printf("[error] malloc %s failed.", message);
		NEWLINE;
		return 0;
	}

	return 1;
}

Handler *construct_(int inital_size) {
	// create handler
	Handler *hdr = (Handler *)malloc(sizeof(Handler));

	if (validate_malloc_(hdr, "Handlr")) {
		// malloc sucess
		hdr->size = inital_size;
		hdr->count = 0;
		hdr->table = (Item **)malloc(sizeof(Item *) * inital_size);

		if (validate_malloc_(hdr->table, "arr Item *")) {
			int idx = 0;
			for (idx; idx < inital_size; idx++) {
				hdr->table[idx] = (Item *)0;
			}
			return hdr;
		}
		//return (validate_malloc_(hdr->table, "arr Item *")) ? hdr : (Handler *)0;
	}

	return 0;
}

int add(Handler *h, unsigned int key, int value) {
	unsigned int h_key = hash(key);
	unsigned int t_idx = h_key % h->size;

	if (h->table[t_idx]) {
		Item *runner = h->table[t_idx];
		while (runner->next) {
			runner = runner->next;
		}
		runner->next = (Item *)malloc(sizeof(Item));
		if (validate_malloc_(runner->next, "runner->next malloc Item")) {
			runner->next->key = key;
			runner->value = value;
			runner->next = (Item *)0;
		}
		else {
			return 0;
		}
	}
	else {
		h->table[t_idx] = (Item *)malloc(sizeof(Item));
		if (validate_malloc_(h->table[t_idx], "h->table[t_idx] malloc Item")) {
			h->table[t_idx]->key = key;
			h->table[t_idx]->value = value;
			h->table[t_idx]->next = (Item *)0;

			(h->count)++;
		}
		else {
			return 0;
		}
	}
	return 1;
}

Item *get(Handler *h, unsigned int key) {
	unsigned int t_idx = hash(key) % h->size;

	if (h->table[t_idx]) {
		Item *rnr = h->table[t_idx];
		while (rnr->next) {
			if (rnr->key == key) {
				return rnr;
			}
			rnr = rnr->next;
		}
	}

	return (Item *)0;
}



int main(void) {
	Handler * h = construct_(SIZE);

	if (h) {
		printf("valid Handler *");
		NEWLINE;
	}
	else {
		printf("invalid Handler *");
		NEWLINE;
	}
	
}

//int main()
//{
//    std::cout << "Hello World!\n"; 
//}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
