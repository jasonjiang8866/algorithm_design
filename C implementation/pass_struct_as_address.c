typedef struct {
    char name[30];
    int age;
    float height;
    float weight;
} Person;
int main()
{
    Person p1 = {"Sean Wai", 38, 1.76, 88.0};
    Person p2 = p1;
    Person p3= {"Sean Wai", 88, 1.76, 88.0};
    Person *p4;
    p1.age = 39;
    printf("p1 age: %d, p2 age: %d\n", p1.age, p2.age);
    p4=&p3;
    p4->age=99;
    printf("p3 age: %d, *p4 age: %d\n", p3.age, p4->age);
    return 0;
}

/*
p1 age: 39, p2 age: 38
p3 age: 99, *p4 age: 99 
*/
