package workers;

import java.io.Serializable;

import exception.EmptyInput;
import exception.MinBasePay;
import exception.ValidGender;

public abstract class Employee implements Comparable<Employee>,Serializable {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	protected int ID;
	protected String FirstName;
	protected String LastName;
	protected String PhoneNum;
	protected String Email;
	protected Gender gender;
	protected int BasePay;
	
	public Employee(int ID,String FirstName,String LastName,String PhoneNum,String Email,Gender gender,int Basepay) throws ValidGender, MinBasePay, EmptyInput {
		setID(ID);
		setFirstName(FirstName);
		setLastName(LastName);
		setPhoneNum(PhoneNum);
		setEmail(Email);
		setBasePay(Basepay);
		setGender(gender);
	}
	public Employee(int ID,String FirstName,String LastName,String Email,Gender gender,int basepay) throws ValidGender, EmptyInput, MinBasePay {
		setID(ID);
		setFirstName(FirstName);
		setLastName(LastName);
		this.PhoneNum = null;
		setEmail(Email);
		setBasePay(basepay);
		setGender(gender);
	}
	public int getID() {
		return this.ID;
	}
	public int compareTo(Employee other) {
		if(this.LastName.equals(other.LastName))
			return this.FirstName.compareTo(other.FirstName);
		else
			return this.LastName.compareTo(other.LastName);
	}

	public void setID(int ID) {
		this.ID = ID;
	}

	public String getFirstName() {
		return FirstName;
	}

	public void setFirstName(String FirstName) throws EmptyInput {
		if(FirstName == "")
			throw new EmptyInput();
		else
		this.FirstName = FirstName;
	}

	public String getLastName() {
		return LastName;
	}

	public void setLastName(String lastName) throws EmptyInput {
		if(lastName == " ")
			throw new EmptyInput();
		else
		LastName = lastName;
	}

	public String getPhoneNum() {
		return PhoneNum;
	}

	public void setPhoneNum(String phoneNum) throws EmptyInput {
		if(phoneNum == " ")
			throw new EmptyInput();
		else
		PhoneNum = phoneNum;
	}

	public String getEmail() {
		return Email;
	}

	public void setEmail(String email) throws EmptyInput {
		if(email == "")
			throw new EmptyInput();
		else
		Email = email;
	}

	public Gender getGender() {
		return gender;
	}

	public void setGender( Gender gender) throws ValidGender {
		if(gender.toString().toLowerCase() == "male" || gender.toString().toLowerCase() == "female")
			this.gender = gender;
		else
			throw new ValidGender("the only valid genders are male or female");
		
		
	
	}
	

	public int getBasePay() {
		return BasePay;
	}

	public void setBasePay(int BasePay) throws MinBasePay {
		if(BasePay > 0)
			this.BasePay = BasePay;
		else
			throw new MinBasePay("the min bsae pay cannot be negtive");
	}
	public int Salary() {
		return this.getBasePay();
	}
	public String check() {
		if(this instanceof Algorithmists)
			return "Algorithmists";
		else if(this instanceof Software_Developer)
			return "Software Developer";
		else if (this instanceof Administrative)
			return "Administrative";
		return "not defined";
			
	}
		

	public boolean equals(Object other) {
		return other instanceof Employee&&(this.ID ==((Employee)other).getID());
		
		
		
	}
	public String toString() {
		return "[The Employee is a: "
				+ this.check()
				+ "] [The Employee ID is: "
				+this.getID()
				+ "] [Employee Name: " 
				+ this.getFirstName() 
				+" "
				+this.getLastName()
				+ "] [Phone Number: " 
				+ this.getPhoneNum() 
				+ "] [Email: " 
				+ this.getEmail() 
				+ "] [His Gendre is: " 
				+ this.getGender()
				+"]";
				
		
		}
}
