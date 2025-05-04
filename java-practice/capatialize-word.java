import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size");
        String str = sc.nextLine();
        String[] words =str.split(" ");
        String result= " ";
        for (String word: words){
            if (word.length()>0){
                String up =word.substring(0,1).toUpperCase() + word.substring(1);
                result += up + " ";
            }
        }
        System.out.println(result.trim());
    }
}