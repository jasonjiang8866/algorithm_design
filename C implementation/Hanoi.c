#include <stdio.h>
#include <string.h>
#define NUM_DISCS 4
#define NUM_PEG 3
typedef struct {
int peg[3][NUM_DISCS+1];
char name[30];
}  Towers;

void make_moves(Towers *t, int n, int src, int des, int aux);
void init_towers(Towers *t, const char name[]);
void print_towers(Towers t);
void move_disc(Towers *t, int src, int des);



Towers tower;

int main(void) {
Towers t;
init_towers(&t, "Hanoi");
printf("Towers of %s\n", t.name);
print_towers(t);
make_moves(&t, NUM_DISCS , 0, 2, 1);

return 0;
}

void make_moves(Towers *t, int n, int src, int des, int aux) {
if (n<=0) return;
make_moves(t, n-1, src, aux, des);
move_disc(t, src, des);
make_moves(t, n-1, aux, des, src);
return;
}


void init_towers(Towers *t, const char name[]) {
	for (int i=0;i<NUM_DISCS;i++){
		t->peg[0][i]=i;
	}
	strcpy(t->name,name);
	/* int name_size=strlen(name);
	for (int i=0;i<name_size;i++){
		t->name[i]=name[i];
	} */
	t->peg[1][0]=-1;
	t->peg[2][0]=-1;
	t->peg[0][NUM_DISCS]=-1;
	/*
	printf("%s\n",t->name);
	for (int i=0;i<NUM_DISCS+1;i++){
		printf("DISC=%d\n",t->peg[0][i]);
	}
	*/
	return;
}

void print_towers(Towers t) {
	for (int i=0;i<NUM_PEG;i++){
		printf("[ ");
		for (int j=0;t.peg[i][j]!=-1;j++){
			printf("%d ",t.peg[i][j]);
		}
		printf("]");
		if (i!=NUM_PEG-1){
			printf(", ");
		} else {
		    printf("\n");
		}
	}
    return;
}

void move_disc(Towers *t, int src, int des) {
    int top;
    /* 
	for implementation
	for (int i=0;i<=NUM_DISCS;i++){
        if (t->peg[src][i]==-1) {
            top=t->peg[src][i-1];
            t->peg[src][i-1]=-1;
            break;
        }
    }
    for (int i=0;i<=NUM_DISCS;i++){
        if (t->peg[des][i]==-1) {
            t->peg[des][i]=top;
            t->peg[des][i+1]=-1;
            break;
        }
    } */
	int i=0;
	while (t->peg[src][i]!=-1){
		i++;
	}
	top=t->peg[src][i-1];
	t->peg[src][i-1]=-1;
	i=0;
	while (t->peg[des][i]!=-1){
		i++;
	}
	t->peg[des][i]=top;
	t->peg[des][i+1]=-1;
	
    print_towers(*t);
    return;
}
