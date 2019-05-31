#include <stdio>
#include <stdlib>

#include "htable.h"

struct hitem_d{
    int key;
    int value;
    hitem_t *next;
};

struct htable_d{
    int size;
    int count;
    hitem_t **table;
};

htable_t *create_table(){
    htable_t *htable_n = (htable_t *)malloc(sizeof(htable_t));

    if(htable_n){
        // initialize the attributes inside htable_n
        htable_n->size = SMALL_SIZE;
        htable_n->count = 0;
        htable_n->table = 
    }
}
