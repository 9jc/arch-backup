import java.io.*;
import java.util.*;
class vector_exer
{
  public static void main(String args[])throws IOException
  {
    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    Vector vect=new Vector();
    int ch=0,pos,i;
    Ex.No: 3
    Date :
    Usage of Vector Class
    System.out.println("\n enter elements to add");
    vect.addElement(br.readLine());
    System.out.println("\n enter elements to add");
    vect.addElement(br.readLine());
    System.out.println("\n size of vector array:"+vect.size()+"\n");
    System.out.println("\n enter elements to insert");
    vect.insertElementAt(br.readLine(),1);
    System.out.println("\n element is inserted in index 1");
    System.out.println("\n element in vector array");
    Iterator it=vect.iterator();
    while(it.hasNext())
    System.out.println(" "+it.next());
    vect.removeElementAt(0);
    System.out.println("\n element at 0 index is deleted");
  } 
}