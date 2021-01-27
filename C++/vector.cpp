#include <iostream>
#include <vector>

using namespace std;


int main()
{
	vector<vector<int>> A;
	vector<int> B;

	B.push_back(0);
	B.push_back(1);
	B.push_back(2);
	B.push_back(3);
	A.push_back(B);

	//注意需要清空B
	B.clear();
	B.push_back(4);
	B.push_back(5);
	B.push_back(6);
	B.push_back(7);
	A.push_back(B);

	cout << "============第一种索引方式============" << endl;
	for (int i = 0; i < 2; i++)
	{
		vector<int> & p = A[i];
		for (int j = 0; j < p.size(); j++)
		{
			cout << p[j] << " ";
		}
		cout << endl;
	}
	
	cout << "============第二种索引方式============" << endl;
	for (int i = 0; i < A.size(); i++)
	{
		for (int j = 0; j < A[0].size();j++)
			cout << A[i][j] << " ";

		cout << endl;
	}

	return  0;
}