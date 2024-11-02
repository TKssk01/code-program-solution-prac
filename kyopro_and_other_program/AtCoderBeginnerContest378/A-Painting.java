/*
 * 考え方の詳細
入力の読み取り

問題では4つのボールが与えられ、それぞれの色が1から4の整数で表されています。
プログラムはScannerクラスを使用して、これらの4つの整数を順番に読み取ります。
色の出現回数のカウント

1から4までの色ごとに出現回数をカウントするために、配列countを用意します。
読み取った各色について、対応するインデックスの値をインクリメントしていきます。
例えば、色が2であればcount[2]を増やします。
ペアの数の計算

各色のボール数を2で割った整数部分が、その色で作成できるペアの数になります。
例えば、色1が3個あれば1ペア（余り1個）、色2が4個あれば2ペアとなります。
全ての色についてペアの数を計算し、合計します。
最大操作回数の決定

4つのボールから最大で2回のペア操作しか行えません（1回の操作で2個のボールを捨てるため）。
計算したペアの合計が2以上であれば、操作回数を2に制限します。そうでなければ、ペアの合計回数をそのまま使用します。
結果の出力

最終的に決定した最大操作回数を標準出力に表示します。
具体例での流れ
 */


import java.util.*; // 必要なユーティリティクラス（例: Scanner）をインポート
import java.lang.*; // 基本的な言語機能をインポート（実際には自動的にインポートされるが明示的に）
import java.io.*; // 入出力関連のクラスをインポート

// メインメソッドは "Main" という名前のクラス内に存在しなければならない
class Main {
    public static void main(String[] args) {

        // 標準入力を読み取るためのScannerオブジェクトを作成
        Scanner sc = new Scanner(System.in);

        // 4つのボールの色を格納する配列を作成
        int[] colors = new int[4];
        // 4回ループして、各ボールの色を入力から読み取る
        for(int i = 0; i < 4; i++){
            colors[i] = sc.nextInt(); // 入力から整数を読み取り、colors配列に格納
        }

        // 色の出現回数をカウントするための配列を作成（色は1から4なので、インデックス1〜4を使用）
        int[] count = new int[5]; // インデックス0は使用しないため、サイズを5に設定
        // colors配列の各色についてループ
        for(int color : colors){
            // 色が1から4の範囲内であることを確認
            if(color >= 1 && color <= 4){
                count[color]++; // 該当する色のカウントをインクリメント
            }
        }

        // 全てのペアの合計数を初期化
        int totalPairs = 0;
        // 色1から色4までループして、各色のペア数を計算
        for(int i = 1; i <= 4; i++){
            totalPairs += count[i] / 2; // 各色のボール数を2で割った整数部分（ペア数）を合計に加算
        }

        // 最大操作回数を決定（4個のボールから最大2回のペア操作が可能）
        int maxOperations = Math.min(totalPairs, 2); // totalPairsと2のうち、小さい方を選択

        // 最大操作回数を標準出力に表示
        System.out.println(maxOperations); // 計算結果を出力

        // Scannerオブジェクトを閉じてリソースを解放
        sc.close(); // 入力ストリームを閉じる
    }
}
