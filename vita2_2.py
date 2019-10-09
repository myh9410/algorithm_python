N = int(input())
using namespace std;

int N;
// mn - 최솟값을 저장하기 위해 적당히 큰 값으로 초기화
// mx - 최댓값을 저장하기 위해 적당히 작은 값으로 초기화
int mn = 987654321, mx = 0;

void go(vector<string> &dat, int depth, int idx, int val) {
	// 리프노드에 도달: 기저사례
	if (depth >= N) {
		mn = min(mn, val);
		mx = max(mx, val);
		return;
	}

	// 왼쪽 자식노드로 굴러갔을 경우
	go(dat, depth + 1, idx * 2, val + dat[depth][idx] - 64);
	// 오른쪽 자식노드로 굴러갔을 경우
	go(dat, depth + 1, idx * 2 + 1, val + dat[depth][idx] - 64);
}
int main() {
	cin >> N;

	vector<string> dat(N);
	for (int i = 0; i < N; ++i) cin >> dat[i];

	go(dat, 0, 0, 0);

	cout << mn << '\n' << mx;

	return 0;
}