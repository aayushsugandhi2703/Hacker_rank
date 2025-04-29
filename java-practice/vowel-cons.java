import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size");
        String str = sc.nextLine();
        int v=0; int c=0;
        str = str.toLowerCase();
        for (int i=0; i<str.length(); i++){
            char ch = str.charAt(i);
            if (ch >='a' && ch<='z'){
                if (ch=='a' || ch=='e' || ch=='i'|| ch=='o' || ch=='u'){
                    v++;
                }
                else{
                    c++;
                }
            }
        }
        System.out.println(v);
        System.out.println(c);
    }
}