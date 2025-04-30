import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size");
        String str = sc.nextLine();
        int c=0;
        str= str.toLowerCase();
        for (int i=0; i<str.length();i++){
            char ch= str.charAt(i);
            if (ch>='a'&& ch<='z'){
                c++;
            }
        }
        System.out.println(c);
    }
}