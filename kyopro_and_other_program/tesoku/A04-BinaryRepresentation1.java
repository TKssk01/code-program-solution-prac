import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 入力の読み込み
        int N = sc.nextInt();
        
        String N2 = "";
        
        while (N > 0){
          int K = N % 2; //2で割ったあまり
          N2 = K + N2; //N2の先頭に余りを追加
          N /= 2; //Nを2で割り更新
        }
        
        // 10桁に満たない場合は左を0で埋める
        N2 = String.format("%10s",N2).replace(' ','0');

        System.out.println(N2);

    }
}