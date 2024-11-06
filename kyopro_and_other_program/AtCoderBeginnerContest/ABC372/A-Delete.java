import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 入力の読み込み
        String inputString = sc.nextLine();
        // '.' を取り除く
        String result = inputString.replace(".","");
        // 結果の出力
        System.out.println(result);
    }
}