#include<stdio.h>
void main()
{
	int m_a[2][2],m_b[2][2],m_c[2][2];
	int i,j;
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("\n mtrix :[%d][%d]",i,j);
			scanf("%d",&m_a[i][j]);
		}
	}
	printf("second matrix");
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("[%d][%d]",i,j);
			scanf("%d",&m_b[i][j]);
		}	
	}
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			m_c[i][j]=m_a[i][j]+m_b[i][j];
		}
	}
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("\t%d",m_c[i][j]);
		}
		printf("\n");
	}
}
