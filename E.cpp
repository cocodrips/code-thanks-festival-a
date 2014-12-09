#include <iostream>
#include <map>
#include <string> 
#include <vector>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <queue>
#include <tuple>
#include <stack>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

using namespace std;

int main(int argc, const char * argv[]){
    int R,C,M,N;
    cin >> R >> C >> M >> N;
    int v[R][C];

    for (int r = 0; r < R; ++r){
        for (int c = 0; c < C; ++c){
            v[r][c] = 0;
        }    
    }

    int r1,r2,c1,c2;
    int rc[N][4];
    for (int i = 0; i < N; ++i){
        cin >> r1 >> r2 >> c1 >> c2;
        rc[i][0] = r1 - 1;
        rc[i][1] = r2 - 1;
        rc[i][2] = c1 - 1;
        rc[i][3] = c2 - 1;
    }

    // for (int i = 0; i < N; ++i){
    //     cout << rc[i][0] << rc[i][1] << rc[i][2] << rc[i][3] << endl;
    // }
    
    for (int i = 0; i < N; ++i){
        for (int r = rc[i][0]; r <= rc[i][1]; ++r){
            for (int c = rc[i][2]; c <= rc[i][3]; ++c){
                v[r][c]++;
            }
        }
    }

    for (int i = 0; i < N; ++i){
        int tmp[R][C];
        for (int r = 0; r < R; ++r){
            for (int c = 0; c < C; ++c){
                tmp[r][c] = v[r][c];
            }
        } 

        int count = 0;
        for (int r = rc[i][0]; r <= rc[i][1]; ++r){
            for (int c = rc[i][2]; c <= rc[i][3]; ++c){
                tmp[r][c]--;
            }    
        }

        for (int r = 0; r < R; ++r){
            for (int c = 0; c < C; ++c){
                // cout << tmp[r][c] << " ";
                if (tmp[r][c] % 4 == 0){
                    count ++;
                }
            }
        } 
        // cout << count << endl;
        if (count == M) {
            cout << i + 1 << endl;
        }
    }

    return 0;
}

