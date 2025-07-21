package workers;

import exception.EmptyInput;
import exception.MinBasePay;
import exception.ValidGender;

public class Administrative extends Employee {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private String role;
	
	public Administrative(int ID, String FirstName, String LastName, String PhoneNum, String Email,
			Gender Gender, int Basepay,String role) throws ValidGender, MinBasePay, EmptyInput {
		super(ID, FirstName, LastName, PhoneNum, Email, Gender, Basepay);
		setRole(role);
	}
	public Administrative(int ID, String FirstName, String LastName, String PhoneNum, String Email,Gender gender,int basepay) throws ValidGender, MinBasePay, EmptyInput {
		super(ID,FirstName,LastName,PhoneNum,Email,gender, ID);
		this.role = "Administrative";
		
		
		
		
		
	}

	public String getRole() {
		return role;
	}

	public void setRole(String role) {
		this.role = role;
	}
	public String toString() {
		return super.toString()
				+"[His monthly salary is: "
				+ Salary()
				+"] "
				+"[His role in the company is: "
				+ this.getRole()
				+"]";
		}

	
	
	
	
}
	
	

