#ifndef HTABLE_H_ /* Include guard */
#define HTABLE_H_

#define SMALL_SIZE 17
#define MEDIUM_SIZE 47
#define LARGE_SIZE 97

struct hitem_d;
typedef hitem_d hitem_t;

struct htable_d;
typedef htable_d htable_t;

/*
 * Hash table contruction
 *
 *  with default size (small)
 *  with custom size (?)
 */
htable_t *create_htable();

/*
 *
 */

#endif // HTABLE_H_
