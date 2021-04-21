#include<iostream>
#include<vector>
#include<bits/stdc++.h>
#include<list>
#include <utility>
#include <chrono>


using namespace std::chrono;
using namespace std;


void dataset(int cantidad, int min, int max, string path){
    fstream file;
    file.open(path, ios::app);
    for(int i = 1; i <= cantidad; ++i){
        file << rand()%max + min << " " << rand()%max + min << endl;
    }
    file.close();
}

void create_datasets(){
    dataset(50000, 0, 901, "dataset_a.txt");
    dataset(25000, 0, 901, "dataset_b.txt");
    dataset(25000, 900, 1501, "dataset_b.txt");
    dataset(50000, 0, 1501, "dataset_c.txt");
    return;
}
//vector<int> cols()
list<pair<int,int>> todo_list;


void parsing3(string dataset){
    fstream file;
    file.open(dataset);
    int x, y;
    while(!file.eof()){
        file >> x >> y;
        todo_list.push_back({x,y});
    }
}

float calc_dist(pair<int,int> cord1, pair<int, int>cord2){
    float x = cord1.first - cord2.first;
    float y = cord1.second - cord2.second;
    float ans = sqrt(pow(x,2) + pow(y,2));
    return ans;
}
typedef pair<float, pair<int,int>> pi;

void k_near_list(int x, int y, int k){
    priority_queue <pi, vector<pi>, greater<pi> > pq;
    float dist;
    for (auto & coord : todo_list){
        dist = calc_dist(coord, make_pair(x,y));
        pq.push(make_pair(dist, coord));
    }
    for (int i = 0; i < k; i++)
    {
        pair<int,int> coord = pq.top().second;
        pq.pop();
        //cout<<coord.first<<"--"<<coord.second<<endl;
    }
    
}

void k_near(int x, int y, int k){
    //int total_cord = todo[x][y];
    bool max_x, min_x, max_y, min_y;
    for(int i = 1; i <= 1500; ++i){
        max_x = x+i <= 1500;
        min_x = x-i >= 0;
        max_y = y+i <= 1500;
        min_y = y-i >= 0;
        
        // if(max_x && todo[x+i][y] != 0)
        // if(min_x && todo[x-i][y] != 0)
        // if(max_y && todo[x][y+i] != 0)
        // if(min_y && todo[x][y-i] != 0)
        // if(max_x && max_y && todo[x+i][y+i] != 0)
        // if(max_x && min_y && todo[x+i][y-i] != 0)
        // if(min_x && min_y && todo[x-i][y-i])
        // if(min_x && max_y && todo[x-i][y+i])
    }
    return;
}

int main(int argc, char const *argv[]){
    srand(time(NULL));
    parsing3("dataset_a.txt");
    for (int i = 0; i < 10; i++)
    {
        int x=rand()%900 + 0;
    int y=rand()%900 + 0;
    int k=rand()%900 + 0;
    auto start = high_resolution_clock::now();
    k_near_list(x, y, k);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
  
    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;
    
    }
    return 0;
}

// https://www.overleaf.com/1431967612zbkczmvmtkcv
// scikit-learn

/* tiempos microsegundos
6913
6916
7241
6896
7110
7107
6913
6992
6916
7040
6955
*/