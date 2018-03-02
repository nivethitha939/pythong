#include<stdio.h>
void main()
{
    char a[50];
    int i;
    scanf("%s",&a);
    for(i=0;a[i]!='\0';i++)
    {
        if (a[i]=='z' || a[i]=='Z')
        {
            printf("%c",a[i]-23);
        }
        else
        {
        printf("%c",a[i]+3);
        }
    }
}
