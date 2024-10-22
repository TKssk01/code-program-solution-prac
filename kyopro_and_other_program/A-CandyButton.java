import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 入力の読み込み
        int N = sc.nextInt(); // ボタンの押下回数
        int C = sc.nextInt(); // 飴をもらうための最小経過時間
        int[] T = new int[N]; // ボタン押下時刻の配列

        for (int i = 0; i < N; i++) {
            T[i] = sc.nextInt();
        }

        sc.close(); // 入力ストリームを閉じる

        // 飴の個数をカウントする変数
        int count = 0;
        // 最後に飴をもらった時刻を記録する変数
        int lastTime = -C; // 最初の押下が必ず成功するように設定

        // ボタン押下のシミュレーション
        for (int t : T) {
            if (t - lastTime >= C) {
                count++;
                lastTime = t;
            }
        }

        // 結果の出力
        System.out.println(count);
    }
}
