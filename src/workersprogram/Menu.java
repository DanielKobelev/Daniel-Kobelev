package workersprogram;


import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;
import exception.EmployeeDoesntExist;
import exception.EmptyInput;
import exception.Existing_Employee;
import exception.MinBasePay;
import exception.MonthlyBonous;
import exception.SpecialBnonus;
import exception.ValidGender;
import staff.HumanResource;
import workers.Administrative;
import workers.Algorithmists;
import workers.Employee;
import workers.Gender;
import workers.Software_Developer;

public class Menu implements Serializable {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	public static boolean flag = true;
	public static ArrayList<Employee> Employeelist = new ArrayList<Employee>();
	public static HumanResource HR = new HumanResource(Employeelist);
	public static ArrayList<Employee>newEmployee = null;
	

	



	public static void main(String[] args) {
		Scanner scann = new Scanner(System.in);
		while (flag) {
		
			
				
					try {
						menu(scann);
						read();
					} catch (Existing_Employee e) {
						System.err.println("Error:\nExisting Employee");
					} catch (EmployeeDoesntExist e) {
						System.err.println("Error:\nEmployee id Doesnt Exist  returning to main menu\n");
					} catch (ValidGender e) {
						System.err.println("Error:\nOnly valid genders are male and female returning to main menu\n");
					} catch (MinBasePay e) {
						System.err.println("Error:\nThe minimum base pay must be over 0 returning to main menu\n");
					} catch(MonthlyBonous e) {
						System.err.println("Error:\nThe MonthlyBonous cannot be negtive");
					}catch(SpecialBnonus e) {
						System.err.println("Error:\n The Special Bnonus cannot be netgtive");
					}catch(IllegalArgumentException e) {
						System.err.println("Error:\nonly valid genders are male and female");
					} catch (FileNotFoundException e) {
						e.printStackTrace();
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (ClassNotFoundException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
			} catch (EmptyInput e) {
						System.out.println("Error:\nEmpty input" );
					}
					
		}
		
	}
					    
				
		
		
		
		
		
	
	
	public static void menu(Scanner scann) throws Existing_Employee, EmployeeDoesntExist,ValidGender,MinBasePay, MonthlyBonous, SpecialBnonus, FileNotFoundException, IOException, ClassNotFoundException, EmptyInput  {
		System.out.println("Please choose:\n1.Add Employee\n2.View personal record\n3.Delete Employee record\n4.Employee List\n5.Exit");
		int userChoice = scann.nextInt();
		switch(userChoice) {
			case 1:
				EmployeeType(scann);
				{
					break;}
			case 2:
				System.out.println("What is the Employee ID");
				int id = scann.nextInt();
				System.out.println("\n"+ HR.FindEmployeeById(id)+"\n");
				break;
			case 3:
				System.out.println("What is the Employee ID");
				int idtemp = scann.nextInt();
				HR.DeletEmployeeByiD(idtemp);
				System.out.println("Employee deleted\n");
				menu(scann);
				break;
			case 4:
				System.out.println(HR);
				break;
			case 5:
				scann.close();
				System.out.println("-----program completed successfully-----");
				write(Employeelist);
				 flag = false;
				return;
			default:
				System.err.println("\nOnly 1-5 options are available\n");
				
				menu(scann);
			}
		}
				

	
	public static void EmployeeType(Scanner scann) throws Existing_Employee, EmployeeDoesntExist, ValidGender, MinBasePay, MonthlyBonous, SpecialBnonus, FileNotFoundException, IOException, ClassNotFoundException,EOFException, EmptyInput{
		System.out.println("Please choose Employee type\n1.Software Developer\n2.Algorithmists\n3.Administrative");
		int userChoice = scann.nextInt();
		switch(userChoice) 
		{
		case 1:
			DefEmployee(scann,"Software Developer");
			break;
		case 2:
			DefEmployee(scann,"Algorithmists");
			break;
		case 3:
			DefEmployee(scann,"Administrative");
			break;
		default:
			System.err.println("\nOnly 1-3 options are available\n");
			EmployeeType(scann);
		}	
	}
	
	public static void DefEmployee(Scanner scann,String type) throws EmployeeDoesntExist, MinBasePay, MonthlyBonous, SpecialBnonus, ValidGender, FileNotFoundException, IOException,EOFException, ClassNotFoundException, Existing_Employee, EmptyInput{
		System.out.println("what is the Employee ID");
		int id = scann.nextInt();
		scann.nextLine();
		for(Employee x : Employeelist)
		{
			if(x.getID() == id) 
				throw new  Existing_Employee();
		}
		String Fname;
		do {
		System.out.println("what is the Employee First name");
		Fname = scann.nextLine();
		try {
		if(Fname.isEmpty())
			throw new EmptyInput();
		}catch(EmptyInput e) {
			System.err.println("empty input please try again");
			System.out.println("what is the Employee First name");
			Fname = scann.nextLine();
		}
		}while(Fname.isEmpty());
		System.out.println("what is the Employee Last name");
		String Lname = scann.next();
		System.out.println("what is the Employee Phone Number");
		String PhoneNum = scann.next();
		System.out.println("what is the Employee Email");
		String email = scann.next();
		System.out.println("what is the Employee Gender(male/female)");
		scann.nextLine();
		String userinput = scann.nextLine();
		Gender gender = Gender.valueOf(userinput.toLowerCase());
		int basepay;
		do {
		System.out.println("what is the Employee Basepay");
		basepay = scann.nextInt();
		try {
			if(basepay < 1)
			throw new MinBasePay();
		}catch (MinBasePay e) {
			System.err.println("Error:\nThe minimum base pay must be over 0");
		}
		}while(basepay < 1);
		
		
		switch(type) {
		case "Software Developer":
			int mb;
			do {
			System.out.println("What is the monthly bonous?");
			mb = scann.nextInt();
			try {
			if(mb < 1) 
				throw new MonthlyBonous();
			}catch (MonthlyBonous e) {
				System.err.println("Error:\nThe monthly bonus cannot be negative");
			}
			}while(mb < 0);
			Employee x = new Software_Developer(id,Fname,Lname,PhoneNum,email,gender,basepay,mb);
			HR.AddEmployee(x);
				System.out.println("\nEmployee Added\n");
			break;
		case "Algorithmists":
			int monthlyBonus;
			do {
			System.out.println("What is the monthly bonous?");
			monthlyBonus = scann.nextInt();
			try {
			if(monthlyBonus < 0) 
				throw new MonthlyBonous();
			}catch (MonthlyBonous e) {
				System.err.println("Error:\nThe monthly bonus cannot be negative");
			}
			}while(monthlyBonus < 0);
			int additionalBonus;
			do {
			System.out.println("What is the additional bonus?");
			additionalBonus = scann.nextInt();
			try {
			if(additionalBonus < 0) 
				throw new SpecialBnonus();
			}catch (SpecialBnonus e) {
				System.err.println("Error:\n The additional bonus cannot be negative");
			}
			}while(additionalBonus < 0);
			Employee y = new Algorithmists(id,Fname,Lname,PhoneNum,email,gender,basepay,monthlyBonus,additionalBonus);
			
			HR.AddEmployee(y);
			System.out.println("\nEmployee Added\n");
			break;
		case "Administrative":
			System.out.println("what is his role");
			String role = scann.next();
			Employee z = new Administrative(id,Fname,Lname,PhoneNum,email,gender,basepay,role);
			HR.AddEmployee(z);
			System.out.println("\nEmployee Added\n");
			break;
			
		}
	}
public static void write(ArrayList<Employee> x) throws FileNotFoundException, IOException {
	ObjectOutputStream out = new ObjectOutputStream( new
			FileOutputStream("workers.dat"));
			out.writeObject(x);
			out.close();}

	
@SuppressWarnings("unchecked")
public static void read() throws FileNotFoundException, IOException, ClassNotFoundException {
	ObjectInputStream in = new ObjectInputStream( new
			FileInputStream("workers.dat"));
	newEmployee = (ArrayList<Employee>) in.readObject(); 
	
	in.close();
}}

	
		
	


