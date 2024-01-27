#include<bits/stdc++.h>
using namespace std;
 
int findLength(char *str)
{
    int n = strlen(str);
    int maxlen =0; // Initialize result
 
    // Choose starting point of every substring
    for (int i=0; i<n; i++)
    {
        // Choose ending point of even length substring
        for (int j =i+1; j<n; j += 2)
        {
            int length = j-i+1;//Find length of current substr
 
            // Calculate left & right sums for current substr
            int leftsum = 0, rightsum =0;
            for (int k =0; k<length/2; k++)
            {
                leftsum += (str[i+k]-'0');
                rightsum += (str[i+k+length/2]-'0');
            }
 
            // Update result if needed
            if (leftsum == rightsum && maxlen < length)
                    maxlen = length;
        }
    }
    return maxlen;
}
 
// Driver program to test above function
int main(void)
{
    char str[] = "1538023";
    cout << "Length of the substring is "
         << findLength(str);
    return 0;
}