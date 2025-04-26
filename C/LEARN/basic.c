#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>


int Rectangle_Perimeter(int side1, int side2){
    int Perimeter= 2*(side1 + side2);
    return Perimeter;

}

int Find_Cube(int number){
    int cube=number*number*number;
    return cube;

}

float average_3_numbers(int number1,int number2,int number3){
    float average=(float)(number1+number2+number3)/3;
    return average;

}

void if_digit(char input){
    if(input>='0' && input<='9'){
        printf("It is a digit\n");
    }
    else {
        printf("It is not a digit\n");
    }

}

int Compare_Two_Numbers(int number1, int number2){
    if(number1>number2){
        return number2;
    }
    else return number1;

}

int Find_Number_of_Digits(int number){
    if (number == 0) return 1;
    int digits=0;
    while(number!=0){
        digits++;
        number/=10;
    }
    return digits;

}

void Check_Armstrong_Number(int number){
    int ORG=number;
    int digits = Find_Number_of_Digits(number);
    int remainder,sum=0;

    while(number>0){
        remainder=number%10;
        int power = 1;
        for (int i = 0; i < digits; i++) {
            power *= remainder;
        }

        sum += power;
        number/=10;
        
    }
    
    if(ORG==sum){
        printf(" yes\n");
    }
    else printf("no\n");

}

void check_natural_number(int number){
    if(number>0){
        printf(" natural number\n");
    }
    else printf("not\n");

}

void pattern(){
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            printf("*\t");
        }
        printf("\n");
    }
}

int Check_prime_number(int number){
    int prime=1;
    for(int i=2;i<number;i++){
        if(number%i==0){
            prime=0;
            break;
        }
    }
    return prime;

}

void prime_in_range(int from, int to){
    int prime,count=0;
    for(int j=from;j<=to;j++){
        prime=Check_prime_number(j);
        if(prime==1){
            printf("%d\n",j);
            count++;
        }
    }
    if(count==0) printf("no prime found\n");

}

int sum_of_digits(int number){
    int remainder,sum=0;
    while(number!=0){
    remainder=number%10;
    sum+=remainder;
    number/=10;
    }
    return sum;
}

int square_Root(int number){
    int square,j;
    int flag=1;

        for(j=1;j<number/2;j++){
            square=j*j;

            if(square==number){
                printf("square root is %d",j);
                flag=0;
                break;
            }
        }

    if(flag==1){
        printf("Not a perfect square\n");

    }
    
}

int power(int base,int exponent){
    int result=1;
    for(int i=0;i<exponent;i++){
        result*=base;
    }
    return result;

}

int maximum_of_two(int *number1,int *number2){
    if(*number1 > *number2){
        return *number1;
    }
    else return *number2;
}

void print_all_english_alphabets(){
    for(int i='A'; i<='Z';i++){
        int *ptr=&i;
        printf("%c",*ptr);
    }
}

char Reverse_Array(char array[],int size){
    for(int i=0; i<size/2;i++){
        char temp= array[i];
        array[i]= array[size-i-1];
        array[size-i-1]=temp;

    }

}

int Number_occured(int array[], int size, int number){
    int count=0;
    for(int i=0;i<size;i++){
        if(number==array[i]){
            count++;
        }
    }
    return count;
}

int Largest_number(int array[],int size){
    int largest=array[0];
    for(int i=0;i<size-1;i++){
        if(largest<array[i+1]){
            largest=array[i+1];
        }
        
    }
    return largest;
}

int insert_at_end(char array[],int size,char number){
    array[size]=number;
    size++;
    return size;
   
}

void Vowel_lower_two_upper(char array[]){
    for(int i=0;array[i]!='\0';i++){
        if(array[i]=='a' || array[i]=='e' ||array[i]=='i' ||array[i]=='o' ||array[i]=='u'){
            array[i]=array[i]-32;
        }
    }
}

char Highest_frequency_character(char str[]){
    char character,frequent=00;
    int frequency1=0,frequency2=0;

    for(int i=0; str[i]!='\0';i++){
        character=str[i];
        for(int j=i+1; str[j]!='\0';j++){
            if(str[j]==character){
                frequency2++;

            }
        }
        if(frequency2>frequency1){
            frequency1=frequency2;
            frequent=character;
        }
        

    }
    return frequent;

}

void Remove_blank_space(char str[]) {
    int i, j = 0;
    
    for(i = 0; str[i] != '\0'; i++) {
        if(str[i] != ' ') {
            str[j] = str[i];
            j++;
        }
    }
    str[j] = '\0'; 
}

void Case_invert(char str[]){
    for(int i=0;str[i]!='\0';i++){
        if(str[i]>=97 && str[i]<=122){
            str[i]=str[i]-32;
        }
        else if(str[i]>=65 && str[i]<=90){
            str[i]=str[i]+32;
        }
    }
}

//Structure
typedef struct information{
    char name[10];
    int age;
    float rating;
} info;

void Store_information(){
    info person[3];

    for(int i=0;i<3;i++){
        printf("enter info of person%d is below: \n",i+1);
        scanf("%s",&person[i].name);
        scanf("%d",&person[i].age);
        scanf("%f",&person[i].rating);
    }

    for(int i=0;i<3;i++){
        printf("info of person%d is below: \n",i+1);
        printf("name: %s\t",person[i].name);
        printf("age: %d\t",person[i].age);
        printf("rating: %f\t",person[i].rating);
    }

}

void Read_file(){
    FILE *fptr;
    char data;

    fptr = fopen("filename.txt", "r");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return;
    }

    data = fgetc(fptr); 
    while (data != EOF) {
        printf("%c", data);   
        data = fgetc(fptr);   
    }

    fclose(fptr);
}

void Replace_count_file(){
    FILE *fptr;
    fptr= fopen("filename.txt","r");

    char data=fgetc(fptr);
    int count=0;

    while(data!=EOF){
        if(data=='a' || data=='e' || data=='i' || data=='o' || data=='u'){
            count++;
        }
        data=fgetc(fptr);
    }

    fclose(fptr);

    fptr=fopen("filename.txt","w");
    fprintf(fptr,"%d",count);
    fclose(fptr);


}

void Memory_allocation(){
    int *ptr;
    ptr= (int*)calloc(500,sizeof(int));
    for(int i=0;i<500;i++){
        ptr[i]=i+1;
    }

    for(int i=0;i<500;i++){
        printf("%d\t",ptr[i]);
    }

    free(ptr);

}


int main(){
    int option;
    do{
        int Task_No;
    
        printf("\n1. Find Perimeter of a Rectangle\n");
        printf("2. Cube of a number\n");
        printf("3. Find average of 3 numbers\n");
        printf("4. Check if digit\n");
        printf("5. Find smallest among two numbers\n");
        printf("6. Check Armstrong number\n");
        printf("7. Check natural number\n");
        printf("8. Print a pattern\n");
        printf("9. check prime number\n");
        printf("10. prime numbers in a range\n");
        printf("11. Sum of digits\n");
        printf("12. Find square root\n");
        printf("13. power function\n");
        printf("14. max of 2 numbers\n");
        printf("15. print all english alphabets\n");
        printf("16. Reverse an array\n");
        printf("17. number occured how many times in array\n");
        printf("18. Largest number in array\n");
        printf("19. Insert element at end of an array\n");
        printf("20. make vowels in string from lower to upper case\n");
        printf("21. Highest_frequency_character in string\n");
        printf("22. remove spaces from string\n");
        printf("23. Invert cases of letters in string\n");
        printf("24. Store information of 3 people\n");
        printf("25. play with file and memory\n");

        printf("\nChoose task to perform:\t");
        scanf("%d", &Task_No);
    
        switch(Task_No){

            case 1: {
                int side1, side2;
                printf("Enter sides of Rectangle\n");
                printf("Enter side 1:\t");
                scanf("%d", &side1);
                printf("Enter side 2:\t");
                scanf("%d", &side2);
                printf("Perimeter of Rectangle is: %d",Rectangle_Perimeter(side1, side2));
                break;
            }

            case 2: {
                int number;
                printf("Enter number\n");
                scanf("%d", &number);
                printf("cube of %d is: %d",number,Find_Cube(number));
                break;
            }

            case 3: {
                int number1,number2,number3;
                printf("Enter number 1:\t");
                scanf("%d", &number1);
                printf("Enter number 2:\t");
                scanf("%d", &number2);
                printf("Enter number 3:\t");
                scanf("%d", &number3);
                printf("Average is: %f",average_3_numbers(number1,number2,number3));
                break;
            }

            case 4: {
                char input;
                printf("Enter input to check:\t");
                scanf(" %c", &input); 
                if_digit(input);
                break;
            }

            case 5: {
                int number1,number2;
                printf("Enter first number:\t");
                scanf("%d", &number1);
                printf("Enter second number:\t");
                scanf("%d", &number2); 
                printf("smallest number is %d",Compare_Two_Numbers(number1,number2));
                break;
            }

            case 6: {
                int number;
                printf("Enter number:\t");
                scanf("%d", &number);
                Check_Armstrong_Number(number);
                break;
            }

            case 7: {
                int number;
                printf("Enter number:\t");
                scanf("%d", &number);
                check_natural_number(number);
                break;
            }

            case 8:  
                pattern();
                break;

            case 9: {
                int number;
                printf("Enter number:\t");
                scanf("%d", &number);
                printf("%d",Check_prime_number(number));
                break;
            }    

            case 10: {
                int from,to;
                printf("Enter from number:\t");
                scanf("%d", &from);
                printf("Enter to number:\t");
                scanf("%d", &to); 
                prime_in_range(from,to);
                break;
            }

            case 11: {
                int number;
                printf("Enter number:\t");
                scanf("%d", &number);
                printf("sum of digits = %d",sum_of_digits(number));
                break;
            }    

            case 12: {
                int number;
                printf("Enter number:\t");
                scanf("%d", &number);
                square_Root(number);
                break;
            }    

            case 13: {
                int base,exponent;
                printf("Enter base:\t");
                scanf("%d", &base);
                printf("Enter exponent:\t");
                scanf("%d", &exponent);
                printf("%d power %d is %d",base,exponent,power(base,exponent));
                break;
            }  
            
            case 14: {
                int number1,number2;
                printf("Enter first number:\t");
                scanf("%d", &number1);
                printf("Enter second number:\t");
                scanf("%d", &number2); 
                printf("Max is %d",maximum_of_two(&number1,&number2));
                break;
            }

            case 15: {
                printf("alphabets: \n");
                print_all_english_alphabets();
                break;
            }

            case 16: {
                int size;
                printf("enter size of array\n");
                scanf("%d",&size);
                char array[size];
                printf("Entere array:");
                for(int i=0;i<size;i++){
                    scanf(" %c",&array[i]);

                }
                Reverse_Array(array,size);
                printf("Reversed array is:");
                for(int i=0;i<size;i++){
                    printf("%c\t",array[i]);

                }
                break;

            }

            case 17: {
                int size,number;
                printf("enter size of array\n");
                scanf("%d",&size);
                int array[size];
                printf("Entere array:");
                for(int i=0;i<size;i++){
                    scanf("%d",&array[i]);

                }
                printf("enter number\n");
                scanf("%d",&number);
                printf("%d occured %d times ",number,Number_occured(array,size,number));            
                break;
            }

            case 18: {
                int size;
                printf("enter size of array\n");
                scanf("%d",&size);
                int array[size];
                printf("Entere array:");
                for(int i=0;i<size;i++){
                    scanf("%d",&array[i]);

                }
                printf("the largest number: %d", Largest_number(array,size));          
                break;
            }

            case 19: {
                int size,choice;
                char number;
                printf("enter size of array\n");
                scanf("%d",&size);
                char array[10];
                printf("Entere array:");
                for(int i=0;i<size;i++){
                    scanf(" %c",&array[i]);

                }
                printf("New array:");
                for(int i=0;i<size;i++){
                    printf("%c",array[i]);

                }
                do{
                printf("enter number\n");
                scanf(" %c",&number);
                size=insert_at_end(array,size,number);
                printf("New array:");
                for(int i=0;i<size;i++){
                    printf("%c",array[i]);

                }
                printf("enter more ? choose 1 otherwise 0\n");
                scanf("%d",&choice);
            }while(choice==1);
                break;
            }

            case 20: {
                char array[100];
                getchar();
                fgets(array,100,stdin);
                Vowel_lower_two_upper(array);
                puts(array);
                break;
            }

            case 21: {
                char str[100];
                char frequent;
                getchar();
                fgets(str,100,stdin);
                frequent=Highest_frequency_character(str);
                printf("highest frequency is of: %c",frequent);
                break;
            }

            case 22: {
                char str[100];
                getchar();
                fgets(str,100,stdin);
                Remove_blank_space(str);
                puts(str);
                break;
            }

            case 23: {
                char str[100];
                getchar();
                fgets(str,100,stdin);
                Case_invert(str);
                puts(str);
                break;
            }

            case 24: {
                Store_information();
                break;
            }

            case 25: {
                Read_file();
                Replace_count_file();
                Memory_allocation();
                break;
            }


            default: printf("Oops! invalid option\n"); 

        }

        printf("\nChoose option :\t 1.Quit\t 2.Retry\n");
        scanf("%d",&option);

    }while(option==2);
    printf("See you next time!\n");
    return 0;
}