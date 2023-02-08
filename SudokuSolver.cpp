#include <iostream>

using namespace std;

int solve(int field[9][9]) {
    
}

int main()
{
    // ~intro/instructions

    cout << "input here like this : [0,1,2,3,4,5,6,7,8] !!! NO SPACES !!! ENTER than again... \n";
    cout << "if cell is empty than 99...\n";

    // we create an 2D-Array of 'Cells'

    int field[9][9] = {};

    for (int row = 0; row < 9; row++) {
        string val;
        cout << row + 1;
        cin >> val;                                                                         // we ask for a row of values.
        int single[9] = {};
        int column = 0;
        for (int x = 0; x < val.length(); x++) {                                            // we loop over all chars in val
            if (val[x] == ';') {                                                            // if there is a ';' we know that we start the next column
                column++;
                field[row][column] = 0;                                                     // so we make the next array-spot 0
            }
            else {
                if (val[x + 1] != ';') {                                                    // if the next char isnt a ';' we know that the current num is a multiple of 10
                    field[row][column] = 10 * val[x];
                }
                else {
                    field[row][column] += val[x];                                           // else we know that it is a single number...
                }
            }
        }
    }
}
