import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size");
        String str = sc.nextLine();
        String up= str.replaceAll("\\s+","");
        System.out.println(up);
    }
}